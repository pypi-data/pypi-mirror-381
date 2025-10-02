"""
Written by Jason Krist
05/01/2024

TODO:
    - Persistent editors may not update with each other... so still need to recreate widgets!
    - ADD IN EDITABLE PROPERTY
    
    - dont include fields that dont apply to type (check with =None?) or greyed out
    - for ID selections, widget should be checkbox menu or combobox
    - change form based on Variable Type (discrete, sequence) and change variable types
    - highlight color on button hover
    - resize list sizes based on number of lists and remaining space?
    - For lists, create buttons by reference ID (tasks, pools, outputs/constraints)
        - if is int and "ID" in name, look through list of references and make a combobox
    - Right click > open in new window (for comboboxes)
    - Should I also make the form a table to allow copy and paste?
    - make long text a textArea instead of Line
    - set confirmed line edits a different color (ones that update on enter)
"""

from copy import deepcopy
from functools import partial
from matplotlib.figure import Figure
from pandas import DataFrame

from PySide6.QtCore import (  # pylint: disable=E0611,E0401,C0413
    QSize,
    Qt,
    QSortFilterProxyModel,
    QModelIndex,
    QAbstractTableModel,
)

from PySide6.QtWidgets import (  # pylint: disable=E0611,E0401,C0413
    QFrame,
    QLineEdit,
    QComboBox,
    QCheckBox,
    QPushButton,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QWidget,
    QFileDialog,
    QTableView,
    QStyledItemDelegate,
    QInputDialog,
    QMenu,
    QApplication,
    QMessageBox,
    QAbstractItemView,
    QSizePolicy,
    QHeaderView,
)

# from PySide6.QtCore import Qt  # pylint: disable=E0611,E0401,C0413
from PySide6.QtGui import QDoubleValidator, QIntValidator  # pylint: disable=E0611,E0401,C0413

try:
    from swoops.gui import widgets as wd  # type: ignore # pylint: disable=E0611,E0401,
    import swoops.constants as CONS  # type: ignore # pylint: disable=E0611,E0401,C0413
    from swoops import helper as hp
    from swoops.structures import NotApplicable, Options, BaseClass, Empty
    from swoops.gui.undo_commands import NewObj, DelObj, EditObj
except ImportError:
    from . import widgets as wd
    from .. import constants as CONS
    from . import helper as hp
    from ..structures import NotApplicable, Options, BaseClass, Empty
    from .undo_commands import NewObj, DelObj, EditObj

MINWIDTH = 200
ROWHEIGHT = 18
MAXROWS = 5

def print_placeholder(*args):
    print("Placeholder function called with args: ", args)

