#!/usr/local/bin/python

import commands
import os
import platform
from subprocess import call
import sys
import time


def guide():
    return "To install Perforce type 'easy_install P4PythonInstaller' "


def install():
    call(["easy_install", "P4PythonInstaller"])
