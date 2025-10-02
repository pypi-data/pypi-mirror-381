from copy import deepcopy

from PySide6.QtGui import (  # pylint: disable=E0611,E0401,C0413
    QUndoCommand,
)

try:
    from swoops import constants as CONS
    from swoops.structures import Trace
except ImportError:
    from .. import constants as CONS  # type: ignore # pylint: disable=E0611,E0401,C0413
    from ..structures import Trace


class NewObj(QUndoCommand):
    """create a new project value"""

    def __init__(self, integrator, trace:Trace):
        super().__init__()
        self.integrator = integrator
        self.trace = trace
        self.obj = None

    def redo(self):
        """create new empty object"""
        if self.obj is None:
            self.integrator.log(f"NewObj Redo: {str(self.trace.head)}")
            self.obj = self.integrator.new_obj(self.trace)
        else:
            self.integrator.log(f"NewObj Redo: {str(self.obj._trace.head)}")
            self.integrator.add_obj(self.obj)
        #self.obj = deepcopy(obj)

    def undo(self):
        """delete new object"""
        self.integrator.log(f"NewObj Undo: {self.obj._trace.head}")
        self.obj = self.integrator.delete_obj(self.obj._trace)


class DelObj(QUndoCommand):
    """delete a project value/object"""

    def __init__(self, integrator, trace:Trace):
        super().__init__()
        self.integrator = integrator
        self.trace = trace
        self.obj = None

    def redo(self):
        """delete object"""
        self.integrator.log(f"DelObj Redo: {self.trace.head}")
        self.obj = self.integrator.delete_obj(self.trace)

    def undo(self):
        """undo object delete"""
        self.integrator.log(f"DelObj Undo: {self.trace.head}")
        self.integrator.add_obj(self.obj)


class EditObj(QUndoCommand):
    """edit a project value"""

    def __init__(self, integrator, trace:Trace, value):
        super().__init__()
        self.integrator = integrator
        self.trace = trace
        self.new_value = value
        self.old_value = None

    def redo(self):
        """edit object"""
        self.old_value = self.integrator.edit_obj(self.trace, self.new_value)
        self.integrator.log(f"EditObj Redo: {self.trace.head} | {self.old_value} -> {self.new_value}")
        # TODO: why save this old value? also should i convert types here?

    def undo(self):
        """undo object edit"""
        self.integrator.log(f"EditObj Undo: {self.trace.head} | {self.new_value} -> {self.old_value}")
        self.integrator.edit_obj(self.trace, self.old_value)


class ViewToggle(QUndoCommand):
    """toggle a dock widget as visible or not from View Menu"""

    def __init__(self, integrator, widget_type, widget_id, check_signal):
        super().__init__()
        self.integrator = integrator
        self.widget_type = widget_type
        self.widget_id = widget_id
        self.ind = self.integrator.stack.currentIndex()
        # TODO: make it so I get all docks of the same type?
        self.dock = self.integrator.stack.containers[self.ind].docks[widget_id]
        self.checkbox = self.integrator.viewmenu.widgets[self.widget_type]
        self.checked = self.checkbox.isChecked()
        self.check_signal = check_signal

    def get_dock_vis(self):
        """check visibilty of all docks of same type in current stack"""
        widgets = list(self.integrator.widgets.values())
        current_widgets = get_by_attr(widgets, "stack_index", self.ind)
        dock_vis = []
        for widget in current_widgets:
            wid = getattr(widget, CONS.ID)
            dock = self.integrator.stack.containers[self.ind].docks[wid]
            dock_vis.append(dock.isVisible())
        return dock_vis

    def toggle_dock(self):
        """toggle dock widget visible or not when checkbox is clicked"""
        # Change visiblity when checkbox and visibility dont match
        dock_vis = self.get_dock_vis()
        if all(dock_vis) and not self.checked:
            self.dock.setVisible(False)
        elif not all(dock_vis) and self.checked:
            self.dock.setVisible(True)

    def toggle_checked(self):
        """toggle view menu checkbox if a dock widget is closed"""
        # Change View Menu checkbox when visibility disagrees after closing
        dock_vis = self.get_dock_vis()
        if not all(dock_vis) and self.checked:
            self.checkbox.setChecked(False)
        elif all(dock_vis) and not self.checked:
            self.checkbox.setChecked(True)

    def redo(self):
        """sync dock widget and view menu changes"""
        # Check Signal is None when Dock Widget is closed
        if self.check_signal is None:
            self.toggle_checked()
        else:
            self.toggle_dock()
        self.checked = False if self.checked else True
        self.check_signal = self.checked

    def undo(self):
        """undo dock widget and view menu changes"""
        printstr = f"{self.dock.isVisible()} {self.checked} {self.check_signal}"
        print(f"    viewtoggle: ({self.ind}) {self.widget_type} {printstr}")
        self.toggle_dock()
        # TODO: is there a bug here?
        self.toggle_checked()
        self.checked = False if self.checked else True


