#!/usr/bin/env python

import os
import readline
from pprint import pprint

from flask import *
from application import *
from application.default_settings import _basedir


os.environ['PYTHONINSPECT'] = 'True'

# Create database directory if not exists.
create_db_dir = _basedir + '/db'
if not os.path.exists(create_db_dir):
    os.mkdir(create_db_dir, 0755)
