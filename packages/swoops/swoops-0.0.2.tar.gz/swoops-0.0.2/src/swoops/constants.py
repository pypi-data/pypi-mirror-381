"""
Written by Jason Krist
05/01/2024
"""

from typing import Literal, get_args
from PySide6.QtCore import Qt  # type: ignore # pylint: disable=E0611,E0401,C0413

NAME = "SWOOPS"
VERSION = "0"
DARK_STYLE = "Fusion"
LIGHT_STYLE = "windowsvista"

# In[0] Object Types (Literals)
InputTypes = Literal["Continuous", "Discrete", "Increment", "Sequential"]
DistTypes = Literal["Uniform", "Normal", "Random"]
OutputTypes = Literal["float", "int", "str", "array", "bool"]
TaskTypes = Literal["Shell Commands", "Python Commands"]
# , "Python Script", "Shell Script"
DependTypes = Literal["Python", "Files", "Success"]  # , "Memory"
SampleTypes = Literal[
    "Empty",
    "Current, Min, Max",
    "Latin Hypercube (LHS)",
    "Monte Carlo (MCS)",
    "Custom",
]
PlotTypes = Literal[
    "pair_plot",
    "scatter_plot",
    "bar_plot",
    "correlation_plot",
    "correlation_heatmap",
    "pie_chart",
    "Custom",
]

CLASS = "classname"
ID = "_id"
TYPE = "_type"
EDIT = "_editable"
FIG = "figure"

WidgetTypes = Literal[
    "Project Tree",
    "Edit Window",
    "Workflow Viewer",
    "Table Viewer",
    "Study Viewer",
    "Command Window",
    "Plot Viewer",
]
WIDGET_NAMES = list(get_args(WidgetTypes))

# In[0] Dropdown Menus
MenuItemTypes = Literal["action", "menu", "checkbox"]
FILE_MENU = {
    # ("New Window", "action"),
    "New": {"type": "action", "call": "new_project"},
    "Recent": {"type": "menu", "call": "placeholder"},
    "Open": {"type": "action", "call": "open_project"},
    "Save": {"type": "action", "call": "save_project"},
    "Save As": {"type": "action", "call": "save_as_project"},
    "Run Script": {"type": "action", "call": "placeholder"},
    "Settings": {"type": "action", "call": "placeholder"},
    "Help": {"type": "action", "call": "placeholder"},
}
VIEW_MENU = list((name, "checkbox") for name in WIDGET_NAMES)

# In[0] Tabs and their Corresponding Buttons
TABS = {
    "Setup": {
        "New Workflow": "ph",
        "New Task": "ph",
    },
    "Workflow": {
        "New Workflow": "new_workflow",
        "New Task": "new_task",
        "New Group": "new_group",
        "New Pool": "new_pool",
        "New Input": "new_input",
        "New Output": "new_output",
    },
    "Optimize": {
        "New Constraint": "new_constraint",
        "New Objective": "new_objective",
        "New Optimization": "ph",
        "New Algorithm": "ph",
    },
    "Orchestrate": {
        "New Run Creator": "new_run_creator",
        "New DOE": "ph",
        "New MCS": "ph",
        "Run": "ph",
        "Stop": "ph",
    },
    "Post": {
        "Convergence": "ph",
        "Constraints": "ph",
        "Bounds": "ph",
        "Create Plot": "ph",
        "Analyze": "ph",
        "Filter": "ph",
    },
    "Surrogates": {
        "Fit New Model": "ph",
        "Predict": "ph",
        "CV Plot": "ph",
        "Feature Importance": "ph",
        "ANOVA": "ph",
        "Model to Task": "ph",
    },
    #   "+": {"Insert Buttons Here": "new_toolbar_button"},
}

# In[0] Search Bar Functions
FUNCTIONS = (list(items) for items in TABS.values())

# In[0] Undo and Window Title Bar Icons and Tips
ZIPPY_ICON = "zippy.png"
ZIPPY_SQ_ICON = "zippy_square.png"
UNDO_BUTTONS = {
    "Undo": {"icon": "arrow-left.svg", "call": "undo"},
    "Redo": {"icon": "arrow-right.svg", "call": "redo"},
}
WIN_BUTTONS = {
    "Settings": {"icon": "gear.svg", "call": "open_settings"},
    "Help": {"icon": "help.svg", "call": "open_help"},
    "Toggle Dark": {"icon": "color-mode.svg", "call": "toggle_dark"},
    #"Minimize": {"icon": "dash.svg", "call": "show_minimized"},
    #"Unmaximize": {"icon": "multiple-windows.svg", "call": "show_normal"},
    #"Maximize": {"icon": "window.svg", "call": "show_maximized"},
    #"Close": {"icon": "close.svg", "call": "close_window"},
}


# In[0] Docker Layouts of stacked widgets
STACKS = {
    "Setup": {
        "Project Tree": Qt.LeftDockWidgetArea,
        "Edit Window": Qt.RightDockWidgetArea,
        "Workflow Viewer": Qt.TopDockWidgetArea,
        "Table Viewer": Qt.BottomDockWidgetArea,
        "Command Window": Qt.LeftDockWidgetArea,
    },
    "Workflow": {
        "Project Tree": Qt.LeftDockWidgetArea,
        "Edit Window": Qt.RightDockWidgetArea,
        "Workflow Viewer": Qt.TopDockWidgetArea,
        "Table Viewer": Qt.BottomDockWidgetArea,  #  (Workflow)
        "Command Window": Qt.LeftDockWidgetArea,
    },
    "Orchestrate": {
        "Project Tree": Qt.LeftDockWidgetArea,
        "Edit Window": Qt.RightDockWidgetArea,
        "Study Viewer": Qt.TopDockWidgetArea,
        "Table Viewer": Qt.BottomDockWidgetArea,  #  (Study)
        "Command Window": Qt.LeftDockWidgetArea,
    },
    "Optimize": {
        "Project Tree": Qt.LeftDockWidgetArea,
        "Edit Window": Qt.RightDockWidgetArea,
        "Plot Viewer": Qt.TopDockWidgetArea,
        "Table Viewer": Qt.BottomDockWidgetArea,  #  (Study)
        "Command Window": Qt.LeftDockWidgetArea,
    },
    "Post": {
        "Project Tree": Qt.LeftDockWidgetArea,
        "Edit Window": Qt.RightDockWidgetArea,
        "Plot Viewer": Qt.TopDockWidgetArea,
        "Table Viewer": Qt.BottomDockWidgetArea,  #  (Analysis)
        "Command Window": Qt.LeftDockWidgetArea,
    },
    "Surrogates": {
        "Project Tree": Qt.LeftDockWidgetArea,
        "Edit Window": Qt.RightDockWidgetArea,
        "Plot Viewer": Qt.TopDockWidgetArea,
        "Table Viewer": Qt.BottomDockWidgetArea,  #  (Analysis)
        "Command Window": Qt.LeftDockWidgetArea,
    },
}
STACK_DEFAULTS = {
    "Setup": "workflows",
    "Workflow": "workflows",
    "Orchestrate": "studies",
    "Optimize": "studies",
    "Post": "analyses",
    "Surrogates": "analyses",
}
