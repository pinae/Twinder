#!/usr/bin/python
# -*- coding: utf-8 -*-

import os


TWINDER_DIR = os.path.dirname(os.path.expanduser("~/.twinder/"))
if not os.path.exists(TWINDER_DIR):
    os.makedirs(TWINDER_DIR)

