"""
Written by Jason Krist
06/02/2025
"""

import importlib.util
import sys
from typing import get_args, Optional, Type, Any, Literal
from os import path
from copy import deepcopy
from functools import partial
from pandas import DataFrame, read_csv, read_excel
#import matplotlib
from matplotlib import pyplot as plt
import numpy as np
#matplotlib.use("Qt5Agg")

try:
    import constants as CONS  # type: ignore # pylint: disable=E0611,E0401,C0413
    import gui.helper as hp  # type: ignore
    import function_parser as fp # type: ignore
except ImportError:
    from . import constants as CONS  # type: ignore # pylint: disable=E0611,E0401,C0413
    from . import function_parser as fp  # type: ignore # pylint: disable=E0611,E0401,C0413
    from .gui import helper as hp  # type: ignore # pylint: disable=E0611,E0401,C0413


class Trace:
    """trace that goes from session object to a current object (left to right)"""

    def __init__(self, trace: list):
        self.attr_obj = None
        self.obj_id = None
        self.obj_class = None
        self.pairs = []
        self.new = self.attr
        if len(trace) % 2 != 0:
            self.attr_obj = trace[-1]
            trace = trace[:-1]
        self.list = trace
        if not trace:
            return
        half_len = int(len(self.list) / 2)
        self.pairs = [self.list[i * 2 : i * 2 + 2] for i in range(half_len)]
        self.obj_id = self.pairs[-1][1]
        try:
            self.obj_class = self.pairs[-1][0]
        except ValueError:
            pass

    def _str_list(self, num=None):
        str_list = []
        list_obj = self.list
        if isinstance(num,int):
            list_obj = list_obj[-num:]
        for item in list_obj:
            if not isinstance(item, int):
                item = str(item.__name__)[0:2]
            str_list.append(str(item))
        if self.attr_obj is not None:
            if isinstance(self.attr_obj, str):
                str_list.append(self.attr_obj)
            else:
                str_list.append(str(self.attr_obj.__name__)[0:2])
        return str_list

    def __repr__(self) -> str:
        str_list = self._str_list()
        return f"Trace({str_list})"

    def __len__(self) -> int:
        return len(self.full)

    @property
    def head(self):
        str_list = self._str_list(2)
        return f"Trace_H({str_list})"

    @property
    def full(self):
        if self.attr_obj is not None:
            return self.list+[self.attr_obj]
        return self.list

    def get_obj(self, session, startind=0):
        """get current item from trace pairs"""
        trace_item = session
        for trace_class, trace_id in self.pairs[startind:]:
            attr_name = hp.attr_name(trace_class.__name__)
            attr_value = getattr(trace_item, attr_name)
            if isinstance(attr_value, dict):
                if trace_id not in attr_value:
                    return None
                trace_item = attr_value[trace_id]
            else:  # covers attributes which are dataframes
                return attr_value
        return trace_item

    # UNUSED BELOW
    def set_obj(self, trace_item, value):
        """set value of trace item"""
        if self.attr_obj is None:
            raise ValueError(
                f"Trying to set item value without an attribute name. {self}"
            )
        if isinstance(trace_item, DataFrame):
            row_id = self.list[0]
            trace_item.loc[row_id, self.attr_obj] = value
            return
        attr_value = getattr(trace_item, self.attr_obj)
        if isinstance(attr_value, dict) and hasattr(value, CONS.ID):
            attr_id = getattr(value, CONS.ID)
            attr_value[attr_id] = value
        else:
            setattr(trace_item, self.attr_obj, value)

    # UNUSED BELOW
    def get_all_objs(self, session):
        """get all trace items"""
        trace_objs = []
        trace_item = session
        for trace_class, trace_id in self.pairs:
            attr_name = hp.attr_name(trace_class.__name__)
            trace_item = getattr(trace_item, attr_name)[trace_id]
            trace_objs.append(trace_item)
        return trace_objs

    # UNUSED BELOW
    def get_objs_by_type(self, session):
        """get all items corresponding to trace type"""
        attr_names = [hp.attr_name(trace_class.__name__) for trace_class, _trace_id in self.pairs]
        trace_items = [session]
        item_traces = [[]]
        attr_ind = 0
        while attr_ind < len(attr_names) - 1:
            next_trace_items = []
            next_item_traces = []
            for ind, item_value in enumerate(trace_items):  # dictname, dictvalue
                attr_name = attr_names[attr_ind]  # i=0: projects
                dictionary = getattr(item_value, attr_name)  # dict of projects
                for subkey, subvalue in dictionary.items():
                    next_trace_items.append(subvalue)  # append each project
                    next_item_traces.append(item_traces[ind] + [attr_name, str(subkey)])
            trace_items = next_trace_items
            item_traces = next_item_traces
            attr_ind += 1
        print(trace_items)
        print(item_traces)
        return trace_items, item_traces

    # UNUSED BELOW
    def unwrap(self, num):
        """return number of objects in list starting from project id"""
        int_list = [item if item.isdigit() else item for item in self.list[:-1]]
        result = list([self.attr_obj] + int_list)[:num]
        result = result + [None] * (num - len(result))
        return result
    
    def parent(self, session):
        """return parent object"""
        if not self.pairs:
            return None
        parent_trace = Trace(self.list[:-2])
        parent = parent_trace.get_obj(session)
        return parent

    def child(self, class_obj, child_id:int):
        """create trace for child object which exists"""
        return Trace([*self.list, class_obj, child_id])

    def attr(self, attr_obj):
        """create attribute trace"""
        return Trace([*self.list, attr_obj])

    def contains(self, trace):
        """checks if the given trace is contained in this trace"""
        if (len(self) > len(trace)):
            return False
        if trace.full[0:len(self)] == self.full:
            return True
        return False

    # UNUSED BELOW
    def id(self, obj_id:int):
        """create id trace from new object trace"""
        return Trace([*self.list, obj_id])

    @property
    def is_new(self):
        """check if trace is for a new object"""
        return not isinstance(self.attr_obj, str)

    @property
    def is_edit(self):
        """check if trace is for an attribute edit"""
        return isinstance(self.attr_obj, str)

    @property
    def is_delete(self):
        """check if trace is for a delete object"""
        return self.attr_obj is None

