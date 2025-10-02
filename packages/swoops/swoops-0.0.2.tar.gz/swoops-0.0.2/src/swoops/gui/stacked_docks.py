"""
Written by Jason Krist
05/01/2024

to do (now):
    - functions to control data structures
        - Connect "new" functions to create and open edit window
        - Where should I put delete function? (edit window, context window in Tree)
        - Click on Tree Item opens Edit Window for object (or right click > Edit?)
    - connect all data structures and models together
    - allow toolbar to be hidden (add collapse / expand button)

to do (later):
    - max and min on double click at pt location
    - add search icon next to search bar (and use buttom swap idea from VScode)
    - add ability to drag up on screen to maximize again
    - complete custom Dock widget title
    - cleanup functions and classes that I am keeping

"""


from PySide6.QtCore import (  # pylint: disable=E0611,E0401,C0413
    Qt,
)

from PySide6.QtWidgets import (  # pylint: disable=E0611,E0401,C0413
    QMainWindow,
    QSizePolicy,
    QDockWidget,
    QTabWidget,
    QStackedWidget,
    QSplitter,
    QWidget,
    QHBoxLayout,
    QPushButton,
    QLabel,
)

try:
    import widgets as wd  # type: ignore # pylint: disable=E0611,E0401,C0413
    from helper import list_length_check
    import swoops.constants as CONS
    from swoops.gui import undo_commands as uc

except ImportError:
    from . import widgets as wd  # type: ignore # pylint: disable=E0611,E0401,C0413
    from .helper import list_length_check
    from .. import constants as CONS
    from . import undo_commands as uc


class StackedDocks(QStackedWidget):
    """stacked widget with a page per tab"""

    def __init__(self):  # , parent
        super().__init__()  # parent
        self.pages = {}
        self.containers = {}

    def add_page(self, tab_index): # , labels, callbacks
        """add a stacked page to the stacked widget"""
        page = wd.WidgetLayout(None, vertical=True)
        #icons = [None] * len(labels)
        #toolbar = wd.ToolBarFrame(self, labels, icons, callbacks)
        # toolbar.setStyleSheet("border-bottom: 0.5px solid gray")
        container = DockContainer(self)  # self,
        # add toolbar and dock widgets
        #page.box.addWidget(toolbar)
        page.box.addWidget(container)
        self.addWidget(page)
        self.pages[tab_index] = page
        self.containers[tab_index] = container
        return page

    def remove_page(self, tab_index):
        page = self.pages.pop(tab_index)
        container = self.containers.pop(tab_index)
        self.removeWidget(page)
        page.deleteLater()
        container.deleteLater()

    def add_hidden(self, tabname, titles, widgets, areas):
        """add hidden widgets to page with tabname"""
        tabind = list(CONS.TABS).index(tabname)
        self.containers[tabind].add_hidden(tabname, titles, widgets, areas)

    def set_dock_callback(self, callback):
        """set a callback for dock visitibility change"""
        for container in self.containers:
            for name, dock in container.docks.items():
                dock.visibilityChanged.connect(lambda x, name=name: callback(name, x))