class EditTableModel(QAbstractTableModel):
    """A model to interface a Qt view with object from Structures.py"""

    def __init__(self, integrator, current=None, editable=True):
        super().__init__()
        self.integrator = integrator
        self.session = self.integrator.session
        self.object = self.integrator.session if current is None else current
        self.trace = self.object._trace if hasattr(self.object, "_trace") else None
        self.editable = editable
        self.labels = []
        self.widgets = {}
        self.open_calls = []
        self.columns = ["Attribute","Value"]
        self.indices = []
        self.views = []
        self.parent = None
        self.load_object(self.object)

    def load_object(self, object):
        self.open_all_editors(False)
        self.beginResetModel()
        print(f"EditTableModel Loading Object: {object}")
        self.object = object
        self.trace = self.object._trace if hasattr(self.object, "_trace") else None
        if self.object:
            viewable_names = [attr for attr in vars(self.object) if (not attr.startswith("_") or (attr in (CONS.TYPE,CONS.ID,"_trace")))]
            self.indices = hp.clean_colnames(viewable_names) # ["ID"]+
            self.attr_names = hp.unclean_colnames(viewable_names)
            self.attr_num = len(self.attr_names)
            #print(f"\nobject trace: {getattr(self.object, '_trace', None)}")
            if hasattr(self.object, '_trace'):
                self.parent = self.object._trace.parent(self.session)
            else:
                self.parent = None
        self.endResetModel()
        self.open_all_editors(True)

    def open_all_editors(self, open:bool):
        del_inds = []
        for i, view in enumerate(self.views):
            exists = view.open_editors(open)
            if not exists:
                del_inds.append(i)
        self.views = [view for i,view in enumerate(self.views) if i not in del_inds]

    def rowCount(self, *args, parent=QModelIndex()) -> int:  # pylint: disable=C0103
        """Override method from QAbstractTableModel. Return row count as number of objects in list."""
        return len(self.indices)

    def columnCount(self, *args, parent=QModelIndex()) -> int:  # pylint: disable=C0103
        """Override method from QAbstractTableModel. Return column count as number of attributes in object list."""
        return len(self.columns)

    def get_value(self, index:QModelIndex):
        attr_name = self.attr_names[index.row()]
        if index.column() == 0:
            return hp.clean_colnames([attr_name])[0]
        return getattr(self.object, attr_name)

    def get_index(self, trace):
        #print(f"EDIT TRACE: {self.trace}, {len(self.trace)}")
        #print(f"EDIT INPUT TRACE: {trace}, {len(trace)}")
        #print(f"EDIT CONTAINS: {self.trace.contains(trace)}")
        if self.trace is None:
            return None
        if not self.trace.contains(trace):
            return None
        #print(f"EDIT ATTR NAMES: {self.attr_names}")
        if trace.attr_obj == CONS.NAME:
            trace = self.trace.new(trace.obj_class)
            #print(f"EDIT INPUT TRACE 2: {trace}")
        if len(trace) > len(self.trace) + 2:
            return None
        row = self.attr_names.index(trace.attr_obj)
        return self.createIndex(row, 1)

    def set_value(self, index:QModelIndex, value):
        if index.column() == 0:
            return
        attr_name = self.attr_names[index.row()]
        old_value = getattr(self.object, attr_name)
        if isinstance(old_value, NotApplicable):
            return
        #elif isinstance(old_value, bool):
        #    if isinstance(value, str):
        #        if value.lower() not in ["true","false"]:
        #            return
        #    value = bool(value)
        #elif isinstance(old_value, Options):
        #    option = deepcopy(old_value)
        #    option.value = value
        #    value = option
        elif isinstance(old_value, list) and (not isinstance(value, list)):
            value = hp.str_to_list(value)
        #print(f"    old_value = {old_value} ({type(old_value)}), value = {value} ({type(value)})")
        #print(f"    old_value.value = {old_value.value} ({type(old_value.value)}), value = {value.value} ({type(value.value)})")
        #setattr(self.object, attr_name, value)
        #print(f"Setting {attr_name} to {value} in {self.object}")
        self.open_all_editors(False)
        self.edit(self.object._trace, attr_name, value)
        #self.beginResetModel()
        #self.dataChanged.emit(col_start, col_end)
        #self.endResetModel()
        self.open_all_editors(True)

    def data(self, index: QModelIndex, role=Qt.ItemDataRole):
        """Override method from QAbstractTableModel. Return data from the object list."""
        if index.isValid():
            attr_name = self.attr_names[index.row()]
            value = self.get_value(index)
            if attr_name in (CONS.ID,"_trace") and role == Qt.DisplayRole:
                if index.column() == 0 and attr_name == "_trace":
                    return "Parent"
                return value
            elif isinstance(value, NotApplicable) and role == Qt.DisplayRole:
                return str(value)
            elif isinstance(value, bool) and role == Qt.DisplayRole:
                return ""
            #    return Qt.Checked if value else Qt.Unchecked
            elif isinstance(value, Options) and role == Qt.DisplayRole:
                return "" # value.value
            #elif isinstance(value, list) and (role == Qt.DisplayRole or role == Qt.EditRole):
            #    return hp.list_to_str(value)
            elif isinstance(value, (dict,list)) and role == Qt.DisplayRole:
                return ""
            elif role == Qt.DisplayRole or role == Qt.EditRole:
                return str(value)
        return None

    def setData(self, index: QModelIndex, value, role=Qt.EditRole):
        attr_name = self.attr_names[index.row()]
        old_value = getattr(self.object, attr_name)
        # if isinstance(old_value, Options):
        #     option = old_value
        #     option.value = value
        #     self.edit(self.object._trace, attr_name, option)
        #     return True
        # elif isinstance(old_value, list):
        #     self.edit(self.object._trace, attr_name, hp.str_to_list(value))
        #     return True
        # elif isinstance(old_value, float):
        #     self.edit(self.object._trace, attr_name, float(value))
        #     return True
        # elif isinstance(old_value, int):
        #     self.edit(self.object._trace, attr_name, int(value))
        #     return True
        print(f"new_value = {value} ({type(value)}), old_value = {old_value} ({type(old_value)})")
        if role == Qt.EditRole:
            self.edit(self.object._trace, attr_name, value)
            return True
        return False

    def headerData(  # pylint: disable=C0103
        self, section: int, orientation: Qt.Orientation, role: Qt.ItemDataRole
    ):
        """Override method from QAbstractTableModel. Return object attributes as horizontal header data."""
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self.columns[section])
            #else:
            #    raise ValueError("ObjectTableModel does not currently support Vertical headers.")
        return None

    def flags(self, index: QModelIndex):
        value = self.get_value(index)
        attr_name = self.attr_names[index.row()]
        if (not self.editable) or (attr_name == CONS.ID) or (index.column() == 0):
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled
        if isinstance(value, NotApplicable):
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable
        if isinstance(value, bool):
            return Qt.ItemIsEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsSelectable
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

    def create_widget(self, parent, attr_name):
        #for key in dir(self.object):
        #value = getattr(self.object, attr_name)
        label = hp.title(attr_name)
        index = self.index(self.attr_names.index(attr_name), 1)
        value = self.get_value(index)
        if attr_name == CONS.ID:
            #widget = QLabel(str(value), parent=parent)
            return None
        elif isinstance(value, NotApplicable):
            widget = QLabel("-", parent=parent)
        # TODO: fix below for kwargs
        elif isinstance(value, dict) and not value:
            widget = QLabel("None", parent=parent)
        elif isinstance(value, dict) and hasattr(list(value.values())[0], "name"):
            #print(f"Creating label list for {attr_name} with value: {value}")
            sublabels = [subval.name for subval in value.values()]
            calls = [lambda i=i: self.load_object(i) for i in value.values()]
            self.open_calls.append(calls)
            widget = ButtonList(sublabels, calls, parent)
        elif not self.editable and isinstance(value, dict | list):
            widget = LabelList(value, parent)
        elif not self.editable:
            if attr_name == CONS.TYPE:
                value = getattr(self.object, CONS.TYPE).value
            widget = QLabel(str(value))
        elif isinstance(value, Empty):
            if value._type is Options:
                # label = "Type"
                widget = QComboBox(parent=parent)
                #print(f"    value: {value.value}\n    options: {value.options}")
                widget.addItems(value.options)
                widget.setCurrentText("")
                widget.setProperty('value', value.value)
                widget.currentTextChanged.connect(lambda v: self.set_value(index, Options(value.options, v)))
            elif value._type is float:
                # widget = QDoubleSpinBox(self) #widget.setRange(-1000000000, 1000000000)
                widget = QLineEdit("", parent=parent)
                widget.setText("")
                validator = QDoubleValidator(-1000000000.0, 1000000000.0, 10)
                # validator.setNotation(QDoubleValidator.StandardNotation)
                widget.setValidator(validator)
                widget.editingFinished.connect(lambda: self.set_value(index, float(widget.text())))
            elif value._type is int:
                # widget = QDoubleSpinBox(self) #widget.setRange(-1000000000, 1000000000)
                widget = QLineEdit("", parent=parent)
                widget.setText("")
                validator = QIntValidator(-1000000000, 1000000000)
                # validator.setNotation(QDoubleValidator.StandardNotation)
                widget.setValidator(validator)
                widget.editingFinished.connect(lambda: self.set_value(index, int(widget.text())))
            else:
                widget = QLineEdit("", parent=parent)
                widget.setText("")
                widget.clear()
                print(f"WIDGET TEXT: {widget.text()}")
                widget.editingFinished.connect(lambda: self.set_value(index, widget.text()))
        elif isinstance(value, Options):  # key == CONS.TYPE or
            #print(f"    Creating combobox for {attr_name} with value: {value}")
            # label = "Type"
            widget = QComboBox(parent=parent)
            #print(f"    value: {value.value}\n    options: {value.options}")
            widget.addItems(value.options)
            widget.setCurrentText(value.value)
            widget.setProperty('value', value.value)
            widget.currentTextChanged.connect(lambda v: self.set_value(index, Options(value.options, v)))
        elif attr_name == "_trace":
            #print(f"Creating _trace button for {attr_name} with value: {value}, parent={self.parent}")
            widget = QPushButton(f"Open {str(self.parent.name)}", parent=parent)
            widget.clicked.connect(partial(self.load_object, self.parent))
        elif attr_name[0] == "_":
            return None
        elif callable(value):
            call = print_placeholder
            widget = QPushButton(attr_name, parent=parent)
            widget.clicked.connect(partial())
        elif isinstance(value, bool):
            widget = QCheckBox(parent=parent)
            widget.setChecked(value)
            widget.stateChanged.connect(lambda state: self.set_value(self.index(self.attr_names.index(attr_name), 1), bool(state)))
        elif isinstance(value, float):
            # widget = QDoubleSpinBox(self) #widget.setRange(-1000000000, 1000000000)
            widget = QLineEdit(str(value), parent=parent)
            validator = QDoubleValidator(-1000000000.0, 1000000000.0, 10)
            # validator.setNotation(QDoubleValidator.StandardNotation)
            widget.setValidator(validator)
            widget.editingFinished.connect(lambda: self.set_value(index, float(widget.text())))
        elif isinstance(value, int):
            # widget = QDoubleSpinBox(self) #widget.setRange(-1000000000, 1000000000)
            widget = QLineEdit(str(value), parent=parent)
            validator = QIntValidator(-1000000000, 1000000000)
            # validator.setNotation(QDoubleValidator.StandardNotation)
            widget.setValidator(validator)
            widget.editingFinished.connect(lambda: self.set_value(index, int(widget.text())))
        elif isinstance(value, str) and "file" in attr_name.lower():
            widget = FileEditWidget(value, lambda: self.set_value(index, widget.lineedit.text()), parent)
        elif isinstance(value, str) or value is None:
            widget = QLineEdit(value, parent=parent)
            widget.editingFinished.connect(lambda: self.set_value(index, widget.text()))
        elif isinstance(value, dict):
            value_list = [f"'{subkey}':{subval}" for subkey, subval in value.items()]
            widget = EditList(value_list, attr_name, lambda v: self.set_value(index, v), parent)
        elif isinstance(value, list|tuple):
            #print(f"    CREATING EDITLIST FOR {attr_name} with value: {value}")
            widget = EditList(value, attr_name, lambda v: self.set_value(index, v), parent)
        elif isinstance(value, DataFrame):
            widget = QLabel("Dataframe in Table")
        elif isinstance(value, BaseClass):
            if value:
                calls = [lambda i=i: self.load_object(i) for i in [value]]
                self.open_calls.append(calls)
                widget = ButtonList([value.name], calls, parent)
            else:
                widget = QLabel("None", parent=parent)
        # elif value is None:
        #    widget = QLabel("None")
        elif isinstance(value, Figure):
            widget = QLabel(str(value), parent=parent)
        else:
            raise ValueError(
                f"Type {type(value)} not supported by EditWindow class.\n    value: {value}"
            )
        widget.setMinimumWidth(MINWIDTH / 2)
        widget.setMinimumHeight(ROWHEIGHT)
        self.labels.append(label)
        self.widgets[attr_name] = widget
        return widget

    def edit(self, trace, attr_name, new_value):
        #print(f"EDIT WINDOW TRACE = {trace}")
        attr_trace = trace.attr(attr_name)
        #print(f"EDIT WINDOW EDIT TRACE = {attr_trace}")
        self.integrator.exec(EditObj, args=(attr_trace,new_value))

    def update(self, trace):
        self.open_all_editors(False)
        #self.beginResetModel()
        index = self.get_index(trace)
        if index is not None:
            col_start = self.index(0, index.column())
            col_end = self.index(self.rowCount()-1, index.column())
            #print(f"col start = {col_start.row()},{col_start.column()}, col end = {col_end.row()},{col_end.column()}")
            #print(f"EDIT WINDOW UPDATE INDEX: ({col_start}, {col_end})")
            self.dataChanged.emit(col_start, col_end)
        #self.endResetModel()
        self.open_all_editors(True)