class BaseClass:
    """base class for all objects"""

    def __init__(self, _id: int, name: str, classname: str):
        self._trace = Trace([])
        self.name = name
        setattr(self, CONS.ID, _id)
        self._classname = classname
        self._class_list = []

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({getattr(self, CONS.ID)}:"{self.name}")'

    def check_class(self, class_obj):
        """check if class object is valid for adding or deleting"""
        if class_obj not in self._class_list:
            errstr = f"Can only create, delete, or assign {self._class_list} objects from {self.__class__.__name__}, not {class_obj.__name__}"
            raise TypeError(errstr)

    def _new(self, class_obj: Any, **kwargs):
        self.check_class(class_obj)
        classname = hp.class_name(class_obj.__name__)
        dictname = hp.attr_name(classname)
        if not hasattr(self, dictname):
            errstr = f'Attribute "{dictname}" does not exist in {self.__class__.__name__}'
            raise AttributeError(errstr)
        dictobj = getattr(self, dictname)
        _id = hp.next_id(dictobj)
        newobj = class_obj(_id=_id, **kwargs)
        dictobj[_id] = newobj
        if hasattr(self, "_trace"):
            newobj._trace = self._trace.child(class_obj, _id)
        else:
            newobj._trace = Trace([]).child(class_obj, _id)
        return newobj

    def _delete(self, class_obj: Any, oid: int):
        """delete an object by id"""
        self.check_class(class_obj)
        dictname = hp.attr_name(class_obj.__name__)
        if not hasattr(self, dictname):
            errstr = f'Attribute "{dictname}" does not exist in {self.__class__.__name__} "{self.name}"'
            raise AttributeError(errstr)
        dictobj = getattr(self, dictname)
        dictobj.pop(oid, None)

    def _add(self, obj: Any):
        """add an already created object to the current object"""
        self.check_class(obj.__class__)
        dictname = hp.attr_name(obj.__class__.__name__)
        if not hasattr(self, dictname):
            errstr = f'Attribute "{dictname}" does not exist in {self.__class__.__name__} "{self.name}"'
            raise AttributeError(errstr)
        dictobj = getattr(self, dictname)
        oid = getattr(obj, CONS.ID)
        dictobj[oid] = obj
        if hasattr(self, "_trace"):
            obj._trace = self._trace.child(obj.__class__, oid)
        else:
            obj._trace = Trace([]).child(obj.__class__, oid)

