#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging


def port_in_range(port_number: int) -> bool:
    """Checks if the port is within the valid range
       from 0 to 65536."""

    if isinstance(port_number, int):
        if port_number >= 0 and port_number < 65536:
            logging.debug('Port within range')
            return True
        else:
            logging.error('Port not within valid ' +
                          'range from 0 to 65536')
            return False
    else:
        raise ValueError('Port has to be an integer.')
