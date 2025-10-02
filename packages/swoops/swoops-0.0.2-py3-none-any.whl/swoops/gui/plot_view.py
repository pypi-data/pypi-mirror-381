"""
Written by Jason Krist
06/20/2024
"""

from copy import deepcopy
from math import atan, pi
import seaborn as sns
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas  # type: ignore # pylint: disable=E0611,E0401,
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar  # type: ignore # pylint: disable=E0611,E0401,
import matplotlib.pyplot as plt  # type: ignore # pylint: disable=E0611,E0401,
from PySide6.QtWidgets import QComboBox, QVBoxLayout, QFrame  # type: ignore # pylint: disable=E0611,E0401,

matplotlib.use("Qt5Agg")


class PlotView(QFrame):
    """Widget containing interactive matplotlib figure"""

    def __init__(self, plot=None, trace=None):
        super().__init__()
        # TODO: get Plot object and use figure from it
        # TODO: add a dropdown with all plots in project
        # TODO: when dropdown is picked, run callback to change figure
        plt.style.use("dark_background")
        # self.project = project
        self.trace = trace
        print(f"plot trace: {trace}")
        if plot is None:
            self.figure = plt.figure()
            self.name = "Empty Figure"
        else:
            self.figure = deepcopy(plot.figure)
            self.name = plot.name
        self.figure.suptitle(self.name)
        self.combobox = QComboBox(self)
        # TODO: get list of plots from project or session
        # obj_list, trace_list = get_obj_and_traces()
        label_list = [self.name, "1", "2", "3"]
        self.combobox.addItems(label_list)
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        # self.button = QPushButton("Plot", self)
        # self.button.clicked.connect(self.create_plot)
        self.box = QVBoxLayout()
        self.box.addWidget(self.combobox)
        self.box.addWidget(self.toolbar)
        self.box.addWidget(self.canvas)
        # layout.addWidget(self.button)
        self.setLayout(self.box)

    def create_plot(self, figure, trace):
        # TODO: add functionality to use image of figure instead of interactive
        """plot random data on button push"""
        old_canvas = self.canvas
        old_canvas.deleteLater()
        self.box.removeWidget(old_canvas)
        old_toolbar = self.toolbar
        old_toolbar.deleteLater()
        self.box.removeWidget(old_toolbar)
        self.trace = trace
        plt.style.use("dark_background")
        self.figure = deepcopy(figure)
        # self.figure.tight_layout()
        self.canvas = FigureCanvas(self.figure)
        # self.canvas.draw()  # could use draw_idle?
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.box.addWidget(self.toolbar)
        self.box.addWidget(self.canvas)

    def update(self):
        """update upon data changes"""


# In[0] Plot Types


def pair_plot(*args, **kwargs):
    """create a seaborn pairplot"""
    df = args[0]
    pairgrid = sns.pairplot(df, corner=True, **kwargs)  # , diag_kind="kde"
    return pairgrid.figure


def scatter_plot(x_name, y_name, *args, **kwargs):
    """create a seaborn scatterplot"""
    # x = number, y = number
    df = args[0]
    figure = plt.figure()
    axis = sns.scatterplot(data=df, x=x_name, y=y_name, **kwargs)
    figure.add_axes(axis)
    return figure


def bar_plot(*args, **kwargs):
    """create a seaborn barplot"""
    # x = category, y = number
    df = args[0]
    figure = plt.figure()
    axis = sns.barplot(data=df, **kwargs)
    figure.add_axes(axis)
    return figure


# crosplot is unnecesary, same as scatter
def cross_plot(x_name: str, y_name: str, *args):
    """crossplot of 2 series"""
    df = args[0]
    x_series = df[x_name]
    y_series = df[y_name]
    figure = plt.figure()
    axis = figure.gca()
    marker_size = 5 * (atan((10 - x_series.size) / 1000) + 1 / 5 + pi / 2)
    axis.scatter(x_series, y_series, s=marker_size)
    axis.grid()
    axis.set(xlabel=x_name, ylabel=y_name)
    axis.set(title=f"{y_name} vs. {x_name}")
    return figure


def correlation_plot(actual_name: str, predicted_name: str, *args, percent_bound=10):
    """correlation plot of actual vs. predicted values"""
    df = args[0]
    actual_series = df[actual_name]
    predicted_series = df[predicted_name]
    min_value = min([actual_series.min(), predicted_series.min()])
    max_value = max([actual_series.max(), predicted_series.max()])
    actual_range = actual_series.max() - actual_series.min()
    bound_diff = actual_range * percent_bound / 100
    figure = plt.figure()
    axis = figure.gca()
    min_max = [min_value, max_value]
    axis.plot(min_max, min_max, "g-")
    axis.plot(min_max, [min_value - bound_diff, max_value - bound_diff], "r--")
    axis.plot(min_max, [min_value + bound_diff, max_value + bound_diff], "r--")
    # marker_size = marker_size_calc(actual_series.size)
    axis.scatter(actual_series, predicted_series)  # , s=marker_size
    axis.grid()
    upper_label = f"+{percent_bound}% Actual Range"
    lower_label = f"-{percent_bound}% Actual Range"
    axis.legend(("100% Correlation", lower_label), upper_label, loc="best")
    axis.set(xlabel=actual_name, ylabel=predicted_name)
    axis.set(title=f"Predicted vs. Actual: {actual_name}")
    axis.set_xlim([min_value, max_value])
    axis.set_ylim([min_value, max_value])
    return figure


def correlation_heatmap(*args):
    """heatmap of dataframe correlation matrix"""
    df = args[0]
    df = df.drop(columns=["run name"])
    figure = plt.figure()
    axis = sns.heatmap(df.corr())
    figure.add_axes(axis)
    return figure


def pie_chart(x_name: str, color_dict: dict, *args):
    """create a pie chart with the middle cut out"""
    df = args[0]
    x_series = df[x_name]
    value_counts = x_series.value_counts()
    number_list = list(value_counts)
    label_list = list(value_counts.index)
    color_list = [color_dict[x_val] for x_val in label_list]

    figure = plt.figure()
    axis = figure.gca()
    axis.pie(
        number_list,
        labels=label_list,
        colors=color_list,
        autopct="%1.1f%%",
        pctdistance=0.8,
        wedgeprops={"linewidth": 8, "edgecolor": "white"},
    )
    # 0.85, 7, 0.7
    circle = plt.Circle((0, 0), 0.8, fc="white")
    axis.add_artist(circle)
    axis.set(title=x_name)
    return figure