class NewWidget(QUndoCommand):
    """create new widget"""

    def __init__(self, integrator, swidget):
        super().__init__()
        self.integrator = integrator
        self.swidget_empty = swidget
        self.swidget_full = None

    def redo(self):
        """create new widget"""
        self.integrator.log(f"{self.__class__.__name__} Redo: {self.swidget_empty}")
        self.swidget_full = self.integrator.new_widget(self.swidget_empty)

    def undo(self):
        """delete widget"""
        self.integrator.log(f"{self.__class__.__name__} Undo: {self.swidget_full}")
        self.swidget_empty = self.integrator.del_widget(self.swidget_full._id)


class DelWidget(QUndoCommand):
    """delete a widget"""

    def __init__(self, integrator, widget_id:int):
        super().__init__()
        self.integrator = integrator
        self.widget_id = widget_id
        self.swidget_empty = None
        self.swidget_full = None

    def redo(self):
        """delete widget"""
        self.integrator.log(f"{self.__class__.__name__} Redo: {self.swidget_full}")
        self.swidget_empty = self.integrator.del_widget(self.widget_id)

    def undo(self):
        """create new widget"""
        self.integrator.log(f"{self.__class__.__name__} Undo: {self.swidget_empty}")
        self.swidget_full = self.integrator.new_widget(self.swidget_empty)
        self.widget_id = self.swidget_full._id


class EditWidget(QUndoCommand):
    """edit a widget to change a property. For changing tab, dock position, or current object"""

    def __init__(self, integrator, widget_id:int, attr_name:str, attr_value, old_value):
        super().__init__()
        self.integrator = integrator
        self.widget_id = widget_id
        self.attr_name = attr_name
        self.attr_value = attr_value
        self.old_value = old_value

    def redo(self):
        """activate object"""
        self.integrator.log(f"{self.__class__.__name__} Redo: {self.attr_name} = {self.attr_value}")
        if self.old_value is None:
            self.old_value = self.integrator.edit_widget(self.widget_id, self.attr_name, self.attr_value)

    def undo(self):
        """undo object activate"""
        self.integrator.log(f"{self.__class__.__name__} Undo: {self.attr_name} = {self.old_value}")
        self.integrator.edit_widget(self.widget_id, self.attr_name, self.old_value)
        self.old_value = None

class NewTab(QUndoCommand):
    """create a new tab"""

    def __init__(self, integrator):
        super().__init__()
        self.integrator = integrator
        self.tab_index = None

    def redo(self):
        """create new tab"""
        self.tab_index = self.integrator.new_tab()

    def undo(self):
        """delete tab"""
        self.integrator.del_tab(self.tab_index)

class DelTab(QUndoCommand):
    """delete an existing tab"""

    def __init__(self, integrator, tab_index:int):
        super().__init__()
        self.integrator = integrator
        self.tab_index = tab_index

    def redo(self):
        """delete tab"""
        self.integrator.del_tab(self.tab_index)

    def undo(self):
        """create new tab"""
        self.tab_index = self.integrator.new_tab()

class EditTab(QUndoCommand):
    """edit an existing tab, just for renaming?"""

    def __init__(self, integrator, tab_index:int, attr_name:str, attr_value):
        super().__init__()
        self.integrator = integrator
        self.tab_index = tab_index
        self.attr_name = attr_name
        self.attr_value = attr_value
        self.old_value = None

    def redo(self):
        """delete tab"""
        self.old_value = self.integrator.edit_tab(self.tab_index, self.attr_name, self.attr_value)

    def undo(self):
        """create new tab"""
        self.integrator.edit_tab(self.tab_index, self.attr_name, self.old_value)
