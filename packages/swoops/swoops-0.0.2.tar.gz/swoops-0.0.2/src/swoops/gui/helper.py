"""
Written by Jason Krist
05/01/2024
"""

from os import path
from typing import Any, get_args, Union
from math import floor, log10
import json
import pickle
import tomli
import tomli_w
from pandas import DataFrame  # pylint: disable=E0611,E0401

try:
    import swoops.constants as CONS  # type: ignore
except ModuleNotFoundError:
    from .. import constants as CONS  # type: ignore # pylint: disable=E0611,E0401

# use dict.get(key,default)


def obj_to_dict(obj: Any) -> Any:
    """Recursively turn an object into a nested dictionary
    Args:
        obj (Any): Instance of a class
    Returns:
        dict: object converted to dict
    """
    out_dict = {}
    if isinstance(obj, dict):
        obj_dict = obj
    elif isinstance(obj, DataFrame):
        # return CONS.CSV_HEADER+"\n"+obj.to_csv()
        df_dict_list = {str(key): value for key, value in obj.T.to_dict("list").items()}
        df_dict = {"columns": list(obj.columns), "list": df_dict_list}
        return df_dict
    elif not hasattr(obj, "__dict__"):
        return obj
    else:
        out_dict[CONS.CLASS] = obj.__class__.__name__
        obj_dict = obj.__dict__
    for key, value in obj_dict.items():
        key_str = str(key)
        if value is None:
            continue
        if callable(value):
            continue
        if isinstance(value, (list, tuple, dict)) and not value:
            continue  # Don't include empty lists, tuples, or dictionaries
        if key == CONS.TYPE:
            value = value.value
        out_dict[key_str] = obj_to_dict(value)
    return out_dict


def save_obj(obj: Any, filepath: str) -> None:
    """Save an object as a custom file format
    Args:
        obj (Any): arbitrary nested object
        filepath (str): path to save object as file
    """
    _base, ext = path.splitext(filepath)
    if ext == ".toml":
        obj_dict = obj_to_dict(obj)
        with open(filepath, "wb") as file:
            tomli_w.dump(obj_dict, file)
    elif ext == ".json":
        obj_dict = obj_to_dict(obj)
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file, indent=4)
    elif ext == ".pickle":
        with open(filepath, "wb") as file:
            pickle.dump(obj, file, protocol=pickle.HIGHEST_PROTOCOL)
    else:
        raise ValueError(f'File Type "{ext}" is not supported for saving.')


def read_obj(filepath: str, dict_to_obj_call, obj):
    """read a TOML, JSON, or PKL file to a dictionary"""
    _base, ext = path.splitext(filepath)
    if ext == ".toml":
        with open(filepath, "rb") as file:
            obj_dict = tomli.load(file)
            dict_to_obj_call(obj, obj_dict)
    elif ext == ".json":
        with open(filepath, "r", encoding="utf-8") as file:
            obj_dict = json.load(file)
            dict_to_obj_call(obj, obj_dict)
    elif ext == ".pickle":
        with open(filepath, "rb") as file:
            obj = pickle.load(file)
    else:
        raise ValueError(f'File Type "{ext}" is not supported for saving.')
    return obj


def dict_to_df(dictionary: dict[int, object]) -> DataFrame:
    """convert dictionary to pandas dataframe"""
    values = list(dictionary.values())
    if not values:
        return DataFrame()
    obj_dict = obj_to_dict(values[0])
    columns = [k for k in obj_dict if k != CONS.CLASS]
    newdict = {}
    for key, obj in dictionary.items():
        obj_dict = obj_to_dict(obj)
        newdict[key] = [val for k, val in obj_dict.items() if k != CONS.CLASS]
    df = DataFrame.from_dict(newdict, orient="index", columns=columns)
    return df


def clean_colnames(colnames: list[str]) -> list[str]:
    """make column names look nicer for Visualization"""
    newcolnames = []
    for col in colnames:
        if col.startswith("_"):
            col = col[1:]
        col = title(col)
        newcolnames.append(col)
    return newcolnames


def unclean_colnames(colnames: list[str]) -> list[str]:
    """make column names look nicer for Visualization"""
    newcolnames = []
    for col in colnames:
        if col == title(CONS.ID):
            col = CONS.ID
        elif col == title(CONS.TYPE[1:]):
            col = CONS.TYPE
        else:
            col = lower(col)
        newcolnames.append(col)
    return newcolnames


def find_by_key(dictionary: dict, key: int) -> Any:
    """Find a dictionary value by a key value id

    Args:
        dictionary (dict): dict with integer keys
        key (int): key to search within dict

    Raises:
        ValueError: if key does not exist

    Returns:
        Any: dict value at the specified key value
    """
    if len(dictionary) == 0:
        raise ValueError("Dictionary has length = 0.")
    for key_id, val in dictionary.items():
        if key_id == key:
            return val
    classname = val.__class__.__name__  # pylint: disable=W0631
    raise ValueError(f"{classname} with id={key} does not exist.")


