"""
Written by Jason Krist
06/02/2024

TODO:
    - FIX COPY AND PASTE WITH CHECKBOX (new delegate?)
    - Check types trying to set to account for pasting
    - Test Copy and Paste with commas and double-quote
    - Add numerical filter option (text and number)
    - BUG: Discrete variable with a single option. Going from empty to index[0] doesnt update until click off window

    - create an "EDIT" button if string length is too long (lists)
    - create ItemModel with additional properties (similar to project_tree)
    - create a validator for list values
    - get resize func working with combo cols
    - CSV import and export buttons
    - use "TAB" button to move right column and enter down row
    - add float and int validation with more custom Delegates
    - add multi-copy and paste
    - Filterable and sortable columns (like Excel)
    - cell validation based on types of attributes
    - resize certain columns to fit?
    - Can i add option to make them all different windows? (no tabs, different docks)
"""

from copy import deepcopy
from io import StringIO
import csv
#from pandas import DataFrame
import numpy as np

from PySide6.QtCore import (  # pylint: disable=E0611,E0401,C0413
    Qt,
    QSortFilterProxyModel,
    QModelIndex,
    QAbstractTableModel,
)

from PySide6.QtWidgets import (  # pylint: disable=E0611,E0401,C0413
    QFrame,
    QTableView,
    QTabWidget,
    QStyledItemDelegate,
    QComboBox,
    QInputDialog,
    QMenu,
    QApplication,
    QMessageBox,
    QAbstractItemView,
)

try:
    from widgets import create_box
    import swoops.constants as CONS  # type: ignore # pylint: disable=E0611,E0401,C0413
    import helper as hp
    from swoops.structures import NotApplicable, Options, Empty
    from swoops.gui.undo_commands import NewObj, DelObj, EditObj
except ImportError:
    from swoops.gui.widgets import create_box
    from .. import constants as CONS
    from . import helper as hp
    from ..structures import NotApplicable, Options, Empty
    from .undo_commands import NewObj, DelObj, EditObj


ROW_RESIZE_LIMIT = 100

def type_cast(value, role):
    if isinstance(value, NotApplicable) and role == Qt.DisplayRole:
        return str(value)
    elif isinstance(value, bool):
        if role == Qt.CheckStateRole:
            return Qt.Checked if value else Qt.Unchecked
        elif role == Qt.DisplayRole:
            # Remove 'True'/'False' text for bools in DisplayRole
            return ""
    elif isinstance(value, Empty) and role == Qt.DisplayRole:
        return "" # "Empty"
    elif isinstance(value, Options) and role == Qt.DisplayRole:
        return value.value
    elif isinstance(value, list) and (role == Qt.DisplayRole or role == Qt.EditRole):
        return hp.list_to_str(value)
    elif role in (Qt.DisplayRole, Qt.EditRole):
        #print(f"type of value in type_cast: {type(value)}")
        if 'numpy' in str(type(value)):
            value = value.item()
        return value
    return None

class ProxyModel(QSortFilterProxyModel):
    """proxy model with sort override"""

    def lessThan(self, left_ind, right_ind):  # pylint: disable=C0103
        """override sorting comparison to order floats which are strings"""
        left_text = left_ind.data()
        right_text = right_ind.data()
        # print(f"     left: {left_text}     right: {right_text}")
        if hp.is_float(left_text) and hp.is_float(right_text):
            return float(left_text) < float(right_text)
        else:
            return left_text < right_text

