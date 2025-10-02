"""
Written by Jason Krist
05/01/2024
"""

from os import path

# import sys

from PySide6.QtCore import (  # pylint: disable=E0611,E0401,C0413
    Qt,
    QUrl,
)
from PySide6.QtWidgets import (  # pylint: disable=E0611,E0401,C0413
    QToolButton,
    QToolBar,
    QWidget,
    QCompleter,
    QComboBox,
    QMenu,
    QCheckBox,
    QWidgetAction,
    QTabBar,
    QVBoxLayout,
    QHBoxLayout,
    QSizePolicy,
    QPushButton,
    QFrame,
)
from PySide6.QtGui import (  # pylint: disable=E0611,E0401,C0413
    QIcon,
    QAction,
)

from PySide6.QtWebEngineWidgets import QWebEngineView


try:
    import styles as st  # type: ignore # pylint: disable=E0611,E0401,C0413
    from helper import list_length_check
except ImportError:
    from . import styles as st  # type: ignore # pylint: disable=E0611,E0401,C0413
    from swoops.gui.helper import list_length_check


class WebView(QWebEngineView):

    def __init__(self, url_path:str, file=False):
        super().__init__()
        if file:
            url = QUrl.fromLocalFile(url_path)
        else:
            url = QUrl(url_path)
        self.load(url)


class IconButton(QToolButton):
    """button with icon and optional text"""

    def __init__(self, icon, text, callback, tooltip=""):
        super().__init__()
        # toolbutton.setGeometry(QRect(0, 0, 40, 40))
        # icon = QIcon.fromTheme(QIcon.ThemeIcon.Scanner)
        # pixmap = QPixmap(f"{imagepath} [exact location of image]")
        # icon.addPixmap(pixmap, QIcon.Normal, QIcon.Off)
        if text:
            self.setText(text)
        if text and icon:
            self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        if icon:
            self.setIcon(icon)
        self.clicked.connect(callback)
        if tooltip:
            self.setToolTip(tooltip)


class ToolBar(QToolBar):
    """tool bar with horizontal line of icon buttons"""

    def __init__(
        self,
        icons: list[str | QIcon],
        texts: list[str],
        callbacks: list,
        tooltips: list[str],
    ):
        list_length_check(
            [icons, texts, callbacks, tooltips],
            ["icons", "texts", "callbacks", "tooltips"],
        )
        super().__init__()
        self.actions = []
        self.buttons = []
        for i, icon_path in enumerate(icons):
            icon = icon_path
            if not icon_path:
                icon = ""
            elif isinstance(icon_path, str):
                if not path.exists(icon_path):
                    raise FileNotFoundError(
                        f"Image was not found: {path.abspath(icon_path)}"
                    )
                # imagename = path.basename(icon_path)
                icon = QIcon(icon_path)
            if tooltips[i]:
                button = IconButton(icon, texts[i], callbacks[i], tooltip=tooltips[i])
            else:
                button = IconButton(icon, texts[i], callbacks[i])
            action = self.addWidget(button)
            self.buttons.append(button)
            self.actions.append(action)


class Menu(QMenu):
    """menu containing widgets with callbacks"""

    def __init__(
        self, title: str, subtitles: list[str], mtypes: list[str], callbacks: list
    ):
        list_length_check(
            [subtitles, mtypes, callbacks], ["subtitles", "mtypes", "callbacks"]
        )
        super().__init__(title)
        self.widgets = {}
        for i, label in enumerate(subtitles):
            if mtypes[i] == "action":
                action = self.addAction(label, callbacks[i])
            elif mtypes[i] == "checkbox":
                action = QAction(label, self, checkable=True)
                # checkaction.triggered.connect(menu.show)
                action.toggled.connect(callbacks[i])
                action.setChecked(True)
                self.addAction(action)
            # Delete below section?
            elif mtypes[i] == "checkbox old":
                checkbox = QCheckBox(label, self)
                action = QWidgetAction(self)
                action.setDefaultWidget(checkbox)
                self.addAction(action)
            elif mtypes[i] == "menu":
                action = self.addMenu(label)
                action.addAction("Placeholder 1")
                action.addAction("Placeholder 2")
            else:
                raise ValueError(f"Menu Type {mtypes[i]} not supported!")
            self.widgets[label] = action
            self.addSeparator()