def next_id(dictionary: dict) -> int:
    """Get the next ID to use in a sorted dict

    Args:
        dictionary (dict): dictionary with integer keys in ascending order

    Returns:
        int: next integer ID to use
    """
    if not list(dictionary):
        return 1
    return list(dictionary)[-1] + 1


def round_sigfig(num: int | float, sigfig: int) -> float:
    """Round a number to a max number of significant figures
    Args:
        num (int | float): number to round
        sigfig (int): max significant figures

    Returns:
        float: number after rounding
    """
    if num == 0:
        return 0
    return round(num, sigfig - int(floor(log10(abs(num)))) - 1)


def list_length_check(lists: list[list], names: list[str]):
    """check that the length of all input lists is equal to one another"""
    lens = [len(sublist) for sublist in lists]
    if not all(i == lens[0] for i in lens):
        list_str = "".join([f"    {names[i]}: {lens[i]}\n" for i in range(len(lens))])
        err_str = f"Length of lists does not match.\n{list_str}"
        raise ValueError(err_str)


def lower(string: str) -> str:
    """convert a string to lowercase and replace spaces with underscores"""
    string = string.replace(" ", "_")
    return string.lower()


def title(string: str) -> str:
    """convert a string to title-case and replace underscores with spaces"""
    string = string.title()
    string = string.replace("id", "ID")
    string = string.replace("Id", "ID")
    string = string.replace("iD", "ID")
    return string.replace("_", " ")


def plural(string: str) -> str:
    """make a string plural"""
    if string.endswith("y"):
        string = string[0:-1] + "ies"
    elif string.lower() == "analysis":
        string = string[:-2] + "es"
    elif not string.endswith("s"):
        string = string + "s"
    return string


def singular(string: str) -> str:
    """make a string singular"""
    if string.endswith("ies"):
        string = string[0:-3] + "y"
    elif string.lower() == "analyses":
        string = string[:-2] + "is"
    elif string.lower() == "analysis":
        return string
    elif string.endswith("s"):
        string = string[0:-1]
    return string


def attr_name(string: str) -> str:
    """attribute names are always plural and lower"""
    return lower(plural(string))

def class_name(string: str) -> str:
    """class names are always titled and singular"""
    return title(singular(string))

def literal_check(value: Any, literal: object):
    """check if value is in literal"""
    literal_tuple = get_args(literal)
    if value in literal_tuple:
        return
    raise ValueError(f'Value "{value}" is not in literal "{literal_tuple}"')


def getnested(iterable: Union[list, tuple], index) -> list:
    """get list of items at index of a nested list or tuple"""
    return [item[index] for item in iterable]

def list_to_str(lst, sep=",", bracket=True):
    """convert list to string"""
    lst = [str(item) for item in lst]
    if bracket:
        return f"[{sep.join(lst)}]"
    return sep.join(lst)

def str_to_list(string, sep=","):
    """convert list to string"""
    string = string.strip("[").strip("]")
    splitstr = string.split(sep)
    if len(splitstr[0]) > 0 or len(splitstr) > 1:
        return splitstr
    return []

def liststr(obj: Union[list, str]) -> str:
    """convert list to string"""
    if isinstance(obj, list):
        obj = [str(item) for item in obj]
        return "[" + "; ".join(obj) + "]"
    return obj


def listify(item) -> list:
    """convert string or list to list"""
    if not isinstance(item, list | str):
        return item
    if isinstance(item, str):
        if any(["[" not in item, "]" not in item]):
            return item
        item = list(item.strip("[]").split(";"))
    if all([isinstance(val, str) for val in item]):
        if all([val.strip().isdigit() for val in item]):
            return [int(val.strip()) for val in item]
        return item
    return item


def dictify(item) -> dict:
    """convert string or list to dictionary"""
    if not isinstance(item, list | str):
        return item
    if isinstance(item, str):
        if any(["{" not in item, "}" not in item]):
            return item
        item = list(item.strip("{}").split(";"))
    item_dict = {}
    for listval in item:
        split = listval.split(":")
        key = split[0].strip('"').strip("'")
        val = ""
        if len(split) > 1:
            val = ":".join(split[1:])
            val = dictify(val)
        item_dict[key] = val
    return item_dict


def cast_type(new_obj, old_obj):
    """cast new object as type(old_obj)"""
    if isinstance(old_obj, bool):
        return bool(new_obj)
    elif isinstance(old_obj, int):
        return int(new_obj)
    elif isinstance(old_obj, float):
        return float(new_obj)
    elif isinstance(old_obj, str):
        return str(new_obj)
    elif isinstance(old_obj, dict):
        return dictify(new_obj)
    else:
        return listify(new_obj)


def first_key(dic: dict):
    """return first key in dictionary or -1"""
    if not dic:
        return None
    return list(dic)[0]


def last_key(dic: dict):
    """return first key in dictionary or -1"""
    if not dic:
        return None
    return list(dic)[-1]


def is_float(string: str) -> bool:
    """check if string can be converted to float"""
    try:
        float(string)
        return True
    except ValueError:
        return False