class TypeBasedDelegate(QStyledItemDelegate):
    """Delegate uses different editors depending on data type or column."""

    def createEditor(self, parent, option, index):
        model = index.model().sourceModel()
        attr_name = model.attr_names[index.row()]
        flags = model.flags(index)
        if (attr_name == CONS.ID) or (index.column() == 0) or not (flags & Qt.ItemIsEditable):
            return None
        editor = model.create_widget(parent, attr_name)
        return editor if editor is not None else super().createEditor(parent, option, index)

    def setEditorData(self, editor, index):
        super().setEditorData(editor, index)

    def setModelData(self, editor, model, index):
        #if isinstance(editor, QComboBox):
        #    model.sourceModel().set_value(index, editor.currentText())
        #else:
        #super().setModelData(editor, model, index)
        pass

    def paint(self, painter, option, index):
        """paint (keeps combobox showing at all times)"""
        #if isinstance(self.parent(), QAbstractItemView):
        #    self.parent().openPersistentEditor(index)
        super(TypeBasedDelegate, self).paint(painter, option, index)

    def commit_editor(self):
        """commit_editor"""
        #self.commitData.emit(self.sender())
        super().commit_editor()

    def updateEditorGeometry(
        self, editor, option, index
    ):  # pylint: disable=C0103,W0613# pylint: disable=C0103,W0613
        """updateEditorGeometry"""
        editor.setGeometry(option.rect)

