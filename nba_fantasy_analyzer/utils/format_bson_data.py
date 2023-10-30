import bson
import copy
from decimal import Decimal
from bson.decimal128 import Decimal128
from uuid import UUID


def format_to_bson(dict_item: dict) -> dict:
    # This function formats a json-formated data to a bson
    # Embedded dictionaries and lists are called recursively.
    if not dict_item:
        return None

    if not isinstance(dict_item, dict):
        return apply_bson_rules(dict_item)

    new_dict = copy.copy(dict_item)
    for k, v in list(new_dict.items()):
        if isinstance(v, dict):
            format_to_bson(v)
        elif isinstance(v, list):
            for item in v:
                format_to_bson(item)
        new_dict[k] = apply_bson_rules(v)

    return new_dict


def apply_bson_rules(value):
    if isinstance(value, Decimal):
        value = Decimal128(str(value))
    elif isinstance(value, UUID):
        value = bson.Binary.from_uuid(value)

    return value


def format_to_json(dict_item: dict) -> dict:
    # This function formats a bson-formated data to a json
    # Embedded dictionaries and lists are called recursively.
    if not dict_item:
        return None

    if not isinstance(dict_item, dict):
        return apply_bson_rules(dict_item)

    new_dict = copy.copy(dict_item)
    for k, v in list(new_dict.items()):
        if isinstance(v, dict):
            format_to_bson(v)
        elif isinstance(v, list):
            for item in v:
                format_to_bson(item)
        new_dict[k] = apply_json_rules(v)

    return new_dict


def apply_json_rules(value):
    if isinstance(value, Decimal128):
        value = Decimal(str(value))
    elif isinstance(value, bson.Binary):
        value = bson.Binary.as_uuid(value)
    elif isinstance(value, bson.ObjectId):
        value = str(value)

    return value
