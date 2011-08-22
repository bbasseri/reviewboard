#!/usr/local/bin/python

import commands
import os
import platform
from subprocess import call
import sys
import time


def guide():
    return "To install MySQL bindings type 'easy_install pysqlite' "


def install():
    call(["easy_install", "pysqlite"])
