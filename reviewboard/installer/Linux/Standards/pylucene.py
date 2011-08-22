#!/usr/local/bin/python

import commands
import os
import platform
from subprocess import call
import sys
import time


def guide():
    return "To install Pylucene type 'sudo apt-get install pylucene' "


def install():
    call(["apt-get", "install", "subversion", "pylucene"])
