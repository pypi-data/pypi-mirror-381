"""
Written by Jason Krist
05/01/2024

TODO:
    - implement "VIEW" checkboxes to turn on and off dock widgets
    - implement a QUndoStack and QUndoView?
    - add a better QCompleter to searchbar and make it a button with Icon (empty when pressed)
    - filename label should be minimizable to 0 width (adjust text accordingly)
"""

from os import path

from PySide6.QtCore import (  # pylint: disable=E0611,E0401,C0413
    QSize,
)

from PySide6.QtWidgets import (  # pylint: disable=E0611,E0401,C0413
    QWidget,
    QSizePolicy,
    QTabBar,
)

from PySide6.QtGui import QIcon  # pylint: disable=E0611,E0401,C0413

try:
    import widgets as wd  # type: ignore # pylint: disable=E0611,E0401,
    import swoops.constants as CONS  # type: ignore # pylint: disable=E0611,E0401,C0413
    import styles as st  # type: ignore # pylint: disable=E0611,E0401,C0413
    import helper as hp
except ImportError:
    from . import widgets as wd
    from .. import constants as CONS
    from . import styles as st
    from . import helper as hp


class Zippy:
    """zippy button in top left"""

    def __init__(self, parent, callback, width: int, height: int):
        scriptdir = path.dirname(path.realpath(__file__))
        icon = QIcon(path.join(scriptdir, "./icons/zippy.png"))
        # self.zippy = wd.IconButton(icon, "", parent.zippy, tooltip="Zippy Tippy")
        # self.zippy.setIconSize(QSize(110, 80))
        toolbar = wd.ToolBar([icon], [""], [callback], ["Zippy Tippy"])
        self.toolbar = toolbar
        self.toolbar.setStyleSheet(f"spacing:0px;height:{height}px;width:{width}px;")
        # border-bottom:0.5px solid gray
        self.toolbar.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        # zippy = zippy_bar.widgetForAction(_actions[0])
        self.toolbar.setIconSize(QSize(width, height))
        # self.zippy.setStyleSheet("background-color:transparent")
        parent.box.addWidget(self.toolbar)

class TitleBar(QWidget):
    """custom title bar"""

    def __init__(self, app, win_calls, menu_calls, undo_calls, zippy_call):
        super().__init__()
        # self.setAutoFillBackground(True)# self.setBackgroundRole(QPalette.ColorRole.Highlight)
        self.app = app
        self.initial_pos = None
        self.box = wd.create_box(self)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # Zippy Icon (far left)
        self.zippybutton = Zippy(self, zippy_call, 50, 40)

        # Right Widgets
        self.right = wd.WidgetLayout(self)
        self.right.setFixedHeight(40)


        # File and View Menus
        titles = ["File", "View"]
        file_labels = list(CONS.FILE_MENU.keys())
        file_mtypes = [value["type"] for value in CONS.FILE_MENU.values()]
        labels = [file_labels, hp.getnested(CONS.VIEW_MENU, 0)]
        mtypes = [file_mtypes, hp.getnested(CONS.VIEW_MENU, 1)]
        # TODO: add calls search here?
        self.menubar = wd.MenuBar(self.right, titles, labels, mtypes, menu_calls)

        # Tab Bar
        # self.tabs =  # ["Workflow", "Optimize", "+"]
        #self.tabbar = wd.TabBar(list(CONS.TABS))
        self.tabbar = QTabBar()
        for tab in ["+"]:
            self.tabbar.addTab(tab)
        self.tabbar.setStyleSheet(st.TABBAR)
        self.tabbar.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.right.box.addWidget(self.tabbar)
        empty_space = QWidget(self.right)
        empty_space.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # empty.setStyleSheet("border-bottom: 0.5px solid gray")
        self.right.box.addWidget(empty_space)

        # Upper Right Widgets
        #self.right_top = wd.WidgetLayout(self.right)
        #self.right_top.setFixedHeight(40)

        # Window Title
        # self.title = QLabel(f"{CONS.NAME} v{CONS.VERSION} - Filename", self)
        # self.title.setStyleSheet(st.WINDOW_TITLE)
        # self.title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        # self.title.setMinimumWidth(182)
        # self.title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.right_top.box.addWidget(self.title)

        # Redo and Undo Buttons
        icons = [value["icon"] for value in CONS.UNDO_BUTTONS.values()]
        tips = list(CONS.UNDO_BUTTONS.keys())
        self.undobar = wd.IconBar(self.right, icons, undo_calls, tips)

        # Search Bar
        self.searchbar = wd.SearchBar(CONS.FUNCTIONS)
        self.searchbar.completer.popup().setStyleSheet(st.SEARCHBAR)
        self.searchbar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.searchbar.setMinimumWidth(st.SEARCHBAR_WIDTH_MIN)
        self.searchbar.setMaximumWidth(st.SEARCHBAR_WIDTH_MAX)
        self.searchbar.setStyleSheet(st.SEARCHBAR)
        self.right.box.addWidget(self.searchbar)

        # Top Right Buttons
        icons = [value["icon"] for value in CONS.WIN_BUTTONS.values()]
        tips = list(CONS.WIN_BUTTONS.keys())
        self.winbar = wd.IconBar(self.right, icons, win_calls, tips)
        # self.normal_button = self.winbar.actions[3]
        # self.max_button = self.winbar.actions[4]
        # self.normal_button.setVisible(False)

        # Lower Right Box
        #self.right_bottom = wd.WidgetLayout(self.right)
        #self.right_bottom.setFixedHeight(40)
        # self.right_bottom.box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    def add_tab(self, tabname):
        index = self.tabbar.count() - 1
        self.tabbar.insertTab(index, tabname)
        return index

    def remove_tab(self, index):
        tabname = self.tabbar.tabText(index)
        self.tabbar.removeTab(index)
        return tabname
    
    def rename_tab(self, index, tabname):
        old_tabname = self.tabbar.tabText(index)
        self.tabbar.setTabText(index, tabname)
        return old_tabname

    @property
    def tabnames(self):
        return [self.tabbar.tabText(i) for i in range(self.tabbar.count())]