class Reference(BaseClass):

    def __init__(self, obj):
        super().__init__(CONS.ID, str(obj), obj.__class__.__name__)
        self.reference_name = obj.name
        self.trace = obj._trace
        self.refclass = obj.__class__.__name__

    def get_obj(self, session):
        return self.trace.get_obj(session)

    def exists(self, session):
        return self.trace.get_obj(session) is not None

class Options:
    """list of options with a current value"""

    def __init__(self, options:list, value):
        if isinstance(options,list):
            self.options = options
        else:
            self.options = list(get_args(options))
        self.value = value

    def __repr__(self) -> str:
        return f'Options("{self.value}"/{len(self.options)})'

    def __eq__(self, other):
        if not isinstance(other, Options):
            return False
        if (self.value == other.value) and (self.options == other.options):
            return True
        return False

    def index(self) -> int:
        if not self.options:
            return None
        if not (self.value in self.options):
            #errstr = f'Value "{self.value}" ({type(self.value)}) not in options "{self.options} ({type(self.options[0])})"'
            #raise ValueError(errstr)
            return None
        return self.options.index(self.value)

class NotApplicable:
    """makes viewer blank because the attribute isnt make_applicable based on parent object type"""

    def __init__(self, obj=None, attr_name=None, default=None):
        value = default
        if obj is not None:
            if hasattr(obj, attr_name):
                value = getattr(obj, attr_name)
        self.value = value

    def __repr__(self) -> str:
        return "-"

class Empty:

    def __init__(self, _type):
        self._type = _type

    def __repr__(self):
        return f"Empty({self._type})"

def make_applicable(parent_obj, attr_name, default):
    """turn NA object back into normal version"""
    if not hasattr(parent_obj, attr_name):
        return default
    obj = getattr(parent_obj, attr_name)
    if isinstance(obj, NotApplicable):
        return obj.value
    return obj

