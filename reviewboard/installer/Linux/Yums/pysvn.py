#!/usr/local/bin/python

import commands
import os
import platform
from subprocess import call
import sys
import time


def guide():
    return "To install Subversion type 'sudo yum install subversion pysvn' "


def install():
    call(["yum", "install", "subversion"])
    call(["yum", "install", "subversion", "pysvn"])
