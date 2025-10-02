"""
Written by Jason Krist
05/01/2024

Building blocks go: 
    > constants
        > styles , structures , widgets
            > gui
                > title_bar , edit_window , project_tree ,
                table_view , workflow_view , command_window
                    > app

TODO:
    - Loading Indicator for "set active workflow" and Workflow Name on Viewer and Table
    - Add popover when project is saved
    - task updates change workflow viewers
    - reorganize init function to be easier to edit
    - create a QSplashScreen
    - think about when loading screens would help
    - Other Widgets:
        - Python Editor (coloring and run button), or jupyter notebook?
        - Plot Output Window (embed interactive?, or open file)

"""

import time
starttime = time.time()
print(f"    App.py Start time: {starttime}")

# import cProfile
from os import path
from functools import partial
print(f"    App.py Import Time 1: {time.time() - starttime}")

from pandas import DataFrame
print(f"    App.py Import Time 2: {time.time() - starttime}")

from PySide6.QtCore import (
    Qt,  # pylint: disable=E0611,E0401,C0413
)

from PySide6.QtGui import (  # pylint: disable=E0611,E0401,C0413
    QIcon,
)

from PySide6.QtWidgets import (  # pylint: disable=E0611,E0401,C0413
    QMainWindow,
    QPushButton,
    QApplication,
)
print(f"    App.py Import Time 3: {time.time() - starttime}")


try:
    from .gui import widgets as w
    from .gui.integrator import Integrator  # type: ignore # pylint: disable=E0611,E0401,C0413
    import constants as CONS
    from .gui.title_bar import TitleBar
    from .gui import table_view as tv
    from .gui import edit_window as ew
    from .gui import tree_view as tr
    from .gui.stacked_docks import StackedDocks, SWidget, STab
    from .gui import undo_commands as uc
except ImportError:
    from swoops.gui import widgets as w
    from swoops.gui.integrator import Integrator
    import swoops.constants as CONS
    from swoops.gui.title_bar import TitleBar
    from swoops.gui import table_view as tv
    from swoops.gui import edit_window as ew
    from swoops.gui import tree_view as tr
    from swoops.gui.stacked_docks import StackedDocks, SWidget, STab
    from swoops.gui import undo_commands as uc
print(f"    App.py Import Time 4: {time.time() - starttime}")

class App(QMainWindow):
    """main window"""

    def __init__(self, qapp:QApplication, session):
        super(App, self).__init__()
        # Create Integrator
        self.qapp = qapp
        self.dark = False
        self.qapp.setStyle('plastique')
        #self.qapp.setStyle('Fusion') 
        self.integrator = Integrator(self, session=session)
        self.titlebar = self.create_titlebar()
        self.tabs = {} # self.titlebar.tabs
        self.stack = TestStack4(self)
        # Create Central Widget, Titlebar, and Stacked Widget
        self.central = w.WidgetLayout(self, vertical=True, central=True)
        self.stack.create_widgets()
        self.central.box.addWidget(self.titlebar)
        self.central.box.addWidget(self.stack)

    def new_tab(self, tabname:str):
        tab_index = self.titlebar.add_tab(tabname)
        _page = self.stack.add_page(tab_index)
        self.tabs[tab_index] = STab(self, tab_index, tabname, [])
        return self.tabs[tab_index]

    def del_tab(self, tab_index:int):
        """delete a tab from the app"""
        tab = self.tabs.pop(tab_index)
        tab.delete_widgets()
        _tabname = self.titlebar.remove_tab(tab_index)
        self.stack.remove_page(tab_index)
        return tab

    def add_tab(self, tab:STab):
        self.titlebar.tabbar.insertTab(tab._id, tab.name)
        _page = self.stack.add_page(tab._id)
        tab.create_widgets()
        self.tabs[tab._id] = tab 

    def rename_tab(self, tab_id:int, tabname:str):
        old_tabname = self.titlebar.rename_tab(tab_id, tabname)
        return old_tabname

    def open_help(self):
        """open help documentation"""
        print("\nHELP IS ON THE WAY!")

    def open_settings(self):
        """open settings menu"""
        print("\nSettings no worky.")

    def toggle_dark(self):
        """toggle dark mode and refresh widget colors reliably"""
        # Toggle dark mode state
        if self.dark:
            QApplication.instance().setStyle(CONS.LIGHT_STYLE)
        else:
            QApplication.instance().setStyle(CONS.DARK_STYLE)
        self.dark = not self.dark

    def close_window(self):
        """close window"""
        # self.integrator.stack.changing_index = True
        self.window().close()

    def create_titlebar(self):
        """Create TitleBar Widget"""
        # Set Window Icon
        #self.setWindowFlags(Qt.WindowType.CustomizeWindowHint) # self.setWindowFlags(Qt.WindowType.FramelessWindowHint) Frameless is bad
        # self.setStyleSheet("border:1px solid white;border-radius:3px;")
        self.setWindowTitle(f"SWOOPS v" + CONS.VERSION+" - Filename")
        self.setWindowIcon(QIcon(path.join(path.dirname(path.realpath(__file__)), f"./gui/icons/{CONS.ZIPPY_SQ_ICON}")))
        # Title Bar Callbacks
        win_calls = [
            getattr(self, value["call"]) for value in CONS.WIN_BUTTONS.values()
        ]
        file_calls = [getattr(self.integrator, value["call"]) for value in CONS.FILE_MENU.values()]
        #view_calls = [lambda x, i=i: self.view_toggle(i, x) for i, _t in CONS.VIEW_MENU]
        view_calls = [lambda x, i=i: self.integrator.print_log for i, _t in CONS.VIEW_MENU]
        menu_calls = [file_calls, view_calls]
        undo_calls = [self.integrator.undostack.undo, self.integrator.undostack.redo]
        # Create Title Bar with Callbacks
        titlebar = TitleBar(self, win_calls, menu_calls, undo_calls, self.placeholder)
        # titlebar.title.setText(f"OpenStudy v{CONS.VERSION} - {self.project.path}")
        self.integrator.viewmenu = titlebar.menubar.menus[1]
        titlebar.tabbar.currentChanged.connect(self.tab_change)
        return titlebar

    def tab_change(self, tab_index):
        # TODO: check if "+" tab is clicked to create a new one
        if self.tabs[tab_index] == "+":
            print(f"Tab Change Placeholder Callback")
            #self.integrator.add
        self.stack.setCurrentIndex(tab_index)

    def placeholder(self):
        print("Placeholder Callback")

    def dock_closed(self):
        print("Dock Closed Placeholder Callback")