class EditWindow(QFrame):
    """form for editing details of data structures"""

    def __init__(self, integrator):
        super().__init__()
        self.integrator = integrator
        self.box = wd.create_box(self, vertical=True)
        self.setMinimumWidth(MINWIDTH)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.model = self.integrator.models[EditTableModel]
        self.view = EditView(self.model)
        self.view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.box.insertWidget(0, self.view, 1)  # stretch factor 1
        self.setLayout(self.box)
        self.view.open_editors(True)


class LabelList(QListWidget):
    """list widget containing QLabels (uneditable)"""

    def __init__(self, listvals, parent):
        super().__init__(parent)
        if isinstance(listvals, dict):
            listvals = list(listvals.values())
        for listval in listvals:
            item = QListWidgetItem(str(listval))
            self.insertItem(self.count(), item)
        rowheight = ROWHEIGHT
        maxrows = MAXROWS
        height = len(listvals) * rowheight
        if height > rowheight * maxrows:
            height = rowheight * maxrows
        self.setFixedHeight(height+25)

class ButtonList(QListWidget):
    """list widget which runs callbacks upon clicking items"""

    def __init__(self, labels, callbacks, parent):
        super().__init__(parent)
        self.addItems(labels)
        self.callbacks = callbacks
        self.itemClicked.connect(self.item_click)
        rowheight = ROWHEIGHT
        maxrows = MAXROWS
        height = len(labels) * rowheight
        if height > rowheight * maxrows:
            height = rowheight * maxrows
        # self.setMinimumHeight(minheight)
        # self.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        # self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        # self.resize(40, height)
        # TODO: add + button to button lists (new)
        self.setFixedHeight(height+25)

    def item_click(self, item):
        """open the list item that is clicked"""
        model_ind = self.indexFromItem(item)
        self.callbacks[model_ind.row()]()