class TypeBasedDelegate(QStyledItemDelegate):
    """Delegate uses different editors depending on data type or column."""

    def createEditor(self, parent, option, index):
        value = index.model().sourceModel().get_value(index)
        num = None
        if isinstance(value, Empty):
            if value._type is Options:
                num = 0
        elif isinstance(value, Options):
            num = 0
            if value.value in value.options:
                num = value.index()
        if num is not None:  # Options use QComboBox
            if value.options:
                editor = QComboBox(parent)
                editor.addItems(value.options)
                editor.setCurrentIndex(num)
                # Commit and close editor immediately on change
                editor.currentIndexChanged.connect(
                    lambda: self.commitData.emit(editor)
                )
                editor.currentIndexChanged.connect(
                    lambda: self.closeEditor.emit(editor, QStyledItemDelegate.NoHint)
                )
                return editor
        else:
            return super().createEditor(parent, option, index)

    def setEditorData(self, editor, index):
        value = index.model().sourceModel().get_value(index)
        if isinstance(editor, QComboBox):
            #idx = editor.findText(str(value))
            #editor.setCurrentIndex(idx if idx >= 0 else 0)
            #print(f"    setEditorData: {value} ({type(value)})")
            #print(f" EDITOR COUNT: {editor.count()}")
            if editor.count() == 0:
                return None
            num = 0
            if isinstance(value, Empty):
                num = editor.currentIndex()
            elif isinstance(value, Options):
                num = 0 if value.index() is None else value.index()
                #print(f"    setEditorData Options: {value.value}, {value.options}")
            current_index = editor.currentIndex()
            if num == current_index:
                editor.showPopup()
            else:
                editor.setCurrentIndex(num)
                # Move below to createEditor to be more efficient?
                editor.currentIndexChanged.connect(self.commit_editor)
        else:
            super().setEditorData(editor, index)

    def setModelData(self, editor, model, index):
        if isinstance(editor, QComboBox):
            #print(f"    1. setModelData HERE")
            model.sourceModel().set_value(index, editor.currentText())
        else:
            super().setModelData(editor, model, index)

    def paint(self, painter, option, index):
        """paint (keeps combobox showing at all times)"""
        if isinstance(self.parent(), QAbstractItemView):
            self.parent().openPersistentEditor(index)
        super(TypeBasedDelegate, self).paint(painter, option, index)

    def commit_editor(self):
        """commit_editor"""
        self.commitData.emit(self.sender())

    def updateEditorGeometry(
        self, editor, option, index
    ):  # pylint: disable=C0103,W0613# pylint: disable=C0103,W0613
        """updateEditorGeometry"""
        editor.setGeometry(option.rect)

