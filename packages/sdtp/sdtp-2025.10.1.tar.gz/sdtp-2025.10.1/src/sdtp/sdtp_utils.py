'''
Constants and utilities for the Simple Data Transfer Protocol
'''

# BSD 3-Clause License
# Copyright (c) 2024-2025, The Regents of the University of California (Regents)
# All rights reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import json
import datetime
import functools
import pandas as pd
from sdtp import type_check, SDML_PYTHON_TYPES


def json_serialize(obj):
    # Convert dates, times, and datetimes to isostrings 
    # for json serialization
    if isinstance(obj, (datetime.datetime, datetime.date, datetime.time)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")



def check_sdml_type_of_list(sdml_type, list_of_values):
    '''
    Check to make sure the values in list_of_values are all the right Python 
    type for operations.
    Arguments:
        sdml_type: One of SDML_SCHEMA_TYPES
        list_of_values: a Python list to be tested
    '''
    type_check_list = [type_check(sdml_type, val) for val in list_of_values]
    return not (False in type_check_list)
    

'''
Exceptions for the Simple Data Transfer Protocol
'''



class InvalidDataException(Exception):
    '''
    An exception thrown when a data table (list of rows) doesn't match an accoompanying schema,
     or a bad schema is specified, or a table row is the wrong length, or..
    '''

    def __init__(self, message):
        super().__init__(message)
        self.message = message

NON_JSONIFIABLE_TYPES = {"date", "timeofday", "datetime"}

def jsonifiable_value(value, column_type):
    '''
    Python doesn't jsonify dates, datetimes, or times properly, so
    convert them to isoformat strings.  Return everything else as is
    Arguments:
        value -- the value to be converted
        column_type -- the SDTP type of the value
    Returns
        A jsonifiable form of the value
    '''
    if column_type in NON_JSONIFIABLE_TYPES:
        return value.isoformat()
    else:
        return value

def jsonifiable_row(row, column_types):
    '''
    IReturn the jsonified form of the row, using jsonifiable_value for each element
    Arguments:
        row -- the row to be converted
        column_types -- the types of each element of the row
    Returns
        A row of jsonifiable values
    '''
    return [jsonifiable_value(row[i], column_types[i]) for i in range(len(row))]


def jsonifiable_rows(rows, column_types):
    '''
    Return the jsonifiable form of the list of rows, using jasonifiable_row for each row
    Arguments:
        rows -- the list of rows to be converted
        column_types -- the types of each element of the row
    Returns
        A list of rows  of jsonified values
    '''
    return [jsonifiable_row(row, column_types) for row in rows]


def jsonifiable_column(column, column_type):
    '''
    Return a jsonifiable version of the column of values, using jsonifiable_value
    to do the conversion.  We actually cheat a little, only calling _jsonifiable_value if column_type
    is one of SDML_TIME, "date", "datetime"
    '''
    if column_type in NON_JSONIFIABLE_TYPES:
        return [jsonifiable_value(value, column_type) for value in column]
    else:
        return column
    
def _convert_to_number(value):
    # Return a numeric form of value, if possible, or throw an InValidDataException if it won't convert
    if isinstance(value, int) or isinstance(value, float):
        return value

    # try an automated conversion to float.  If it fails, it still
    # might be an int in base 2, 8, or 16, so pass the error to try
    # all of those

    try:
        return float(value)
    except (ValueError, TypeError):
        pass
    # if we get here, it must be a string or won't convert
    if not isinstance(value, str):
        raise InvalidDataException(f'Cannot convert {value} to number')

    # Try to convert to binary, octal, decimal

    for base in [2, 8, 16]:
        try:
            return int(value, base)
        except ValueError:
            pass
    # Everything has failed, so toss the exception
    raise InvalidDataException(f'Cannot convert {value} to number')


def convert_to_type(sdml_type, value):
    '''
    Convert value to sdml_type, so that comparisons can be done.  This is used to convert
    the values in a filter_spec to a form that can be used in a filter.
    Throws an InvalidDataException if the type can't be converted.
    An exception is Boolean, where "True, true, t" are all converted to True, but any
    other values are converted to False

    Arguments:
        sdml_type (str): type to convert to
        value (Any): value to be converted
    Returns:
        value cast to the correct type
    '''
    if type(value) in SDML_PYTHON_TYPES[sdml_type]:
        return value
    if sdml_type == "string":
        if isinstance(value, str):
            return value
        try:
            return str(value)
        except ValueError:
            raise InvalidDataException('Cannot convert value to string')
    elif sdml_type == "number":
        return _convert_to_number(value)
    elif sdml_type == "boolean":
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            return value in {'True', 'true', 't', '1', '1.0'}
        if isinstance(value, int):
            return value != 0
        if isinstance(value, float):
            return value != 0.0
        return False
    # Everything else is a date or time

    elif sdml_type == "datetime":
        if type(value) == datetime.date:
            return datetime.datetime(value.year, value.month, value.day, 0, 0, 0)
        if isinstance(value, str):
            try:
                return datetime.datetime.fromisoformat(value)
            except Exception:
                raise InvalidDataException(f"Can't convert {value} to datetime")
        raise InvalidDataException(f"Can't convert {value} to datetime")

    elif sdml_type == "date":
        if type(value) in SDML_PYTHON_TYPES["datetime"]:
            return value.date()
        if isinstance(value, str):
            try:
                return datetime.datetime.fromisoformat(value).date()
            except Exception:
                raise InvalidDataException(f"Can't convert {value} to date")
        raise InvalidDataException(f"Can't convert {value} to date")
    
    elif sdml_type == "timeofday":
        if type(value) in SDML_PYTHON_TYPES["datetime"]:
            return value.time()
        if isinstance(value, str):
            try:
                return datetime.time.fromisoformat(value)
            except Exception:
                try:
                    return datetime.datetime.fromisoformat(value).time()
                except Exception:
                    raise InvalidDataException(f"Can't convert {value} to time")

        raise InvalidDataException(f"Couldn't convert {value} to {sdml_type}")
    
    raise InvalidDataException(f"Don't recognize {sdml_type}")
        
def convert_list_to_type(sdml_type, value_list):
    '''
    Convert value_list to sdml_type, so that comparisons can be done.  Currently only works for lists of string, number, and boolean.
    Returns a default value if value can't be converted
    Note that it's the responsibility of the object which provides the rows to always provide the correct types,
    so this really should always just return a new copy of value_list
    Arguments:
        sdml_type: type to convert to
        value_list: list of values to be converted
    Returns:
        value_list with each element cast to the correct type
    '''
    try:
        return  [convert_to_type(sdml_type, elem) for elem in value_list]
        
        # result = []
        # for i in range(len(value_list)): result.append(convert_to_type(sdml_type, value_list[i]))
        # return result
    except Exception as exc:
        raise InvalidDataException(f'Failed to convert {value_list} to {sdml_type}')
    
def convert_row_to_type_list(sdml_type_list, row):
    # called from convert_rows_to_type_list, which should error check
    # to make sure that the row is the same length as sdml_type_list
    return [convert_to_type(sdml_type_list[i], row[i]) for i in range(len(row))]


def convert_rows_to_type_list(sdml_type_list, rows):
    '''
    Convert the list of rows to the 
    '''
    length = len(sdml_type_list)
    

    for row in rows:
        # print("convert_rows_to_type_list received types:", sdml_type_list)
        # print("Row:", row)
        # print("Expected length:", length, "Actual length:", len(row))

        if len(row) != length:
            raise InvalidDataException(f'Length mismatch: required number of columns {length}, length {row} = {len(row)}')
    return  [convert_row_to_type_list(sdml_type_list, row) for row in rows]
    
def convert_dict_to_type(sdml_type, value_dict):
    '''
    Convert value_dict to sdml_type, so that comparisons can be done.  Currently only works for lists of string, number, and boolean.

    Returns a default value if value can't be converted
    Note that it's the responsibility of the object which provides the rows to always provide the correct types,
    so this really should always just return a new copy of value_list
    Arguments:
        sdml_type: type to convert to
        value_dict: dictionary of values to be converted
    Returns:
        value_dict with each value in the dictionary cast to the correct type
    '''
    result = {}
    try:
        for (key, value) in value_dict.items():
            result[key] = convert_to_type(sdml_type, value)
        return result
    except Exception as exc:
        raise InvalidDataException(f'Failed to convert {value_dict} to {sdml_type}')

#
# Classes and methods to support authentication for RemoteSDMLTables and the sdtp
# client.
#
from typing import TypedDict, Union, Optional
import os

class EnvAuthMethod(TypedDict):
    '''
    The authentication token is in an the environment variable env
    '''
    env: str

class PathAuthMethod(TypedDict):
    '''
    The authentication token is in the file at path
    '''
    path: str

class ValueAuthMethod(TypedDict):
    '''
    The authentication token is the value
    '''
    value: str

AuthMethod = Union[EnvAuthMethod, PathAuthMethod, ValueAuthMethod]

def resolve_auth_method(method: AuthMethod) -> Optional[str]:
    """
    Resolve an AuthMethod dict to a credential string.
    Returns None if the method can't be satisfied (env var/file missing, etc.).
    """
    if "env" in method:
        return os.environ.get(method["env"])
    elif "path" in method:
        try:
            with open(os.path.expanduser(method["path"]), "r") as f:
                return f.read().strip()
        except Exception:
            return None
    elif "value" in method:
        return method["value"]
    return None