class EditList(QWidget):
    """edit list with new button under"""

    def __init__(self, listvals, key, item_changed, parent):
        QWidget.__init__(self, parent)
        self.box = wd.create_box(self, vertical=True)
        self.editlist = EditListWidget(listvals, key, item_changed, parent)
        self.newbutton = QPushButton("+")
        self.newbutton.setMinimumWidth(MINWIDTH / 2)
        self.newbutton.clicked.connect(self.editlist.new)
        self.box.addWidget(self.editlist)
        self.box.addWidget(self.newbutton)
        self.setLayout(self.box)

class EditListWidget(QListWidget):
    """list widget containing QLineEdit items with New and Delete buttons"""

    def __init__(self, listvals, key, item_changed, parent):
        super().__init__(parent)
        self.cast_type = type(listvals)
        self.listvals = listvals
        self.file = "file" in key
        self.item_changed = item_changed
        self.items_dict = {}
        #self.addItems(listvals)
        # self.setDragDropMode(QAbstractItemView.InternalMove)
        for ind, listval in enumerate(listvals):
            item = ListWidgetItem(listval, ind, self.delete, self.file, self.update)
            self.insertItem(self.count(), item)
            self.setItemWidget(item, item.widget)
            self.items_dict[ind] = item

        #self.resize()
        rowheight = ROWHEIGHT
        maxrows = MAXROWS
        height = len(listvals) * rowheight
        if height > rowheight * maxrows:
            height = rowheight * maxrows
        self.setFixedHeight(height+25)

    def resize(self):
        """resize list to fit items"""
        rowheight = ROWHEIGHT + 4
        maxrows = MAXROWS + 1
        height = self.count() * rowheight
        if height > rowheight * maxrows:
            height = rowheight * maxrows
        self.setFixedHeight(height+25)

    def text(self) -> str:
        """current text of combined widget"""
        listvals = []
        for i in range(self.count()):
            listvals.append(self.item(i).text())
        return hp.liststr(listvals)

    def new(self):
        """add a new blank item to bottom of list"""
        item_inds = [item.ind for item in self.items_dict.values()]
        ind = 0
        if item_inds:
            ind = max(item_inds) + 1
        item = ListWidgetItem("", ind, self.delete, self.file, self.update)
        self.insertItem(self.count(), item)
        self.setItemWidget(item, item.widget)
        # item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.items_dict[ind] = item
        self.resize()
        self.update()

    def delete(self, ind):
        """delete list item with given index"""
        for row in range(self.count()):
            item = self.item(row)
            if not hasattr(item, "ind"):
                continue
            if item.ind == ind:
                self.takeItem(row)
                del item
                self.items_dict.pop(ind)
                self.resize()
                self.update()
                return

    def update(self):
        """list update callback function"""
        # TODO: infinite recursion happening here
        new_value = [it for it in self.items_dict.values()]
        values_list = []
        for item in new_value:
            if item.vtype == type(int()):
                values_list.append(int(item.lineedit.text()))
            if item.vtype == type(float()):
                values_list.append(float(item.lineedit.text()))
            else:
                values_list.append(item.lineedit.text())
        self.item_changed(values_list)

