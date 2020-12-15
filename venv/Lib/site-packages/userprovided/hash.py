#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import logging
import pathlib
from typing import Union


def hash_available(hash_method: str,
                   fail_on_deprecated: bool = True) -> bool:
    """Checks if the supplied hashing algorithm is available.
       If fail_on_deprecated is set to True (default) it will raise an
       exception if the method is deprecated (md5 and sha1)."""

    if hash_method:
        hash_method = hash_method.strip()

    if hash_method == '' or hash_method is None:
        raise ValueError('No hash method provided')

    # Is the chosen method available and supported?
    hash_method = hash_method.strip()

    if fail_on_deprecated:
        if hash_method in ('md5', 'sha1'):
            raise ValueError('The supplied hash method %s is deprecated!')

    if hash_method in hashlib.algorithms_available:
        logging.debug('Hash method %s is available.', hash_method)
        return True
    else:
        return False


def calculate_file_hash(file_path: Union[pathlib.Path, str],
                        hash_method: str = 'sha256') -> str:
    """Calculate hash value for a file.
       Supported: SHA224 / SHA256 / SHA512"""

    if hash_method in ('md5', 'sha1'):
        raise NotImplementedError('Deprecated hash method not supported')

    if hash_available(hash_method):
        if hash_method == 'sha224':
            h = hashlib.sha224()
        elif hash_method == 'sha256':
            h = hashlib.sha256()
        elif hash_method == 'sha512':
            h = hashlib.sha512()
        else:
            raise ValueError('Hash method not supported')
    else:
        raise ValueError(f"Hash method {hash_method} not available on system.")

    try:
        with open(pathlib.Path(file_path), 'rb') as file:
            content = file.read()
        h.update(content)
        return h.hexdigest()
    except FileNotFoundError:
        logging.error('Cannot calculate hash: File not found or not readable.',
                      exc_info=True)
        raise
    except Exception:
        logging.error('Exception while trying to get file hash',
                      exc_info=True)
        raise
