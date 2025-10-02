
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
    QAbstractItemModel,
)

from PySide6.QtWidgets import (  # pylint: disable=E0611,E0401,C0413
    QFrame,
    QTreeView,
    QPushButton,
    QMenu,
    QMessageBox,
    QInputDialog,
    QInputDialog,
    QMenu,
    QMessageBox,
)


from PySide6.QtGui import (  # pylint: disable=E0611,E0401,C0413
    QIcon,
    QColor,
)

try:
    from widgets import create_box, WidgetLayout
    import swoops.constants as CONS  # type: ignore # pylint: disable=E0611,E0401,C0413
    import helper as hp
    from swoops import structures as st
    from swoops.gui.undo_commands import NewObj, DelObj, EditObj
except ImportError:
    from swoops.gui.widgets import create_box, WidgetLayout
    from .. import constants as CONS
    from . import helper as hp
    from .. import structures as st
    from .undo_commands import NewObj, DelObj, EditObj





# --- TreeItem class for recursive tree structure ---
class TreeItem:
    def __init__(self, obj, parent=None):
        self.object = obj  # Should be a BaseClass object or a string
        self.trace = obj._trace if hasattr(obj, "_trace") else None
        self.parentItem = parent
        self.childItems = []

    def appendChild(self, item):
        self.childItems.append(item)

    def child(self, row):
        if 0 <= row < len(self.childItems):
            return self.childItems[row]
        return None

    def childCount(self):
        return len(self.childItems)

    def columnCount(self):
        return 4  # Name, #, ID, Type

    def dataAt(self, column):
        # Map columns to attributes
        if self.trace is None:
            if column == 0:
                return hp.title(str(self.object))
            if column == 1:
                return self.childCount()
            if column == 2:
                return ""
            if column == 3:
                return ""
        else:
            if column == 0:
                return getattr(self.object, "name")
            if column == 1:
                return ""
            if column == 2:
                return getattr(self.object, CONS.ID)
            if column == 3:
                return getattr(self.object, '_classname')
        return ""

    def parent(self):
        return self.parentItem

    def row(self):
        if self.parentItem:
            return self.parentItem.childItems.index(self)
        return 0


