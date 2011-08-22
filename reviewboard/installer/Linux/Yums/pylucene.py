#!/usr/local/bin/python

import commands
import os
import platform
from subprocess import call
import sys
import time


def guide():
    return "To install Pylucene type 'sudo yum install pylucene' "


def install():
    call(["yum", "install", "subversion", "pylucene"])