class TabTableModel(QAbstractTableModel):
    """A model to interface a Qt view with object from Structures.py"""

    def __init__(self, integrator, parent_trace, attr_name, editable=True):
        super().__init__()
        self.integrator = integrator
        self.parent_trace = parent_trace
        self.parent = parent_trace.get_obj(self.integrator.session)
        self.object = getattr(self.parent, attr_name)
        self.trace = None
        self.views = []
        self.editable = editable
        self.columns = []
        self.indices = []
        self.attr_names = []
        self.load_object(self.object)

    def load_object(self, object:dict):
        #self.beginResetModel()
        print(f"TabTableModel Loading # Objects: {len(object)}")
        self.object = object
        if self.object:
            self.trace = self.parent_trace.new(list(self.object.values())[0].__class__)
        else:
            self.trace = None
        if self.object:
            first_key = list(self.object.keys())[0]
            viewable_names = [attr for attr in vars(self.object[first_key]) if (not attr.startswith("_") or attr == CONS.TYPE)]
            self.columns = hp.clean_colnames(viewable_names)
            self.indices = list(range(1, len(self.object)+1))
            self.attr_names = hp.unclean_colnames(self.columns)
        #self.endResetModel()

    def rowCount(self, *args) -> int:  # pylint: disable=C0103
        """Override method from QAbstractTableModel. Return row count as number of objects in list."""
        return len(self.object)

    def columnCount(self, *args) -> int:  # pylint: disable=C0103
        """Override method from QAbstractTableModel. Return column count as number of attributes in object list."""
        return len(self.columns)

    def get_value(self, index:QModelIndex):
        key = list(self.object.keys())[index.row()]
        obj = self.object[key]
        attr_name = self.attr_names[index.column()]
        return getattr(obj, attr_name)

    def get_index(self, trace):
        if self.trace is None:
            return None
        if not self.trace.contains(trace):
            return None
        #print(f"TABLE TRACE: {self.trace}, {len(self.trace)}")
        #print(f"TABLE INPUT TRACE: {trace}, {len(trace)}")
        #print(f"TABLE CONTAINS: {self.trace.contains(trace)}")
        id_list = list(self.object.keys())
        #print(f"TABLE ID LIST: {id_list}")
        if not id_list:
            return None
        row = id_list.index(trace.obj_id)
        #print(f"TABLE ATTR_NAMES: {self.attr_names}")
        column = self.attr_names.index(trace.attr_obj)
        return self.createIndex(row, column)

    def set_value(self, index:QModelIndex, new_value):
        """callable for pasting and double click for checkboxes"""
        key = list(self.object.keys())[index.row()]
        obj = self.object[key]
        attr_name = self.attr_names[index.column()]
        old_value = self.get_value(index)
        if isinstance(old_value, NotApplicable):
            return
        elif isinstance(old_value, bool):
            if isinstance(new_value, str):
                if new_value.lower() not in ["true","false"]:
                    return
            new_value = bool(new_value)
        elif isinstance(old_value, Options):
            option = deepcopy(old_value) # copy?
            option.value = new_value
            new_value = option
        elif isinstance(old_value, list):
            new_value = hp.str_to_list(new_value)
        #elif isinstance(old_value, Empty):
        #    if old_value._type is Options:
        #        new_value = Options(obj.options, new_value)
        #else:
        #    setattr(obj, attr_name, new_value)
        #print(f"    2. BEFORE set_value: {obj}, {attr_name} = {new_value}")
        self.edit(obj._trace, attr_name, new_value)
        self.dataChanged.emit(index, index)

    def data(self, index: QModelIndex, role=Qt.ItemDataRole):
        """Override method from QAbstractTableModel. Return data from the object list."""
        if index.isValid():
            value = self.get_value(index)
            return_val = type_cast(value, role)
            return return_val
        return None

    def setData(self, index: QModelIndex, new_value, role):
        key = list(self.object.keys())[index.row()]
        obj = self.object[key]
        attr_name = self.attr_names[index.column()]
        old_value = getattr(obj, attr_name)
        if isinstance(old_value, Options):
            option = deepcopy(old_value) # copy?
            option.value = new_value
            self.edit(obj._trace, attr_name, option)
            #print(f"    combo setData: {obj}, {attr_name}, {new_value}")
            #self.dataChanged.emit(index, index)
            return True
        elif isinstance(old_value, Empty):
            if old_value._type is Options:
                self.edit(obj._trace, attr_name, Options(obj.options, new_value))
                #print(f"    empty combo setData: {obj}, {attr_name}, {new_value}")
                #self.dataChanged.emit(index, index)
                return True
            else:
                self.edit(obj._trace, attr_name, new_value)
                #print(f"    empty setData: {obj}, {attr_name}, {new_value}")
                #self.dataChanged.emit(index, index)
                return True
        elif isinstance(old_value, list):
            self.edit(obj._trace, attr_name, hp.str_to_list(new_value))
            #print(f"    list setData: {obj}, {attr_name}, {new_value}")
            #self.dataChanged.emit(index, index)
            return True
        if role == Qt.EditRole:
            self.edit(obj._trace, attr_name, new_value)
            #print(f"    reg setData: {obj}, {attr_name}, {new_value}")
            #self.dataChanged.emit(index, index)
            return True
        return False

    def headerData(  # pylint: disable=C0103
        self, section: int, orientation: Qt.Orientation, role: Qt.ItemDataRole
    ):
        """Override method from QAbstractTableModel. Return object attributes as horizontal header data."""
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self.columns[section])
            else:
                return str(self.indices[section])
        return None

    def flags(self, index: QModelIndex):
        value = self.get_value(index)
        if not self.editable:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled
        if isinstance(value, NotApplicable):
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable
        if isinstance(value, bool):
            return Qt.ItemIsEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsSelectable
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

    def edit(self, trace, attr_name, new_value):
        attr_trace = trace.attr(attr_name)
        #print(f"    3. TABLE EDIT TRACE = {attr_trace}, {new_value}, {type(new_value)}")
        self.integrator.exec(EditObj, args=(attr_trace,new_value))

    def update(self, trace):
        index = self.get_index(trace)
        # TODO: change entire row to handle attribute changes like Input Type
        # TODO: get index range for deletions and new items (above and below for deletion, )
        # OR USED beginRemoveRows,  endRemoveRows and beginInsertRows, endInsertRows
        if index is not None:
            #print(f"TABLE VIEW UPDATE ROW: {index.row()}")
            row_start = self.index(index.row(), 0)
            row_end = self.index(index.row(), self.columnCount()-1)
            self.dataChanged.emit(row_start, row_end)

class TabTableModels(dict):
    def __init__(self, integrator, trace):
        self.integrator = integrator
        self.trace = trace
        self.object = trace.get_obj(self.integrator.session)
        self.models = []
        for key, value in self.object.__dict__.items():
            if isinstance(value, (dict)):
                self.models.append((key, TabTableModel(self.integrator, self.trace, key)))
        super().__init__(self.models)

    def update(self, trace):
        
        for model in self.values():
            model.update(trace)