class FileEditWidget(QWidget):
    """file string editor with file select button"""

    def __init__(self, text, update_call, parent):
        super().__init__(parent)
        self.box = wd.create_box(self)
        self.lineedit = QLineEdit(str(text), self)
        self.update_call = update_call
        self.lineedit.editingFinished.connect(self.update_call)
        self.filebutton = QPushButton(" Select ")
        self.filebutton.clicked.connect(self.select_file)
        self.box.addWidget(self.filebutton)
        self.box.addWidget(self.lineedit)
        self.setLayout(self.box)

    def select_file(self):
        """select a file and fill in line edit with selection"""
        filepath, _filter = QFileDialog.getOpenFileName(self, "Select File", "", "", "")
        if filepath:
            self.lineedit.setText(filepath)

class ListWidgetItem(QListWidgetItem):
    """ListWidget item which contains a line editor and a delete button"""

    def __init__(self, text, ind, delete_call, file, update_call):
        super().__init__()
        self.widget = QWidget(self.listWidget())
        self.ind = ind
        self.box = wd.create_box(self.widget)
        self.lineedit = QLineEdit(str(text), self.widget)
        # self.lineedit.setFixedHeight(30)
        self.vtype = type(text)
        if isinstance(text, int | float):
            validator = QDoubleValidator(-1000000000.0, 1000000000.0, 10)
            self.lineedit.setValidator(validator)
        self.update_call = update_call
        self.lineedit.editingFinished.connect(self.update_call)
        self.deletebutton = QPushButton("X")
        self.delete_call = delete_call
        self.deletebutton.clicked.connect(self.delete)
        if file:
            self.filebutton = QPushButton(" Select ")
            self.filebutton.clicked.connect(self.select_file)
            self.box.addWidget(self.filebutton)
        self.box.addWidget(self.lineedit)
        self.box.addWidget(self.deletebutton)
        #self.widget.setMinimumHeight(MINWIDTH / 2)
        #self.widget.setMinimumWidth(ROWHEIGHT)
        self.widget.setLayout(self.box)
        # self.sizeHint().height() + 4
        #self.setSizeHint(QSize(0, ROWHEIGHT + 2))
        # self.setFlags(self.flags() | Qt.ItemIsEditable)

    def delete(self):
        """delete this list item"""
        self.delete_call(self.ind)

    def select_file(self):
        """select a file and fill in line edit with selection"""
        filepath, _filter = QFileDialog.getOpenFileName(
            self.widget, "Select File", "", "", ""
        )
        if filepath:
            self.lineedit.setText(filepath)
            self.update_call()

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

