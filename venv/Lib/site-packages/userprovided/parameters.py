#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from typing import Optional, Union


def convert_to_set(convert_this: Union[list, set, str, tuple]) -> set:
    """ Convert a string, a tuple, or a list into a set
        (i.e. no duplicates, unordered)"""

    if isinstance(convert_this, set):
        # functions using this expect a set, so everything
        # else just captures bad input by users
        new_set = convert_this
    elif isinstance(convert_this, str):
        new_set = {convert_this}
    elif isinstance(convert_this, list):
        new_set = set(convert_this)
    elif isinstance(convert_this, tuple):
        new_set = set(convert_this)
    else:
        raise TypeError('The function calling this expects a set.')

    return new_set


def validate_dict_keys(dict_to_check: dict,
                       allowed_keys: set,
                       necessary_keys: Optional[set] = None,
                       dict_name: Optional[str] = None) -> bool:
    """If you use dictionaries to pass parameters, there are two common errors:
       * misspelled keys
       * necessary keys are missing
       This functions checks whether all keys are in the set of allowed_keys
       and raises ValueError if a unknown key is found.
       It can also check whether all necessary keys are present and
       raises ValueError if not.
       dict_name can be used for a better error message."""

    if not dict_name:
        # fallback to neutral
        dict_name = 'dictionary'

    # In case something other than a set is provided:
    allowed_keys = convert_to_set(allowed_keys)

    if necessary_keys:
        # also make sure it is a set:
        necessary_keys = convert_to_set(necessary_keys)
        # Are all necessary keys in the allowed key list?
        if len(necessary_keys - allowed_keys) != 0:
            msg = ("Contradiction: Not all necessary keys " +
                   "are in the allowed keys set!")
            logging.exception(msg)
            raise ValueError(msg)

    # Get all keys in the dictionary:
    try:
        found_keys = dict_to_check.keys()
    except AttributeError:
        raise AttributeError('Expected a dictionary for ' +
                             'the dict_to_check parameter!')

    # Check for unknown keys:
    for key in found_keys:
        if key not in allowed_keys:
            msg = f"Unknown key {key} in {dict_name}"
            logging.exception(msg)
            raise ValueError(msg)
    logging.debug('No unknown keys found.')

    # Check if all necessary keys are present:
    if necessary_keys:
        for key in necessary_keys:
            if key not in found_keys:
                msg = f"Necessary key {key} missing in {dict_name}!"
                logging.exception(msg)
                raise ValueError(msg)
        logging.debug('All necessary keys found.')

    return True


def numeric_in_range(parameter_name: str,
                     given_value: Union[int, float],
                     minimum_value: Union[int, float],
                     maximum_value: Union[int, float],
                     fallback_value: Union[int, float]
                     ) -> Union[int, float]:
    """Checks if a numeric value is within a specified range.
       If not this returns the fallback value and logs a warning."""
    if not parameter_name:
        parameter_name = ''

    for param in {given_value, minimum_value, maximum_value, fallback_value}:
        if not isinstance(param, (int, float)):
            raise ValueError('Value must be numeric.')

    if minimum_value > maximum_value:
        raise ValueError("Minimum must not be larger than maximum value.")

    if fallback_value < minimum_value or fallback_value > maximum_value:
        raise ValueError("Fallback value outside the allowed range.")

    if given_value < minimum_value:
        msg = (f"Value of {parameter_name} is below the minimum allowed." +
               f"Falling back to {fallback_value}.")
        logging.warning(msg)
        return fallback_value

    if given_value > maximum_value:
        msg = (f"Value of {parameter_name} is above the maximum allowed." +
               f"Falling back to {fallback_value}.")
        logging.warning(msg)
        return fallback_value

    # passed all checks:
    return given_value


def int_in_range(parameter_name: str,
                 given_value: int,
                 minimum_value: int,
                 maximum_value: int,
                 fallback_value: int) -> int:
    """Special case of numeric_in_range: check if given integer is
       within a specified range of possible values."""
    for param in {given_value, minimum_value, maximum_value, fallback_value}:
        if type(param) != int:
            raise ValueError('Value must be an integer.')
    return int(numeric_in_range(parameter_name,
                                given_value,
                                minimum_value,
                                maximum_value,
                                fallback_value))


def string_in_range(string_to_check: str,
                    minimum_length: int,
                    maximum_lenght: int,
                    strip_string: bool = True) -> bool:
    """Strips whitespace from both ends of a string and then checks
       if the length of that string falls in those limits.
       The strip() can be turned off. """

    if minimum_length > maximum_lenght:
        raise ValueError("Minimum must not be larger than maximum value.")
    enforce_boolean(strip_string)

    if strip_string:
        string_to_check = string_to_check.strip()
    if len(string_to_check) < minimum_length:
        logging.info("String length below minimum length.")
        return False
    if len(string_to_check) > maximum_lenght:
        logging.info("String longer than maximum.")
        return False
    return True


def enforce_boolean(parameter_value: bool,
                    parameter_name: Optional[str] = None) -> None:
    """Raise a ValueError if the parameter is not of type bool."""
    if type(parameter_value) != bool:
        parameter_name = 'parameter' if parameter_name else ''
        raise ValueError(f"Value of {parameter_name} must be boolean," +
                         "i.e True / False (without quotation marks).")