class TabBar(QTabBar):
    """tab bar"""

    def __init__(self, titles: list[str]):
        super().__init__()
        for title in titles:
            self.addTab(title)


class SearchBar(QComboBox):
    """editable searchbar with auto-complete dropdown"""

    def __init__(self, wordlist: list[str], text: str = "Search"):
        super().__init__()
        self.addItems(wordlist)
        self.setEditable(True)
        self.setInsertPolicy(QComboBox.NoInsert)
        self.completer = self.completer()
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.setCurrentText(text)


def create_box(parent, vertical=False):
    """create a box layout with 0 spacing and margins"""
    if vertical:
        layout = QVBoxLayout(parent)
    else:
        layout = QHBoxLayout(parent)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setSpacing(0)
    return layout


class WidgetLayout(QWidget):
    """widget with a layout with 0 spacing and margins"""

    def __init__(self, parent, vertical: bool = False, central: bool = False):
        super().__init__(parent)
        self.box = create_box(self, vertical=vertical)
        if parent is None:
            return
        if central:
            parent.setCentralWidget(self)
        else:
            parent.box.addWidget(self)


class IconBar:
    """row of icons with 0 spacing and fixed size"""

    def __init__(self, parent, iconnames: list, callbacks: list, tooltips: list[str]):
        list_length_check(
            [iconnames, callbacks, tooltips], ["iconnames", "callbacks", "tooltips"]
        )
        scriptdir = path.dirname(path.realpath(__file__))
        icons = [path.join(scriptdir, "icons", name) for name in iconnames]
        self.toolbar = ToolBar(icons, [""] * len(icons), callbacks, tooltips)
        self.actions = self.toolbar.actions
        self.toolbar.setStyleSheet(st.ICONBAR)
        self.toolbar.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        parent.box.addWidget(self.toolbar)


class ToolBarFrame(QFrame):
    """toolbar with text and icons under title bar"""

    def __init__(self, parent, labels: list[str], icons: list, callbacks: list):
        list_length_check([labels, callbacks, icons], ["labels", "callbacks", "icons"])
        super().__init__(parent)
        self.parent = parent
        self.box = create_box(self)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.box.setSpacing(0)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        labels = [label.replace(" ", "\n") for label in labels]
        self.toolbar = ToolBar(icons, labels, callbacks, [""] * len(icons))
        for action in self.toolbar.actions:
            button = self.toolbar.widgetForAction(action)
            button.setStyleSheet(st.TOOLBAR_BUTTON)
        self.toolbar.setStyleSheet(st.TOOLBAR)
        self.toolbar.setFixedHeight(st.TOOLBAR_HEIGHT)
        self.box.addWidget(self.toolbar)


class MenuBar(QWidget):
    """Menu bar with dropdown buttons"""

    def __init__(
        self,
        parent,
        titles: list[str],
        labels: list[list[str]],
        mtypes: list[list[str]],
        callbacks: list[list],
    ):
        list_length_check(
            [titles, labels, callbacks, mtypes],
            ["titles", "labels", "callbacks", "mtypes"],
        )
        super().__init__(parent)
        self.buttons = []
        self.menus = []
        self.box = create_box(self)
        for i, title in enumerate(titles):
            button = QPushButton(title)
            button.setFlat(True)
            button.setStyleSheet(st.MENUBUTTON)
            button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
            menu = Menu(title, labels[i], mtypes[i], callbacks[i])
            menu.setStyleSheet(st.MENUITEMS)
            button.setMenu(menu)
            self.buttons.append(button)
            self.menus.append(menu)
            self.box.addWidget(button)
        parent.box.addWidget(self)
