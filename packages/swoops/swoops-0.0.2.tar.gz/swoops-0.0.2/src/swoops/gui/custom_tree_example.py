
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




class TreeModel(QAbstractItemModel):
    def __init__(self, integrator):
        super().__init__()
        self.session = self.integrator.session
        self.trace = st.Trace([])
        self.views = []
        self.columns = ["Name", "#", "ID", "Type"]
        self.setHorizontalHeaderLabels(self.columns)
        #self._rootItem = TreeItem(root_data)
        # Populate your tree structure here, e.g., by adding children to _rootItem

    def rowCount(self, parent = QModelIndex()) -> int:
        if not parent.isValid():
            parentItem = self._rootItem
        else:
            parentItem = parent.internalPointer()
        return parentItem.childCount()

    def columnCount(self, parent = QModelIndex()) -> int:
        return len(self.columns)

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if index.isValid():
            item = index.internalPointer()
            parent = index.parent()
            if parent == QModelIndex():
                trace = self.trace.child(st.Project, index.row())
                project = trace.get_obj(self.session)
                return project.name
            else:
                print(parent)
        return None

    def setData(self, index: QModelIndex, value: Any, role= Qt.EditRole) -> bool:
        if not index.isValid():
            return False
        if role == Qt.EditRole:
            item = index.internalPointer()
            if item.setData(index.column(), value):
                self.dataChanged.emit(index, index, [role])
                return True
        return False

    def index(self, row: int, column: int, parent: QModelIndex = QModelIndex()) -> QModelIndex:
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

    def parent(self, index: QModelIndex) -> QModelIndex:
        if not index.isValid():
            return QModelIndex()
        childItem = index.internalPointer()
        parentItem = childItem.parent()
        if parentItem == self._rootItem:
            return QModelIndex()
        return self.createIndex(parentItem.row(), 0, parentItem)

    def flags(self, index: QModelIndex) -> Qt.ItemFlags:
        if not index.isValid():
            return Qt.NoItemFlags
        return super().flags(index) | Qt.ItemIsEditable

    def get_value(self, index: QModelIndex):
        trace = st.Trace([])
        value = trace.get_obj(self.session)
        return value

    def update(self, trace):
        self.beginResetModel()
        index = self.get_index(trace)
        if index is not None:
            print(f"PROJECT TREE UPDATE INDEX: {index}")
            self.dataChanged.emit(index, index)
        self.endResetModel()
        for view in self.views:
            view.open_editors(True)


class ProjectView(QFrame):
    """project tree viewer"""

    def __init__(self, model):
        super().__init__()
        self.box = create_box(self, vertical=True)
        self.top = WidgetLayout(self)
        self.model = model
        self.view = QTreeView()
        self.view.setSelectionMode(self.view.selectionMode().ExtendedSelection)
        self.view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.view.customContextMenuRequested.connect(self.context_menu)
        self.view.itemDelegate().closeEditor.connect(self.close_editor)
        self.view.doubleClicked.connect(self.double_click_edit)
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
        if not item.new and not item.static:
            trace = get_trace(item) + self.model.trace
            self.model.integrator.open_edit(trace)


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
