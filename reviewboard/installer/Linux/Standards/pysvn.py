#!/usr/local/bin/python

import commands
import os
import platform
from subprocess import call
import sys
import time


def guide():
    return "To install Subversion type "\
           + "'sudo apt-get install subversion python-svn'."


def install():
    call(["apt-get", "install", "subversion", "python-svn"])