class Input(BaseClass):
    """Input"""

    def __init__(
        self,
        _id: int = -1,
        name: str = "",
        value: Empty|float|Options=Empty(float),
        vtype: CONS.InputTypes = None,
        lb: Empty|float=Empty(float),
        ub: Empty|float=Empty(float),
        options: list=None,
        shape: tuple[int]=None,
        units: str="",
        #distribution: CONS.DistTypes = None,
    ):
        super().__init__(_id, name, self.__class__.__name__)
        self.active: bool = True
        vtype = get_args(CONS.InputTypes)[0] if vtype is None else vtype
        super().__setattr__(CONS.TYPE, Options(CONS.InputTypes, vtype))
        super().__setattr__("value", value)
        self.lower_bound  = lb
        self.upper_bound = ub
        # discrete option need to open another window
        # Increment?, Parse Arg?
        self.options = NotApplicable(self, "options", []) if options is None else options
        self.shape = (1,) if shape is None else shape
        if isinstance(self.value, list):
            self.shape = (len(self.value),)
        elif isinstance(self.value, np.ndarray):
            self.shape = self.value.shape
        self.units = units
        #self.distribution = (
        #    get_args(CONS.DistTypes)[0] if distribution is None else distribution
        #)
        self.tasks: list[int] = []

    # Type Change Function Here?
    @property
    def discrete(self) -> bool:
        """check if variable is discrete"""
        return getattr(self, CONS.TYPE).value == "Discrete"

    @property
    def continuous(self) -> bool:
        """check if variable is continuous"""
        return getattr(self, CONS.TYPE).value == "Continuous"

    def __setattr__(self, name, value):
        if isinstance(value, str) and name == CONS.TYPE:
            value = Options(CONS.InputTypes, value)
        elif (name == "value") and (isinstance(self.options, list)):
            #print(f"    changing value to include options ({self.options}): {value} ({type(value)})")
            if isinstance(value, Options):
                value = value.value
            if not isinstance(value, Empty):
                value = Options(self.options, value)
            #print(f"    changing value to include options ({self.options}): {value} ({type(value)})")
        elif name == "tasks":
            value = list([int(val) if val.isdigit() else 0 for val in value])
        elif (name == "value") and (isinstance(value, list|np.ndarray)):
            if isinstance(value, np.ndarray):
                self.shape = value.index
            else:
                self.shape = (len(value),)
        super().__setattr__(name, value)
        if name == CONS.TYPE:
            if value.value == "Continuous":
                super().__setattr__("value", Empty(float))
                self.lower_bound:float|Empty = make_applicable(self, "lower_bound", Empty(float))
                self.upper_bound:float|Empty = make_applicable(self, "upper_bound", Empty(float))
                self.options:NotApplicable = NotApplicable(self, "options", [self.value])
            elif value.value in ["Discrete", "Increment", "Sequential"]:
                super().__setattr__("value", Empty(Options))
                self.lower_bound:NotApplicable = NotApplicable(self, "lower_bound", Empty(float))
                self.upper_bound:NotApplicable = NotApplicable(self, "upper_bound", Empty(float))
                self.options:Options = make_applicable(self, "options", [self.value])
            # if value is Sequential, make options dropdown of discrete vars
        elif name == "options" and (getattr(self, CONS.TYPE).value in ["Discrete", "Increment", "Sequential"]):
            #print(f"    changing value due to options change: {value} ({type(value)})")
            if isinstance(self.value, Empty) and value:
                self.value.value = value[0]
            elif isinstance(self.value, Options) and value:
                if self.value.value not in value:
                    self.value.value = Empty(Options)
            elif not value:
                self.value.value = Empty(Options)
            self.value.options = value

class Output(BaseClass):
    """Output"""

    def __init__(self, _id: int = -1, name: str = "", value=None, vtype=None, units:str=""):
        super().__init__(_id, name, self.__class__.__name__)
        vtype = get_args(CONS.OutputTypes)[0] if vtype is None else vtype
        setattr(self, CONS.TYPE, Options(CONS.OutputTypes, vtype))
        self.value = value
        self.units = units

    def __setattr__(self, name, value):
        if name == CONS.TYPE:
            if isinstance(value, str):
                value = Options(CONS.OutputTypes, value)
        super().__setattr__(name, value)

class Constraint(BaseClass):
    """Constraint"""

    def __init__(self, name="", _id: int = -1, output: Output = None, lb=None, ub=None):
        super().__init__(_id, name, self.__class__.__name__)
        self.output: Empty | Reference = Empty(Reference) if output is None else Reference(output)
        # output options (from workflow outputs)
        self.lower_bound = lb
        self.upper_bound = ub
        self._class_list = [Output]

class Objective(BaseClass):
    """Objective"""

    def __init__(self, name="", _id: int = -1, output: Output = None):
        super().__init__(_id, name, self.__class__.__name__)
        self.output: Empty | Reference = Empty(Reference) if output is None else Reference(output)
        self._class_list = [Output]