class EditView(QTableView):
    """table view with custom context menu"""

    def __init__(self, model):
        super().__init__()
        self.setItemDelegate(TypeBasedDelegate(self))
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.table_context)
        self.horizontalHeader().setContextMenuPolicy(Qt.CustomContextMenu)
        self.horizontalHeader().customContextMenuRequested.connect(self.header_context)
        self.keyPressEvent = self.key_press  # pylint: disable=C0103
        self.doubleClicked.connect(self.double_click)
        proxy = ProxyModel(self)
        proxy.setSourceModel(model)
        self.setModel(proxy)
        model.views.append(self)
        model_obj = self.model().sourceModel().object
        self.trace = model_obj.trace if hasattr(model_obj, 'trace') else None
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        #self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #self.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.horizontalHeader().setStretchLastSection(True)
        #self.open_editors(True)
        self.resizeRowsToContents()

    def open_editors(self, open:bool):
        """open all persistent editors only for editable cells, and only if not already open"""
        try:
            for row in range(self.model().sourceModel().rowCount(QModelIndex())):
                for col in range(self.model().sourceModel().columnCount(QModelIndex())):
                    index = self.model().sourceModel().index(row, col)
                    proxy_index = self.model().mapFromSource(index)
                    #flags = self.model().sourceModel().flags(index)
                    if open and not self.isPersistentEditorOpen(proxy_index):
                        self.openPersistentEditor(proxy_index)
                    elif (not open) and self.isPersistentEditorOpen(proxy_index):
                        self.closePersistentEditor(proxy_index)
            if open:
                self.horizontalHeader().setStretchLastSection(True)
                self.resizeRowsToContents()
            return True
        except RuntimeError as _e:
            return False

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

    def double_click(self, index):
        """check box when double-clicked"""
        src_index = self.model().mapToSource(index)
        value = self.model().sourceModel().get_value(src_index)
        if isinstance(value, bool):
            if value:
                self.model().sourceModel().set_value(src_index, False)
            else:
                self.model().sourceModel().set_value(src_index, True)

    def key_press(self, event):
        """copy and paste upon keypress"""
        if event.key() == 67:
            self.copy()
        elif event.key() == 86:
            self.paste()
        else:
            super().keyPressEvent(event)

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



