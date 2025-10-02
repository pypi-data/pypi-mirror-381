"""
Written by Jason Krist
05/01/2024

TODO:
    - ADD HIGHLIGHT OR INDICATOR TO ACTIVE PROJECT ON EACH TAB (in view?)
    - for data_set dictionary, add import, export, and copy runs
    
    - ADD TO CONTEXT: Copy, Paste, Export
    - double-click to edit as default behavior (AND set active)
    - SET ACTIVE WORKFLOW
        - any other set active options?
    - allow multi-selection deletion
    - delete confirm popup should be optional?
    - different colors for lists vs. objects (and each object type)
    - even more dull when 0 of something
    - Add icons next to projects, workflows, executions, inputs, outputs, etc.
    - add an "Active" column which is checkable for inputs, outputs
    - inputs, outputs, etc. are copy and pastable
"""

from pandas import DataFrame

from PySide6.QtCore import (  # pylint: disable=E0611,E0401,C0413
    Qt,
    QModelIndex,
)

from PySide6.QtWidgets import (  # pylint: disable=E0611,E0401,C0413
    QFrame,
    QTreeView,
    # QLabel,
    QPushButton,
    QMenu,
    QMessageBox,
    QInputDialog,
)

from PySide6.QtGui import (  # pylint: disable=E0611,E0401,C0413
    QStandardItemModel,
    QStandardItem,
    QIcon,
)

try:
    from widgets import create_box, WidgetLayout
    import swoops.constants as CONS  # type: ignore # pylint: disable=E0611,E0401,C0413
    from swoops.structures import Trace
    from swoops.gui.helper import title, plural
    from swoops.gui.undo_commands import NewObj, DelObj, EditObj
except ImportError:
    from .widgets import create_box, WidgetLayout
    from .. import constants as CONS
    from ..structures import Trace
    from .helper import title, plural
    from .undo_commands import NewObj, DelObj, EditObj


class ProjectModel(QStandardItemModel):
    """Tree Model of Project Structure"""
    # TODO: implement custom tree example instead so setData and data fxns are used
    # TODO: dataChanged should give indices above and below

    def __init__(self, integrator):
        super().__init__()
        self.integrator = integrator
        self.session = self.integrator.session
        self.trace = Trace([])
        self.views = []
        self.create(self.session.projects)
        self.itemChanged.connect(self.item_changed)

    def create(self, object_dict):
        """create item model from project"""
        for _key, value in object_dict.items():
            #if isinstance(value, dict):
            append_row(self, value.name, value)
        self.setHorizontalHeaderLabels(["Name", "#", "ID", "Type"])

    # UNUSED BELOW
    def change_num(self, index, increment, new_num=None):
        """change number of items in parenthesis"""
        num_index = index.siblingAtColumn(1)
        num_item = self.itemFromIndex(num_index)
        current_num = 0
        if num_item.text():
            current_num = int(num_item.text().strip("(").strip(")"))
        new_number = int(current_num + increment)
        if new_num is not None:
            new_number = new_num
        new_text = f"({new_number})"
        if new_number == 0:
            new_text = ""
        num_item.setText(new_text)

    # UNUSED BELOW
    def item_changed(self, item):
        """callback when model item changes"""
        colnum = item.index().column()
        if colnum == 0:
            trace = ["name"] + get_trace(item) + self.trace
            self.integrator.exec(EditObj, trace, value = item.text())

    # UNUSED BELOW
    def find_item(self, trace, old_value):
        """find item by change and trace"""
        find_items = self.findItems(old_value, column=0, flags=Qt.MatchRecursive)
        if len(find_items) == 0:
            return None
        traces = [get_trace(item) + self.trace for item in find_items]
        items = [item for i, item in enumerate(find_items) if traces[i] == trace]
        if len(items) < 1 or len(items) > 1:
            print(f"    ERROR: find items: {find_items}, traces: {traces}")
            print(f"    ERROR: items: {items}, trace: {trace}, old_val: {old_value}")
            return None
        return items[0]

    # UNUSED BELOW
    def new(self, trace, change):
        """create a new item in the project tree"""
        parent_name = title(plural(trace[0]))
        parent_item = self.find_item(trace, parent_name)
        if parent_item is not None:
            parent_index = self.indexFromItem(parent_item)
            append_row(parent_item, change["new"].name, change["new"])
            self.change_num(parent_index, 1)

    # UNUSED BELOW
    def delete(self, trace, change):
        """delete an item from project tree"""
        if isinstance(change["old"], DataFrame):
            print(f"    delete item proj tree: {trace}")
            item = self.find_item(trace[1:], title(trace[1]))
            index = self.indexFromItem(item)
            self.change_num(index, -1)
            return
        item = self.find_item(trace, change["old"].name)
        if item is not None:
            index = self.indexFromItem(item)
            parent_index = item.parent().index()
            item.parent().removeRow(index.row())
            self.change_num(parent_index, -1)

    # UNUSED BELOW
    def edit_item(self, trace, change):
        """edit item by trace"""
        if trace[0] == "name" and not isinstance(change["old"], DataFrame):
            item = self.find_item(trace[1:], change["old"])
            if item is not None:
                item.setText(change["new"])
        elif trace[0] == "runs":  # number of runs changes
            print(f"    edit item proj tree: {trace}")
            item = self.find_item(trace, title(trace[0]))
            if item is not None:
                index = self.indexFromItem(item)
                self.change_num(index, 0, new_num=len(change["new"]))

    def update(self, trace):
        self.beginResetModel()
        index = self.get_index(trace)
        if index is not None:
            print(f"PROJECT TREE UPDATE INDEX: {index}")
            self.dataChanged.emit(index, index)
        self.endResetModel()
        for view in self.views:
            view.open_editors(True)

    def get_index(trace):
        # TODO: get index and parent?
        pass


