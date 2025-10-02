"""put QSS styles here"""

WINDOW_TITLE = """
font: 22px;
margin: 2px;
"""

ICONBAR = """
spacing:0px;
height:40px;
width:40px
"""

SEARCHBAR = """
font:18px;
"""

SEARCHBAR_WIDTH_MIN = 80
SEARCHBAR_WIDTH_MAX = 300

MENUBUTTON = """
font:24px;
padding: 6px;
background-color:transparent;
"""

MENUITEMS = """
font: 18px;
padding: 2px;
"""

TABBAR = """
QTabBar{
    font: 24px;
    border-bottom:0px;
}
"""  # background:#3B3838;
# QTabBar:tab:selected{padding-left:12;padding-right:12;border-radius:2}

TOOLBAR_HEIGHT = 100

TOOLBAR = f"""
spacing:10px;
padding:10px;
height:{TOOLBAR_HEIGHT-20}px;
width:80px;
font:14px;
"""  # background-color:#3B3838;

TOOLBAR_BUTTON = """
QToolButton{
    background-color:#002060;
    color:white;
    border:0.5 solid gray;
    border-radius:4;
}
QToolButton:hover{
    background-color:#00639A;
    border-color:#33B6FF;
}
"""
