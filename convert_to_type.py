import ast
import json


def type_conversion(value = ""):
    """
    Convert a String to its Correct Type using the Builtin Json Package.
    :param value:
    :return:
    """
    try:
        value = "false" if value == "False" else "true" if value == "True" else value
        return json.loads(value)
    except ValueError:
        return value


def adv_type_conversion(value = ""):
    """
    Convert a String to its Correct Type using the Builtin ast Package.
    :param value:
    :return:
    """
    try:
        value = "False" if value == "false" else "True" if value == "true" else value
        return ast.literal_eval(value)
    except ValueError:
        return value


def types_conversion(values = list):
    """
    Convert a List of Values to there Correct Types using the Builtin Json Package.
    :param values:
    :return:
    """
    for value in values:
        try:
            value = "false" if value == "False" else "true" if value == "True" else value
            yield json.loads(value)
        except ValueError:
            yield value


def adv_types_conversion(values = list):
    """
    Convert a List of Values to there Correct Types using the Builtin ast Package.
    :param values:
    :return:
    """
    for value in values:
        try:
            value = "False" if value == "false" else "True" if value == "true" else value
            yield ast.literal_eval(value)
        except ValueError:
            yield value