class ProjectItem(QStandardItem):
    """item in a project tree"""

    def __init__(self, attr_name, obj, text:str, col_index:int): # , static=False, orig=""
        super().__init__(text)
        self.attr_name = attr_name
        self.object = obj
        self.trace = None
        self.new = False
        self.editable = False
        if hasattr(obj, "_trace"):
            self.trace = obj._trace
        elif isinstance(obj, dict):
            self.new = True
        self.setEditable(False)
        if (col_index == 0) and (hasattr(obj, "_trace")):
            self.setIcon(QIcon(r"C:\Users\jkris\OneDrive\2022_onward\2025\python\swoops\src\swoops\gui\icons\gear.svg"))
            self.setEditable(True)
        # TODOL finish putting right click options here based on object

def get_vals(attr_name, obj):
    if isinstance(obj, dict):
        len_num = str(len(obj)) if obj else ""
        return title(attr_name), len_num, "", ""
    elif isinstance(obj, DataFrame):  # for study runs
        return title(attr_name), str(len(obj)), "", "DataFrame"
    else:
        return attr_name,"",str(getattr(obj, CONS.ID)),obj.__class__.__name__


def append_row(parent, attr_name, attr_value):
    name, len_num, id_num, _type = get_vals(attr_name, attr_value)
    row_items = [ProjectItem(attr_name, attr_value, text, i) for i,text in enumerate([name, len_num, id_num, _type])]
    if hasattr(attr_value, "__dict__") and not isinstance(attr_value, DataFrame):
        for key, value in attr_value.__dict__.items():
            if isinstance(value, dict | DataFrame):
                if isinstance(value, dict) and len(value) > 0:
                    if not hasattr(list(value.values())[0], "name"):
                        continue
                append_row(row_items[0], key, value)
    elif isinstance(attr_value, dict):
        for value in attr_value.values():
            if not hasattr(value, "name"):
                return
            # TODO: why am I using value.name as the attr_name?
            append_row(row_items[0], value.name, value)
    parent.appendRow(row_items)
    #return item


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