class TreeModel(QAbstractItemModel):
    def __init__(self, integrator):
        super().__init__()
        self.integrator = integrator
        self.session = self.integrator.session
        self.columns = ["Name", "#", "ID", "Type"]
        self.views = []
        self._rootItem = self.build_tree()

    def build_tree(self):
        # Build the tree recursively from session > projects > workflows > inputs
        root = TreeItem(self.session)
        for proj in self.session.projects.values():
            proj_item = TreeItem(proj, root)
            root.appendChild(proj_item)
            self.build_nested(proj_item, proj)
        return root

    def build_nested(self, parent_item, parent_obj):
        if hasattr(parent_obj, "_trace"):
            for attr_name, attr_value in parent_obj.__dict__.items():
                if not isinstance(attr_value, dict):
                    continue
                child_dict_item = TreeItem(attr_name, parent_item)
                parent_item.appendChild(child_dict_item)
                for child_obj in attr_value.values():
                    child_item = TreeItem(child_obj, child_dict_item)
                    child_dict_item.appendChild(child_item)
                    self.build_nested(child_item, child_obj)

    def rowCount(self, parent=QModelIndex()):
        if not parent.isValid():
            return self._rootItem.childCount()
        parentItem = parent.internalPointer()
        if parentItem:
            return parentItem.childCount()
        return 0

    def columnCount(self, parent=QModelIndex()):
        return len(self.columns)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        item = index.internalPointer()
        # Always show gear icon in first column
        if role == Qt.DecorationRole and index.column() == 0:
            return QIcon(r"C:\Users\jkris\OneDrive\2022_onward\2025\python\swoops\src\swoops\gui\icons\gear.svg")
        if role == Qt.BackgroundRole:
            if item.trace is None:
                rgb = (240, 240, 200)  # light yellow
                if item.object.startswith("t"):
                    rgb = (101, 247, 233)  # turquoise
                elif item.object.startswith("p"):
                    rgb = (255, 192, 203)  # pink
                elif item.object.startswith("w"):
                    rgb = (194, 154, 106)  # walnut
                elif item.object.startswith("i"):
                    rgb = (172, 146, 247)  # Indigo
                elif item.object.startswith("o"):
                    rgb = (245, 169, 93)  # Orange
                elif item.object.startswith("s"):
                    rgb = (255, 146, 128)  # Scarlett
                elif item.object.startswith("g"):
                    rgb = (125, 250, 125)  # green
                elif item.object.startswith("m"):
                    rgb = (171, 133, 133)  # maroon
                elif item.object.startswith("d"):
                    rgb = (255, 255, 143)  # daffodil
                if self.integrator.app.dark:
                    rgb = tuple(int(num*0.4) for num in rgb)
            else:
                if item.row() % 2 == 0:
                    rgb = (255, 255, 255)
                    if self.integrator.app.dark:
                        rgb = (40, 40, 40)
                else:
                    rgb = (240, 240, 240)
                    if self.integrator.app.dark:
                        rgb = (70, 70, 70)
            return QColor(*rgb)
        if role == Qt.DisplayRole:
            return item.dataAt(index.column())
        return None

    def setData(self, index, value, role=Qt.EditRole):
        if not index.isValid():
            return False
        item = index.internalPointer()
        if role == Qt.EditRole and index.column() == 0:
            if hasattr(item.object, 'name'):
                name_trace = item.object._trace.attr("name")
                self.integrator.exec(EditObj, args=(name_trace, value))
                #setattr(item.object, 'name', value)
                #self.dataChanged.emit(index, index, [role])
                return True
        return False

    def index(self, row, column, parent=QModelIndex()):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()
        if not parent.isValid():
            parentItem = self._rootItem
        else:
            parentItem = parent.internalPointer()
        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        return QModelIndex()

    def parent(self, index):
        if not index.isValid():
            return QModelIndex()
        childItem = index.internalPointer()
        #if not childItem:
        #    return QModelIndex()
        parentItem = childItem.parent()
        if parentItem == self._rootItem or parentItem is None:
            return QModelIndex()
        return self.createIndex(parentItem.row(), 0, parentItem)

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.columns[section]
        return None

    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags
        # Only name column is editable
        item = index.internalPointer()
        if index.column() == 0 and (hasattr(item.object, "_trace")):
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled

    #def itemFromIndex(self, index):
        
    def get_index(self, trace):
        item = self.nested_search(self._rootItem, trace)
        if item is not None:
            #print(f"item row found: {item.row()}, {item.parent().trace}")
            #if item.parent() is not None:
            return self.createIndex(item.row(), 0, item.parent())
            #return self.createIndex(item.row(), 0)
        return None

    def nested_search(self, item, search_trace):
        # Recursively search for a child with matching trace.list
        if (item.trace is not None):
            if not item.trace.contains(search_trace):
                return None
            #print(f"    {item.trace.list} == {search_trace.list} >> {item.trace.list == search_trace.list}")
            #print(f"        {item.trace.contains(search_trace)} , {search_trace.contains(item.trace)}")
        if (item.trace is not None) and (item.trace.list == search_trace.list):
            return item
        for child_item in item.childItems:
            result = self.nested_search(child_item, search_trace)
            if result is not None:
                return result
        return None

    def update(self, trace):
        index = self.get_index(trace)
        if index is not None:
            #print(f"index: {index}")
            row_start = self.index(index.row(), 0, parent=index.parent())
            row_end = self.index(index.row(), self.columnCount()-1, parent=index.parent())
            self.dataChanged.emit(row_start, row_end)
            #self.beginResetModel()
            #self._rootItem = self.build_tree()
            #self.endResetModel()