class Dependency(BaseClass):
    """Dependency"""

    def __init__(
        self,
        _id: int = -1,
        name="",
        src_id: int = -1,
        dest_ids: Optional[list[int]] = None,
        dtype=None,
        files=None,
    ):
        super().__init__(_id, name, self.__class__.__name__)
        dtype = get_args(CONS.DependTypes)[0] if dtype is None else dtype
        setattr(self, CONS.TYPE, Options(CONS.DependTypes, dtype))
        self.source_id = src_id
        self.destination_ids = [] if dest_ids is None else dest_ids
        self.files = [] if files is None else files
        # self.parent_reference = "nodes"

    def __setattr__(self, name, value):
        if name == CONS.TYPE:
            if isinstance(value, str):
                value = Options(CONS.DependTypes, value)
        super().__setattr__(name, value)

    def connect(self, src_id: int, dest_ids: list[int]):
        """connect tasks by adding source and destination IDs"""
        self.source_id = src_id
        self.destination_ids.extend(dest_ids)
        did = getattr(self, CONS.ID)
        self.name = f"D{did}: Task {src_id} Files" or self.name

# TODO: add "parser" python function to auto-parse inputs and outputs. Default is Python Function.
class Method(BaseClass):
    """method"""

    def __init__(
        self,
        _id: int = -1,
        name: str = "",
        #ctype: Optional[str] = None,
        # pre_commands: Optional[list[str]] = None,
        file: str = "",
        function: Optional[str] = None,
        args: Optional[dict] = None,
        # post_commands: Optional[list[str]] = None,
    ):
        super().__init__(_id, name, self.__class__.__name__)
        self.file = file
        self.function = Options([""],"") if function is None else function
        self.args: dict = {} if args is None else args
        self._parsed_functions:dict[str,dict] = []

    def __setattr__(self, name, value):
        if name == "file":
            real_path = path.realpath(value)
            file_name = path.dirname(real_path)
            super().__setattr__(name, value)
            if path.exists(self.file):
                self._parsed_functions = fp.parse_functions(self.file)
                function_names = list(self._parsed_functions.keys())
                if function_names:
                    self.function = Options(function_names, function_names[0])
        elif name == "function":
            function_names = list(self._parsed_functions.keys())
            if isinstance(value, str):
                if value:
                    if value in function_names:
                        super().__setattr__(name, Options(function_names, value))
                        self.args = self._parsed_functions[value]['args']
                    else:
                        raise ValueError(f"Invalid function name: {value}")
            elif isinstance(value, Options):
                if all([opt in function_names for opt in value.options]):
                    super().__setattr__(name, value)
                    self.args = self._parsed_functions[value.value]['args']
                else:
                    raise ValueError(f"Invalid function options: {value}")
        else:
            super().__setattr__(name, value)

    def run(self, *args, **kwargs):
        from importlib.machinery import SourceFileLoader
        module = SourceFileLoader("module_name", self.file).load_module()
        fun_callable = getattr(module, self.function.value)
        result = fun_callable(*args, **kwargs)
        if not isinstance(result, tuple):
            result = (result,)
        return result

    @property
    def _module_name(self):
        """name of module upon import"""
        return f"{self.name}_{getattr(self,CONS.ID)}"

    @property
    def functions(self) -> Optional[list[str]]:
        """current function names from python module"""
        self._parsed_functions = fp.parse_functions(self.file)
        return list(self._parsed_functions.keys())

    @property
    def module(self):
        """current file as Python module"""
        if not path.exists(self.file):
            return None
        spec = importlib.util.spec_from_file_location(self._module_name, self.file)
        if spec is None:
            return None
        mod = importlib.util.module_from_spec(spec)
        sys.modules[self._module_name] = mod
        spec.loader.exec_module(mod)
        return mod

    @property
    def callable(self):
        """get callable function handle from module"""
        if not path.exists(self.file):
            return None
        if not self.function.value:
            return None
        func = getattr(self.module, self.function.value)
        # TODO: raise exception if positional args are not filled?
        #args = list(self.args.values())
        #return partial(func, *args, **self.kwargs)
        return func

