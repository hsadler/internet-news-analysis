#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os


try:
    user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
except KeyError:
    user_paths = []

print user_paths
