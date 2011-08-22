#!/usr/local/bin/python

import commands
import os
import platform
from subprocess import call
import sys
import time


def guide():
    return "To install CVS type 'sudo yum install cvs' "


def install():
    call(["yum", "install", "cvs"])