class TabTableViews(QFrame):
    """project tree viewer"""

    def __init__(self, integrator):
        super().__init__()
        self.integrator = integrator
        self.box = create_box(self, vertical=True)
        self.tabs = QTabWidget(self)
        self.box.addWidget(self.tabs)
        self.models = self.integrator.models[TabTableModels]
        # s[parent.active_workflow]
        self.proxies = {}
        self.views = {}
        self.tabinds = {}
        self.delegates = {}
        self.tabs.currentChanged.connect(self.on_tab_changed)
        #if self.models:
        #    self.create_view(list(self.models.keys())[0])
        self.shown_tabs = []
        self.create_views()

    def create_view(self, key):
        model = self.models[key]
        proxy = ProxyModel(self)
        proxy.setSourceModel(model)
        self.proxies[key] = proxy
        label = hp.title(key)
        view = TableView(proxy)
        model.views.append(view)
        #view.setModel(proxy)
        self.views[key] = view
        tabind = self.tabs.addTab(view, label)
        self.tabinds[tabind] = key
        # TODO: need to set this to visible if a value is added (not empty anymore)
        if proxy.rowCount() == 0:
            self.tabs.setTabVisible(tabind, False)
        else:
            self.shown_tabs.append(tabind)
        #print(f"shown tabs: {self.shown_tabs}")

    def create_views(self):
        """update table views and proxy models"""
        for key in self.models.keys():
            self.create_view(key)
        if self.shown_tabs:
            self.tabs.setCurrentIndex(self.shown_tabs[0])
        # Below line adds 20 seconds with 10k rows
        self.resize_cols()

    # TODO: only should resize the specific view that changed
    def resize_cols(self, only_tab=None):
        """resize all columns after contents change"""
        for tabname, model in self.models.items():
            if model.rowCount() > ROW_RESIZE_LIMIT:
                continue
            if (only_tab is not None) and (only_tab != tabname):
                continue
            for colnum in range(model.columnCount(QModelIndex())):
                # if c not in model.combo_columns.keys():
                view = self.views[tabname]
                view.resizeColumnToContents(colnum)

    def set_tabs_visible(self):
        """set tabs invisible if proxy model is empty and visible otherwise"""
        for ind, (tabname, model) in enumerate(self.models.items()):
            if model.rowCount() > 0:
                self.tabs.setTabVisible(ind, True)
                if model.rowCount() <= ROW_RESIZE_LIMIT:
                    self.resize_cols(only_tab=tabname)
            else:
                self.tabs.setTabVisible(ind, False)

    def on_tab_changed(self, index):
        """
        This function is called whenever the current tab is changed.
        The 'index' argument represents the index of the newly selected tab.
        """
        #print(f"Tab changed to index: {index}")
        #print(f"New current tab text: {self.tabs.tabText(index)}")
        if index not in self.tabinds:
            return
        key = self.tabinds[index]
        if key not in self.models:
            print("!!!! MODEL CREATED HERE FROM INTEGRATOR?")
            #self.models[key] = TabTableModel(self.integrator, )
        if key not in self.views:
            self.create_view(key)


