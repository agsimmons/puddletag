# -*- coding: utf-8 -*-
import os
from os.path import dirname

version_string = '2.0.0'
version = (2, 0, 0)
changeset = None

filedir = dirname(dirname(dirname(__file__)))
hash_file = os.path.join(filedir, '.git/refs/heads/master')
if os.path.exists(hash_file):
    try:
        with open(hash_file) as fo:
            changeset = fo.read().strip()
    except (EnvironmentError, AttributeError):
        pass