class TestStack1():
    def __init__(self, integrator):
        self.integrator = integrator
        self.wf = self.integrator.session.projects[1].workflows[1]
        self.integrator.tablemodels = {}
        for key, value in self.wf.__dict__.items():
            if isinstance(value, (dict, DataFrame)):
                self.integrator.tablemodels[key] = tv.TabTableModel(self.integrator, self.wf._trace, key)
        self.integrator.editmodel = ew.EditTableModel(self.integrator, current = self.wf)
        self.table1 = ew.EditWindow(self.integrator)
        self.table2 = ew.EditWindow(self.integrator)
        self.view1 = tv.TabTableViews(self.integrator)
        self.view2 = tv.TabTableViews(self.integrator)
        self.central = w.WidgetLayout(None)
        self.left = w.WidgetLayout(self.central, vertical=True)
        self.central.box.addWidget(self.left)
        self.left.box.addWidget(self.view1)
        self.left.box.addWidget(self.view2)
        self.central.box.addWidget(self.table1)
        self.central.box.addWidget(self.table2)
        self.button = QPushButton("Print Session")
        self.button.clicked.connect(self.integrator.print_log)
        self.central.box.addWidget(self.button)

class TestStack2(w.WidgetLayout):
    def __init__(self, integrator):
        # TODO: add project view?
        super().__init__(None)
        self.integrator = integrator
        self.wf = self.integrator.session.projects[1].workflows[1]
        self.integrator.tablemodels = {}
        for key, value in self.wf.__dict__.items():
            if isinstance(value, (dict, DataFrame)):
                self.integrator.tablemodels[key] = tv.TabTableModel(self.integrator, self.wf._trace, key)
        self.integrator.editmodel = ew.EditTableModel(self.integrator, current = self.wf)
        self.table1 = ew.EditWindow(self.integrator)
        self.table2 = ew.EditWindow(self.integrator)
        self.view1 = tv.TabTableViews(self.integrator)
        self.view2 = tv.TabTableViews(self.integrator)
        self.left = w.WidgetLayout(self, vertical=True)
        self.box.addWidget(self.left)
        self.left.box.addWidget(self.view1)
        self.left.box.addWidget(self.view2)
        self.box.addWidget(self.table1)
        self.box.addWidget(self.table2)
        self.button = QPushButton("Print Session")
        self.button.clicked.connect(self.integrator.print_log)
        self.box.addWidget(self.button)