class TableView(QTableView):
    """table view with custom context menu"""

    def __init__(self, proxy_model):
        super().__init__()
        self.setItemDelegate(TypeBasedDelegate())
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.table_context)
        self.horizontalHeader().setContextMenuPolicy(Qt.CustomContextMenu)
        self.horizontalHeader().customContextMenuRequested.connect(self.header_context)
        self.keyPressEvent = self.key_press  # pylint: disable=C0103
        self.doubleClicked.connect(self.double_click)
        self.setModel(proxy_model)
        model_obj = self.model().sourceModel().object
        self.trace = model_obj.trace if hasattr(model_obj, 'trace') else None

    def find_header_col(self, name):
        """find index of header column with given name"""
        for colnum in range(self.model().sourceModel().columnCount()):
            #header = self.model().sourceModel().horizontalHeaderItem(colnum)
            header = self.model().sourceModel().headerData(colnum, Qt.Horizontal, Qt.DisplayRole)
            header_name = hp.lower(header) # .text()
            if header_name == name:
                return colnum
        return None

    def resize_col(self, colname):
        """resize single column by name"""
        colnum = self.find_header_col(colname)
        if colnum is not None:
            self.resizeColumnToContents(colnum)

    def key_press(self, event):
        """copy and paste upon keypress"""
        if event.key() == 67:
            self.copy()
        elif event.key() == 86:
            self.paste()
        else:
            super().keyPressEvent(event)

    def double_click(self, index):
        """check box when double-clicked"""
        src_index = self.model().mapToSource(index)
        value = self.model().sourceModel().get_value(src_index)
        if isinstance(value, bool):
            if value:
                self.model().sourceModel().set_value(src_index, False)
            else:
                self.model().sourceModel().set_value(src_index, True)

    def header_context(self, pos):
        """context menu on right click for headers"""
        col = self.indexAt(pos).column()
        menu = QMenu()
        sort_asc_action = menu.addAction("Sort Asc")
        sort_des_action = menu.addAction("Sort Desc")
        regex_filter_action = menu.addAction("Regex Filter")
        num_filter_action = menu.addAction("Number Filter")
        clear_filter_action = menu.addAction("Clear Filter")
        action = menu.exec_(self.viewport().mapToGlobal(pos))
        print(f"    action: {action}")
        if action == sort_asc_action:
            self.model().sort(col, Qt.AscendingOrder)
        elif action == sort_des_action:
            self.model().sort(col, Qt.DescendingOrder)
        elif action == regex_filter_action:
            text, ok = QInputDialog.getText(
                self, "Filter Table Column", "Regex Filter: "
            )
            if ok and text:
                # TODO: add regex filter shown somewhere
                # textLabel.setText(text)
                self.model().setFilterKeyColumn(col)
                self.model().setFilterRegularExpression(text)
        elif action == num_filter_action:
            # TODO: add better number filters (additional menus?)
            text, ok = QInputDialog.getText(
                self, "Filter Table Column", "Number Filter: "
            )
            if ok and text:
                # textLabel.setText(text)
                self.model().setFilterKeyColumn(col)
                self.model().setFilterRegularExpression(text)
        elif action == clear_filter_action:
            self.model().setFilterRegularExpression("")

    def table_context(self, pos):
        """open context menu on right click for table"""
        index = self.indexAt(pos)
        if not index.isValid():
            return
        menu = QMenu()
        copy_action = menu.addAction("&Copy")
        paste_action = menu.addAction("&Paste")
        edit_action = menu.addAction("&Edit")
        delete_action = menu.addAction("&Delete")
        action = menu.exec_(self.viewport().mapToGlobal(pos))
        if action == copy_action:
            self.copy()
        elif action == paste_action:
            self.paste()
        elif action == edit_action:
            self.open_edit(index)
        elif action == delete_action:
            self.delete()

    def copy(self):
        """copy current table selection"""
        clipboard = QApplication.clipboard()
        indexlist = self.selectedIndexes()
        csvlines = ""
        csvline = ""
        last_row = -1
        sep = "\t"  # ","
        for index in indexlist:
            src_index = self.model().mapToSource(index)
            value = self.model().sourceModel().get_value(src_index)
            text = str(value)
            if isinstance(value, Options):
                text = str(value.value)
            # TODO: add list to str
            if last_row < 0:
                last_row = index.row()
            if index.row() == last_row:
                csvline += text + sep
            else:
                csvlines += csvline[:-1] + "\n"
                csvline = text + sep
                last_row = index.row()
        csvlines += csvline[:-1]
        # print(csvlines)
        clipboard.setText(csvlines)

    def paste(self):
        """paste current table selection"""
        # TODO: should i create rows if they dont exist?
        cliptext = QApplication.clipboard().text()
        # print(cliptext)
        csvfile = StringIO(cliptext)
        sep = "\t"
        csvreader = csv.reader(csvfile, delimiter=sep)
        startrow = self.selectedIndexes()[0].row()
        startcol = self.selectedIndexes()[0].column()
        for rownum, row in enumerate(csvreader):
            for colnum, cellval in enumerate(row):
                index = self.model().index(
                    rownum + startrow, colnum + startcol, QModelIndex()
                )
                src_index = self.model().mapToSource(index)
                self.model().sourceModel().set_value(src_index, cellval)

    def delete(self):
        """delete selected rows"""
        q_str = "Are you sure you want to delete all selected rows?"
        opts = QMessageBox.Yes | QMessageBox.No
        ans = QMessageBox.question(self, "Confirm Delete", q_str, opts)
        if ans == QMessageBox.Yes:
            indexlist = self.selectedIndexes()
            items = []
            for index in indexlist:
                src_index = self.model().mapToSource(index)
                value = self.model().sourceModel().data(src_index, Qt.DisplayRole)
                items.append(value)
            for item in items:
                print(f"tableview delete item: {item}")
                # trace = get_trace(item)
                # if len(trace) % 2 != 0:
                #     trace = trace[1:]
                # change = {"old": item.text(), "new": None}
                # print(f"table_view delete: {trace}, {change}")
                # self.model().sourceModel().exec_call(trace, change)

    def open_edit(self, index):
        """edit currently selected row item"""
        src_index = self.model().mapToSource(index)
        value = self.model().sourceModel().data(src_index, Qt.DisplayRole)
        check_value = self.model().sourceModel().data(src_index, Qt.CheckStateRole)
        print(f"tableview send to edit item: {value} {check_value}")
        #trace = get_trace(item)
        #self.model().sourceModel().edit_call(trace)
