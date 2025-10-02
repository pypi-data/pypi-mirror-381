"""
Written by Jason Krist
05/01/2024

TODO:
    - MERGE INTO SINGLE COMMAND WINDOW WITH SAME HISTORY
    - callbacks for record, stop, and run buttons
    - icons for buttons
    - context menu for "copy" commands
    - different colors for commands and responses (bold?)
    - should this just be an ipython console with access to copies of data structures?

"""

import atexit
from qtconsole.rich_jupyter_widget import (  # type: ignore
    RichJupyterWidget,
)
from qtconsole.manager import QtKernelManager  # type: ignore

from PySide6.QtWidgets import (  # pylint: disable=E0611,E0401,C0413
    QFrame,
    QPushButton,
    QTreeView,
    QSizePolicy,
)

from PySide6.QtGui import (  # pylint: disable=E0611,E0401,C0413
    QStandardItemModel,
    QStandardItem,
)

try:
    import widgets as wd  # type: ignore # pylint: disable=E0611,E0401,
except ImportError:
    from . import widgets as wd


class CommandWindowOld(QFrame):
    """window for executing commands and seeing command history"""

    def __init__(self):
        super().__init__()
        self.history = [["cmd1", "rsp1"], ["cmd2", "rsp2"]]
        self.commands = [sublist[0] for sublist in self.history]
        self.box = wd.create_box(self, vertical=True)
        # self.scrollarea = QScrollArea()
        # self.scrollarea.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.scrollarea.setWidgetResizable(True)
        self.tree = CommandTree(self, self.history)
        # self.scrollarea.setWidget(self.tree)
        # Add top buttons
        self.top = wd.WidgetLayout(self)
        expand = QPushButton("Expand All")
        expand.clicked.connect(self.tree.expandAll)
        collapse = QPushButton("Collapse All")
        collapse.clicked.connect(self.tree.collapseAll)
        # record = QPushButton("Record")
        # stop = QPushButton("Stop")
        # run = QPushButton("Run")
        for widget in [expand, collapse]:  # , record, stop, run
            self.top.box.addWidget(widget)
        self.box.addWidget(self.top)
        self.box.addWidget(self.tree)
        # Later, put entire list of commands in suggestions
        self.searchbar = wd.SearchBar(self.commands, text="")
        self.searchline = self.searchbar.lineEdit()
        self.searchline.returnPressed.connect(self.append_command)
        self.scroll = self.tree.verticalScrollBar()
        self.scroll.rangeChanged.connect(self.scroll_to_bottom)
        self.box.addWidget(self.searchbar)

    def scroll_to_bottom(self):
        """scroll treeviewer viewport to bottom"""
        self.scroll.setValue(self.scroll.maximum())

    def append_command(self):
        """add command to history and update tree"""
        # Add some command checking and popup if not valid
        command = self.searchbar.currentText()
        if command in self.commands:
            response = run_command(command)
            self.history.append([command, response])
            self.tree.append_history(command, response)
        else:
            print(f"Command not found: {command}")


def run_command(command):
    """run command interpreter here"""
    response = "\n".join(list(command))
    # capture stdout here?
    return response


class CommandTree(QTreeView):
    """project tree viewer"""

    def __init__(self, parent, history):
        super().__init__(parent)
        self.history = history
        self.model = QStandardItemModel()
        self.setHeaderHidden(True)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.update_view()

    def append_history(self, command, response):
        """append to history and model"""
        self.history.append([command, response])
        self.model = append_row(self.model, command, response)

    def create_model(self):
        """create a new item model from project object"""
        old_model = self.model
        self.model = QStandardItemModel()
        for command, response in self.history:
            self.model = append_row(self.model, command, response)
        del old_model

    def update_view(self):
        """update project tree viewer from item model"""
        # History Model and Tree View
        self.create_model()
        self.setModel(self.model)
        self.expandAll()
        self.resizeColumnToContents(0)
        self.collapseAll()


def append_row(model, command, response):
    """append a row (command with response as child)"""
    item = QStandardItem(command)
    item.setEditable(False)
    subitem = QStandardItem(response)
    subitem.setEditable(False)
    item.appendRow(subitem)
    model.appendRow(item)
    return model


class CommandKernel(QtKernelManager):
    """Have one kernel for all JupyterWidgets"""

    def __init__(self):
        # Start a kernel, connect to it, and create a RichJupyterWidget to use it
        super().__init__(kernel_name="python3")  # kernel could be bash or ir
        self.start_kernel()
        self.kernel_client = self.client()
        self.kernel_client.start_channels()

    # @atexit.register
    # def shutdown_kernel(self):
    #     """shut down jupyter ipython kernel"""
    #     print("Shutting down kernel...")
    #     self.kernel_client.stop_channels()
    #     self.shutdown_kernel()


class CommandWindow(QFrame):
    """A window that contains a single Qt console."""

    def __init__(self, kernel):
        super().__init__()
        self.box = wd.create_box(self, vertical=True)
        self.jupyter_widget = RichJupyterWidget()
        self.jupyter_widget.set_default_style(colors="linux")
        self.jupyter_widget.kernel_manager = kernel
        self.jupyter_widget.kernel_client = kernel.kernel_client
        # USE: Ins - inputs in current session
        # Outs - outputs in current session, dir() for in-scope vars,
        self.box.addWidget(self.jupyter_widget)

    def set_text(self):
        """change console text? idk havent tried it"""
        self.jupyter_widget.input_buffer = "set_text_test sldkfjsldfk"