class Task(BaseClass):
    """task"""

    def __init__(
        self,
        _id: int = -1,
        name: str = "",
        methods: Optional[dict[int, Method]] = None,
        inputs: Optional[dict[int, Input]] = None,
        outputs: Optional[dict[int, Output]] = None,
    ):
        super().__init__(_id, name, self.__class__.__name__)
        self.methods: dict[int, Method] = {} if methods is None else methods
        self.inputs: dict[int, Reference] = {} if inputs is None else [Reference(input) for input in inputs]
        self.outputs: dict[int, Reference] = {} if outputs is None else [Reference(output) for output in outputs]
        self._class_list = [Method, Input, Output]

    def new(self, class_obj: Type[Method], **kwargs):
        """create a new workflow or study"""
        return self._new(class_obj, **kwargs)

class Group(BaseClass):
    """Group of tasks and/or Task Groups"""

    def __init__(self, _id: int = -1, name: str = "", same_folder: bool = False, tasks: Optional[list[Task]] = None):
        super().__init__(_id, name, self.__class__.__name__)
        self.same_folder = same_folder
        self.tasks: list[Reference] = [] if tasks is None else [Reference(task) for task in tasks]

class Pool(BaseClass):
    """Pool"""

    def __init__(
        self,
        name: str = "",
        _id: int = -1,
        size: int = 1,
        series: int = 1,
        parallel: int = 1,
    ):
        super().__init__(_id, name, self.__class__.__name__)
        self.size = size
        self.series = series
        self.parallel = parallel

class Workflow(BaseClass):
    """Workflow"""

    def __init__(self, _id: int = -1, name: str = ""):
        super().__init__(_id, name, self.__class__.__name__)
        self.inputs: dict[int, Input] = {}
        self.outputs: dict[int, Output] = {}
        self.tasks: dict[int, Task] = {}
        self.methods: dict[int, Method] = {}
        self.constraints: dict[int, Constraint] = {}
        self.objectives: dict[int, Objective] = {}
        self.dependencies: dict[int, Dependency] = {}
        self.groups: dict[int, Group] = {}
        self.pools: dict[int, Pool] = {}
        self._class_list = [Input, Output, Task, Dependency, Method, Group, Pool, Constraint, Objective]  # 
        setattr(self, CONS.EDIT, True)
        # self.tree: dict[int, dict | int] = {}
        # self.parameters

    def new(self, class_obj, **kwargs):
        """create a new constraint or objective"""
        return self._new(class_obj, **kwargs)

    def delete(self, class_obj, oid: int):
        """delete an object by id"""
        self._delete(class_obj, oid)

    def assign(self, parent, child):
        """assign a child object to a parent object by reference"""
        parent.check_class(child.__class__)
        attr_name = hp.attr_name(child.__class__.__name__)
        if hasattr(parent, attr_name):
            obj = getattr(parent, attr_name)
            obj[getattr(child, CONS.ID)] = Reference(child)
        else:
            attr_name = hp.singular(attr_name)
            setattr(parent, attr_name, Reference(child))


    # UNUSED?
    def new_dependency(self, src_task: Task, dest_tasks: list[Task], **kwargs):
        """add a dependency to the workflow"""
        did = hp.next_id(self.dependencies)
        dependency = Dependency(_id=did, **kwargs)
        src_id = getattr(src_task, CONS.ID)
        dest_ids = [getattr(dest_task, CONS.ID) for dest_task in dest_tasks]
        dependency.connect(src_id, dest_ids)
        self.dependencies[did] = dependency
        return dependency

    # UNUSED below
    def find_by_id(self, classname: str, tid: int):
        """return an object searching by classname and id"""
        dictname = hp.attr_name(classname)
        dictobj = getattr(self, dictname)
        return hp.find_by_key(dictobj, tid)

    def set_editable(self, editable: bool):
        """setter for _editable property"""
        setattr(self, CONS.EDIT, editable)