class TreeView(QFrame):
    """project tree viewer"""

    def __init__(self, integrator):
        super().__init__()
        self.integrator = integrator
        self.box = create_box(self, vertical=True)
        self.top = WidgetLayout(self)
        self.model = self.integrator.models[TreeModel]
        self.view = QTreeView()
        self.view.setSelectionMode(self.view.selectionMode().ExtendedSelection)
        self.view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.view.customContextMenuRequested.connect(self.context_menu)
        #self.view.itemDelegate().closeEditor.connect(self.close_editor)
        #self.view.doubleClicked.connect(self.double_click_edit)
        self.update_view()

    def update_view(self):
        """update project tree viewer from item model"""
        # Add project label, collapse all, and expand all buttons
        self.top = WidgetLayout(self)
        # label = QLabel(self.model.proj.name)
        expand = QPushButton("Expand All")
        expand.clicked.connect(self.view.expandAll)
        collapse = QPushButton("Collapse All")
        collapse.clicked.connect(self.view.collapseAll)
        # self.top.box.addWidget(label)
        self.top.box.addWidget(expand)
        self.top.box.addWidget(collapse)
        self.box.addWidget(self.top)
        # Project Model and Tree View
        self.view.setModel(self.model)
        self.view.expandAll()
        self.resize_cols()
        self.view.collapseAll()
        self.box.addWidget(self.view)

    def resize_cols(self):
        """resize all columns to fit contents"""
        for i in range(self.model.columnCount()):
            self.view.resizeColumnToContents(i)

    def close_editor(self, editor):
        """close rename editor"""
        index = self.view.indexAt(editor.pos())
        if not index.isValid():
            return
        item = self.model.itemFromIndex(index)
        item.setEditable(False)

    def context_menu(self, pos):
        """Project Tree Context Menus"""
        index = self.view.indexAt(pos)
        if not index.isValid():
            return
        item = self.model.itemFromIndex(index)
        trace = get_trace(item) + self.model.trace
        menu = QMenu()
        if item.new:
            new_action()
        elif item.editable:
            # TODO: add export button (file dialog)
            rename_action = menu.addAction("&Rename")
            edit_action = menu.addAction("&Edit")
            delete_action = menu.addAction("&Delete")
            #if item.workflow:
            #    active_action = menu.addAction("&Set Active")
            # active_action = menu.addAction("&Set Active") # DO I NEED THIS?
            action = menu.exec_(self.view.viewport().mapToGlobal(pos))
            if action == rename_action:
                item.setEditable(True)
                self.view.edit(index)
            elif action == edit_action:
                self.model.integrator.open_edit(trace)
            elif action == delete_action:
                q_str = f'Are you sure you want to delete "{item.text()}"?'
                opts = QMessageBox.Yes | QMessageBox.No
                ans = QMessageBox.question(self, "Confirm Delete", q_str, opts)
                if ans == QMessageBox.Yes:
                    change = {"old": item.text(), "new": None}
                    print(f"delete: {trace}, {change}")
                    self.model.exec_call(trace, change)
            #elif item.workflow:
            #    if action == active_action:
            #        self.model.exec_call(trace, {"activate": True})

    def double_click_edit(self, index):
        """open edit window on double click"""
        item = self.model.itemFromIndex(index)
        print(f"double click: {item.text()}")
        #if not item.new and not item.static:
        #    #trace = get_trace(item) + self.model.trace
        #    #self.model.integrator.open_edit(trace)


def get_trace(item) -> list[str]:
    """get a list of parent item types and IDs, closest to furthest up"""
    if item.orig:
        trace = [item.orig]
    else:
        item_id = item.parent().child(item.index().row(), 2).text()
        trace = [item_id]
    while item.parent():
        if item.parent().orig:
            parent_text = item.parent().orig
        else:
            index = item.parent().index()
            id_item = item.parent().parent().child(index.row(), 2)
            parent_text = id_item.text()
        trace.append(parent_text)
        item = item.parent()
    return trace


def new_action(view, menu, item, pos):
    # TODO: add import button (file dialog)
    new_action = menu.addAction("&New (1)")
    multi_action = menu.addAction("New (Multi)")
    action = menu.exec_(view.view.viewport().mapToGlobal(pos))
    if action == new_action:
        # self.model.exec_call(trace, {"old": None, "new": None})
        view.model.integrator.exec(NewObj, trace)
    elif action == multi_action:
        windowname = "New (Multi) Dialog"
        label = f"Create X New {item.text()}: "
        integer, ok = QInputDialog.getInt(view, windowname, label, 1, 0, 100)
        if ok:
            for _i in range(integer):
                trace = None # TODO: get trace here
                view.model.exec_call(trace, {"old": None, "new": None})
                view.integrator.exec(NewObj, trace)
