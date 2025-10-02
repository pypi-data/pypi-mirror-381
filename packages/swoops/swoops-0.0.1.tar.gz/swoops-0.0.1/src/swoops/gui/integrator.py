"""
Written by Jason Krist
06/02/2025

Ideas:
    - umodel contains backend UndoCommand updates
    - integrator contains GUI object creation/updates
    - umodel is in integrator which is passed to each GUI model for callbacks
    - update commands sends "new/edit/delete" 
    - models are created when an object is made current
    - first object in each GUI widget is made current by default
    - during update, check if trace from update overlaps with all or current models
    - if able to just do current models, then update entire model when made current

"""


from copy import deepcopy
from functools import partial

from PySide6.QtGui import (  # pylint: disable=E0611,E0401,C0413
    QUndoStack,
)

try:
    import swoops.constants as CONS  # type: ignore # pylint: disable=E0611,E0401,C0413
    import swoops.gui.helper as hp
    from swoops.structures import Trace, Session, Empty
    from swoops.gui import toolbar_calls as tbc  # type: ignore # pylint: disable=E0611,E0401,C0413
    from swoops.gui.undo_commands import EditObj
except ImportError:
    from .. import constants as CONS
    from . import helper as hp
    from ..structures import Trace, Session, Empty
    from . import toolbar_calls as tbc  # type: ignore # pylint: disable=E0611,E0401,C0413
    from .undo_commands import EditObj


class Integrator:
    """Class to integrate changes to the session and models."""
    def __init__(self, app, session = None):
        self.app = app
        self.session = session if session is not None else Session()
        #self.umodel = UModel(self)
        self.undostack = QUndoStack()
        self._log = []
        self.models = {} # Model Type, Model
        self.swidgets = {} # SWidget ID, SWidget
        # Add Toolbar Callbacks to Self
        for callname, callfxn in tbc.__dict__.items():
            if not callable(callfxn):
                continue
            callback = partial(callfxn, self)
            setattr(self, callname, callback)
        #self.stack = Stack()

    def exec(self, command, args:tuple): # 
        """execute an undoable command"""
        if command is EditObj:
            trace = args[0]
            new_value = args[1]
            obj = trace.get_obj(self.session)
            old_value = getattr(obj, trace.attr_obj)
            if type(new_value)!=type(old_value) and (not isinstance(old_value, Empty)):
                errstr = f"Cannot change type of {trace.attr_obj} from {type(old_value)} to {type(new_value)}"
                raise TypeError(errstr)
            #print(f"new_value = {new_value}, old_value = {old_value}")
            if new_value == old_value:
                return
        command_obj = command(self, *args)
        self.undostack.push(command_obj)

    def log(self, message:str):
        """log a message"""
        self._log.append(message)
        print(message)

    def new_obj(self, trace:Trace):
        """create a new object in the session"""
        parent = trace.get_obj(self.session)
        new_obj = parent._new(trace.attr_obj)
        return new_obj

    def delete_obj(self, trace:Trace):
        """delete an object from the session"""
        parent = trace.parent(self.session)
        deleted_obj = deepcopy(trace.get_obj(self.session))
        parent._delete(trace.obj_class, trace.obj_id)
        return deleted_obj

    def edit_obj(self, trace:Trace, value):
        """edit an object in the session"""
        obj = trace.get_obj(self.session)
        old_value = deepcopy(getattr(obj, trace.attr_obj))
        setattr(obj, trace.attr_obj, value)
        for _modeltype, model in self.models.items():
            model.update(trace)
        return old_value
    
    def add_obj(self, obj):
        """add an object to a list in the session"""
        parent = obj._trace.parent(self.session)
        parent._add(obj)

    def new_widget(self, swidget):
        # create widget, pack widget, add to integrator or app structure
        _id = hp.next_id(self.swidgets)
        swidget.create(_id)
        swidget.pack()
        self.swidgets[_id] = swidget
        return swidget

    def del_widget(self, widget_id:int):
        # unpack widget, remove widget from integrator, maybe delete (optional)
        swidget = self.swidgets.pop(widget_id)
        swidget.unpack()
        swidget.delete()
        return swidget

    def edit_widget(self, widget_id:int, attr_name:str, attr_value):
        # self.widget_id, self.attr_name, self.attr_value
        swidget = self.swidgets[widget_id]
        old_value = getattr(swidget, attr_name)
        setattr(swidget, attr_name, attr_value)
        return old_value

    def placeholder(self):
        print("Placeholder Callback")

    def print_log(self):
        print("\n")
        for line in self._log:
            print(line)

    def new_model(self):
        pass

    def del_model(self):
        pass