class Study(BaseClass):
    """Study"""

    def __init__(
        self, _id: int = -1, name: str = "", workflow: Optional[Workflow] = None
    ):
        super().__init__(_id, name, self.__class__.__name__)
        # self.set_workflow = self.set_workflow_as
        self.workflow = workflow
        #self.optimizer: PyFunction = PyFunction()
        #self.orchestrator: PyFunction = PyFunction()
        self.constraints: dict[int, Constraint] = {}
        self.objectives: dict[int, Objective] = {}
        #self.run_creators: dict[int, Run_Creator] = {}
        self.runs: DataFrame = DataFrame()
        self.results: DataFrame = DataFrame()
        self.task_statuses: DataFrame = DataFrame()
        self._class_list = [Constraint, Objective] # , Run_Creator
        # Put task status matrix into a "Results" object?
        setattr(self, CONS.EDIT, True)

    def new(self, class_obj: Type[Constraint]|Type[Objective], **kwargs):
        """create a new workflow or study"""
        return self._new(class_obj, **kwargs)

    def delete(self, class_obj: Type[Constraint]|Type[Objective], oid: int):
        """delete an object by id"""
        self._delete(class_obj, oid)
        # if isinstance(dictobj, DataFrame):
        #    dictobj.drop(index=oid)

    def add_runs(self, creator_id):
        """add runs from run creator to runs dataframe"""
        creator = self.run_creators[creator_id]
        _attr_name, change = creator.exec(self)
        self.runs = change["new"]

    def __setattr__(self, name, value):
        if name == "workflow":
            if value is not None:
                value = deepcopy(value)
                value.set_editable(False)
        super().__setattr__(name, value)

    def set_editable(self, editable: bool):
        """setter for _editable property"""
        setattr(self, CONS.EDIT, editable)

class Plot(BaseClass):
    """plot object holding figure and static data"""

    def __init__(self, _id: int = -1, name: str = "", data_id: int = -1, vtype=None):
        super().__init__(_id, name, self.__class__.__name__)
        scriptpath = path.dirname(path.abspath(__file__))
        self._file = path.join(scriptpath, "gui", "plot_view.py")
        self.data_id = data_id
        vtype = get_args(CONS.PlotTypes)[0] if vtype is None else vtype
        setattr(self, CONS.TYPE, Options(CONS.PlotTypes, vtype))
        #self.py_function = PyFunction(file=self._file)
        self.create_plot = self.create_plot_call
        plt.style.use("dark_background")
        setattr(self, CONS.FIG, plt.figure())

    def create_plot_call(self, analysis):
        """create plot and update figure attribute"""
        data_set = analysis.data_sets[self.data_id]
        call = self.py_function.callable
        new_figure = call(data_set)
        trace = ["figure", str(getattr(self, CONS.ID)), "plots"]
        change = {"old": getattr(self, CONS.FIG), "new": new_figure}
        return trace, change

    def __setattr__(self, name, value):
        if name == CONS.TYPE:
            if value == "Custom":
                self.py_function = PyFunction(file="")
            else:
                self.py_function = PyFunction(file=self._file, fun=str(value))
            if isinstance(value, str):
                value = Options(CONS.PlotTypes, value)
        super().__setattr__(name, value)

class Analysis(BaseClass):
    """Post object containing data, plots, and ML models"""

    def __init__(self, _id: int = -1, name: str = ""):
        super().__init__(_id, name, self.__class__.__name__)
        #self.data_sets: dict[int, Data_Set] = {}
        self.plots: dict[int, Plot] = {}
        #self.models: dict[int, Model] = {}
        self._class_list = [Plot] # Data_Set, Model
        self.data_file = ""
        self.import_data = partial(self.import_data_call)

    def new(self, class_obj: Type[Plot], **kwargs):
        """create a new plot"""
        return self._new(class_obj, **kwargs)

    def delete(self, class_obj: Type[Plot], oid: int):
        """delete an object by id"""
        self._delete(class_obj, oid)

    def import_data_call(self):
        """import CSV or Excel file as a Data Set"""
        data_set = DataFrame()
        if path.exists(self.data_file):
            _base, ext = path.splitext(self.data_file)
            if ext == ".csv":
                data_set = read_csv(self.data_file)
            elif ext == ".xlsx":
                data_set = read_excel(self.data_file)
            else:
                raise TypeError(
                    f"data file is not an Excel or CSV file: {self.data_file}"
                )
        change = {"new": data_set, "old": None}
        return "data_sets", change