class DockWidget(QDockWidget):
    """adds custom floating title bar to docks"""

    def __init__(self, *args, **kwargs):
        self.title = args[0]
        self.container = args[1]
        self.widget_id = int(kwargs.get("objectName", "-1"))
        super().__init__(*args, **kwargs)
        self.topLevelChanged.connect(self.floating_titlebar)
        #self.setWindowFlags(Qt.Window | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)
        #self.dockLocationChanged.connect(self.area_changed)
    
    def closeEvent(self, _event):
        self.container.stack.app.integrator.exec(uc.DelWidget, args=(self.widget_id,))
        #self.container.unpack(self.widget_id)

    def toggle_max(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

        # Add minimize/maximize buttons when floating
    def floating_titlebar(self, is_floating):
        #title_bar = self.titleBarWidget()
        if is_floating:
            # Create custom title bar with buttons
            titlebar = QWidget()
            layout = QHBoxLayout(titlebar)
            layout.setContentsMargins(4, 2, 4, 2)
            label = QLabel(self.title)
            layout.addWidget(label)
            btn_min = QPushButton("-")
            btn_min.setFixedWidth(24)
            btn_min.clicked.connect(lambda: self.setWindowState(self.windowState() | Qt.WindowMinimized))
            layout.addWidget(btn_min)
            btn_max = QPushButton("□")
            btn_max.setFixedWidth(24)
            btn_max.clicked.connect(self.toggle_max)
            layout.addWidget(btn_max)
            btn_close = QPushButton("×")
            btn_close.setFixedWidth(24)
            btn_close.clicked.connect(self.close)
            layout.addWidget(btn_close)
            self.setTitleBarWidget(titlebar)
        else:
            self.setTitleBarWidget(None)

    #def area_changed(self, area):
    #    self.stack.app.integrator.exec(uc.EditWidget, args=(self.widget_id, "area", area, True))

    # def resizeEvent(self, event):
    #     super().resizeEvent(event)
    #     width = event.size().width()
    #     height = event.size().height()
    #     self.stack.app.integrator.exec(uc.EditWidget, args=(self.widget_id, "size", (width, height)))

class DockContainer(QMainWindow):
    """main window containing dock widgets"""

    def __init__(self, stack):  # parent,
        # list_length_check([titles, widgets, areas], ["titles", "widgets", "areas"])
        super().__init__()  # parent
        self.docks = {}
        self.swidgets = {}
        self.stack = stack
        # Check that names, widgets, areas are same length
        self.setTabPosition(Qt.AllDockWidgetAreas, QTabWidget.North)
        self.setCorner(Qt.TopLeftCorner, Qt.LeftDockWidgetArea)
        self.setCorner(Qt.BottomLeftCorner, Qt.LeftDockWidgetArea)
        self.setCorner(Qt.TopRightCorner, Qt.RightDockWidgetArea)
        self.setCorner(Qt.BottomRightCorner, Qt.RightDockWidgetArea)
        splitter = QSplitter()
        splitter.setFixedHeight(10)
        splitter.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setCentralWidget(splitter)
        #self.setWindowFlags(Qt.Window | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)

    def pack(self, swidget, title:str, area):
        self.swidgets[swidget._id] = swidget
        dock = DockWidget(title, self, objectName=str(swidget._id))
        dock.setStyleSheet("border: 1px solid light gray")
        dock.setAllowedAreas(Qt.AllDockWidgetAreas)
        dock.setWidget(swidget._widget)
        self.addDockWidget(area, dock)
        self.docks[swidget._id] = dock

    def unpack(self, widget_id:int):
        dock = self.docks.pop(widget_id)
        self.removeDockWidget(dock)
        return dock

class STab:
    def __init__(self, app, _id:int, tabname:str, swidgets:list):
        self.app = app
        self._id = _id
        self.name = tabname
        self.swidgets = swidgets

    def create_widgets(self):
        for swidget in self.swidgets:
            swidget.set_tab_id(self._id)
            self.app.integrator.new_widget(swidget)

    def delete_widgets(self):
        for swidget in self.swidgets:
            self.app.integrator.del_widget(swidget._id)

class SWidget:
    def __init__(self, stack, widget_partial, model_partial, dock_area, title):
        # Swidget class - tab_id, tab_name, dock_location, _widget, _dock
        self.stack = stack
        self.packed = False
        self._dock = None
        #self.size = None
        
        self.partial = widget_partial
        self.model_partial = model_partial
        self._widget = None
        self._id = None
        self.area = dock_area
        self.title = title

        self.tab_id = None
        self._tab_name = None
        self._container = None

    def __repr__(self):
        return f"SWidget({self._id}, {self.tab_id}, {self.title}), {self._widget.__class__.__name__})"

    def __setattr__(self, name, value):
        repack = False
        if name in ["area"] and self.packed:
            self.unpack()
            self.delete()
            repack = True
        #elif (name == "title") and (self._dock is not None):
        #    self._dock.setWindowTitle(value)
        #elif name in ["size"] and (self._dock is not None) and (self.size is not None):
        #    self._dock.resize(self.size[0], self.size[1])
        # TODO: change tab_name and container upon tab_id change
        super().__setattr__(name, value)
        if repack:
            self.create(self._id)
            self.pack()

    def set_tab_id(self, tab_id:int):
        self.tab_id = tab_id
        self._tab_name = self.stack.app.titlebar.tabnames[tab_id]
        self._container = self.stack.containers[tab_id]

    def check_tab_set(self):
        if self.tab_id is None:
            raise AttributeError("tab_id is not set")

    def create(self, _id:int):
        self._id = _id
        self._widget = self.partial()

    def delete(self):
        self._widget.deleteLater()
        self._widget = None

    def pack(self):
        self._dock = self._container.pack(self, self.title, self.area)
        self.packed = True

    def unpack(self):
        self._container.unpack(self._id) # self
        self.packed = False
        self._dock = None