class TestStack3(StackedDocks):

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.integrator = app.integrator
        self.integrator.tabs = app.titlebar.tabs
        # Copied from TestStack2
        self.wf = self.integrator.session.projects[1].workflows[1]
        self.integrator.models[tv.TabTableModels] = tv.TabTableModels(self.integrator, self.wf._trace)
        self.integrator.models[ew.EditTableModel] = ew.EditTableModel(self.integrator, current = self.wf)
        self.integrator.models[tr.TreeModel] = tr.TreeModel(self.integrator)
        self.changing_index = False
        #self.tabs = CONS.TABS
        self.widget_map = {}
        for tabname in self.integrator.tabs: # self.tabs.items()
            #tb_calls = [getattr(integrator, call) for call in tabdict.values()]
            #tb_labels = list(tabdict.keys())
            # Stacked Widget Dock Contents
            self.add_page(tabname) # , tb_labels, tb_calls
        self.set_dock_callback(self.integrator.app.dock_closed)

    def create_widgets(self):
        tree_partial = partial(tr.TreeView, self.integrator)
        table_partial = partial(tv.TabTableViews, self.integrator)
        edit_partial = partial(ew.EditWindow, self.integrator)
        swidget = SWidget(self, tree_partial, None, 0, Qt.LeftDockWidgetArea, "Tree 1")
        self.integrator.new_widget(swidget)
        swidget = SWidget(self, table_partial, None, 0, Qt.TopDockWidgetArea, "Table 1")
        self.integrator.new_widget(swidget)
        swidget = SWidget(self, table_partial, None, 0, Qt.BottomDockWidgetArea, "Table 2")
        self.integrator.new_widget(swidget)
        swidget = SWidget(self, edit_partial, None, 0, Qt.LeftDockWidgetArea, "Edit 1")
        self.integrator.new_widget(swidget)
        swidget = SWidget(self, edit_partial, None, 0, Qt.RightDockWidgetArea, "Edit 2")
        self.integrator.new_widget(swidget)
        swidget = SWidget(self, tree_partial, None, 0, Qt.RightDockWidgetArea, "Tree 2")
        self.integrator.new_widget(swidget)

        # Create Widget
        swidget = SWidget(self, edit_partial, None, 0, Qt.RightDockWidgetArea, "Tsdfsf")
        self.integrator.exec(uc.NewWidget, args=(swidget,))
        # Delete Widget
        #self.integrator.exec(uc.DelWidget, args=(swidget._id,))
        # Create it again
        #self.integrator.exec(uc.NewWidget, args=(swidget,))
        # Edit its location
        #self.integrator.exec(uc.EditWidget, args=(swidget._id, "area", Qt.LeftDockWidgetArea, None))

class TestStack4(StackedDocks):

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.integrator = app.integrator
        # Copied from TestStack3
        self.wf = self.integrator.session.projects[1].workflows[1]
        self.integrator.models[tv.TabTableModels] = tv.TabTableModels(self.integrator, self.wf._trace)
        self.integrator.models[ew.EditTableModel] = ew.EditTableModel(self.integrator, current = self.wf)
        self.integrator.models[tr.TreeModel] = tr.TreeModel(self.integrator)

    def create_widgets(self):

        # Create Tab 1
        tree_partial = partial(tr.TreeView, self.integrator)
        table_partial = partial(tv.TabTableViews, self.integrator)
        edit_partial = partial(ew.EditWindow, self.integrator)
        n2_path = r"C:\Users\jkris\OneDrive\2022_onward\2025\python\swoops\test\test_gui\n2.html"
        web_partial = partial(w.WebView, n2_path, file=True)

        swidgets = [
            SWidget(self, tree_partial, None, Qt.LeftDockWidgetArea, "Project Tree 1"),
            SWidget(self, table_partial, None, Qt.BottomDockWidgetArea, "Workflow Table 1"),
            SWidget(self, edit_partial, None, Qt.RightDockWidgetArea, "Edit Window 1"),
            #SWidget(self, web_partial, None, Qt.TopDockWidgetArea, "Web View 1"),
        ]
        tab1 = STab(self.app, 0, "Tab 1", swidgets)
        self.app.add_tab(tab1)

        # Create Tab 2
        swidgets = [
            SWidget(self, table_partial, None, Qt.BottomDockWidgetArea, "Workflow Table 2"),
            SWidget(self, tree_partial, None, Qt.LeftDockWidgetArea, "Project Tree 2"),
            SWidget(self, edit_partial, None, Qt.RightDockWidgetArea, "Edit Window 2"),
            #SWidget(self, web_partial, None, Qt.TopDockWidgetArea, "Web View 1"),
        ]
        tab2 = STab(self.app, 1, "Tab 2", swidgets)
        self.app.add_tab(tab2)

print(f"    App.py Import Time 5: {time.time() - starttime}")