class Project(BaseClass):
    """Project"""

    def __init__(self, _id: int = -1, name: str = ""):
        super().__init__(_id, name, self.__class__.__name__)
        self.file_path = ""
        self.workflows: dict[int, Workflow] = {}
        self.studies: dict[int, Study] = {}
        self.analyses: dict[int, Analysis] = {}
        self._class_list = [Workflow,Study,Analysis]
        # self.tasks: dict[int, Task] = {}
        # self.postviews?
        # self.setups?

    def save(self) -> bool:
        """save project at current file path"""
        # Use shutil to zip and unzip files to save space?
        if not self.file_path:
            return False
        hp.save_obj(self, self.file_path)
        return True

    def save_as(self, projpath: str):
        """save project at specified file path"""
        self.file_path = path.abspath(projpath)
        hp.save_obj(self, self.file_path)

    def open(self, projpath: str):
        """open project file at given path"""
        hp.read_obj(projpath, dict_to_obj, self)
        self.file_path = projpath
        return self

    def new(self, class_obj: Type[Workflow]|Type[Study]|Type[Analysis], **kwargs):
        """create a new workflow or study"""
        return self._new(class_obj, **kwargs)

    def delete(self, class_obj: Type[Workflow]|Type[Study]|Type[Analysis], oid: int):
        """delete an object by id"""
        self._delete(class_obj, oid)

class Session(BaseClass):
    """Session"""

    def __init__(self, _id: int, name: str = "Session"):
        super().__init__(_id, name, self.__class__.__name__)
        delattr(self, "_trace")
        self.name = name
        self.projects: dict[int, Project] = {}
        self._class_list = [Project]
        #self.library: Library = Library(0)
        # TODO: include GUI session properties here?
        # include a session command history?

    def open_project(self, projpath: str):
        """open a project file"""
        pid = hp.next_id(self.projects)
        project = Project(_id=pid).open(projpath)
        self.projects[pid] = project
        return project

    def new(self, class_obj: Type[Project], **kwargs):
        """create a new constraint or objective"""
        return self._new(class_obj, **kwargs)

    def delete(self, class_obj: Type[Project], oid: int):
        """delete an object by id"""
        self._delete(class_obj, oid)

CLASS_LIST = [
    Input,
    Output,
    Constraint,
    Objective,
    Dependency,
    Method,
    Task,
    Workflow,
    Project,
    Session,
    NotApplicable,
    Options,
]
CLASS_DICT = {obj.__name__: obj for obj in CLASS_LIST}

def dict_to_obj(obj: Any, dictionary: dict) -> Any:
    """Recursively convert dictionary to nested objects

    Args:
        obj (Any): instance of an object to set attributes of
        dictionary (dict): dictionary defining attributes (keys) and values

    Returns:
        Any : obj with updated attributes from dictionary
    """
    for key, value in dictionary.items():
        if key == CONS.CLASS:
            continue  # skip reading "classname" attribute
        if hasattr(obj, key):
            if isinstance(getattr(obj, key), DataFrame):
                df_data = value["list"]
                df_columns = value["columns"]
                value = DataFrame.from_dict(df_data, orient="index", columns=df_columns)
                setattr(obj, key, value)
                continue
        if isinstance(value, dict):
            subobj = {}
            if CONS.CLASS in value:
                subobj = CLASS_DICT[value[CONS.CLASS]]()
                value.pop(CONS.CLASS, None)
            subobj = dict_to_obj(subobj, value)
            if isinstance(obj, dict):
                if key.isdigit():
                    key = int(key)
                obj[key] = subobj
            else:
                setattr(obj, key, subobj)
        elif isinstance(obj, dict):
            obj[key] = value
        else:
            setattr(obj, key, value)
    return obj
