# -*- coding: utf8 -*-
# This file is part of PyBossa.
#
# Copyright (C) 2013 SF Isle of Man Limited
#
# PyBossa is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBossa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBossa.  If not, see <http://www.gnu.org/licenses/>.

#import os
#from glob import iglob
import logging
import datetime
#import time
import json
import uuid

from werkzeug import generate_password_hash, check_password_hash
import flask.ext.login
from sqlalchemy import BigInteger, Integer, Boolean, Unicode,\
        Float, UnicodeText, Text, String
from sqlalchemy.schema import Table, MetaData, Column, ForeignKey
from sqlalchemy.orm import relationship, backref, class_mapper
from sqlalchemy.types import MutableType, TypeDecorator
from sqlalchemy import event, text
from sqlalchemy.engine import reflection
from sqlalchemy import create_engine
from sqlalchemy.schema import (
    MetaData,
    Table,
    DropTable,
    ForeignKeyConstraint,
    DropConstraint,
    )

from pybossa.core import db
from pybossa.util import pretty_date

from app import App
from blogpost import Blogpost
from category import Category
from featured import Featured
from task import Task
from task_run import TaskRun
from user import User
from util import rebuild_db, make_uuid


log = logging.getLogger(__name__)


