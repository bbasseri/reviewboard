#!/usr/local/bin/python

import commands
import os
import platform
from subprocess import call
import sys
import time


def guide():
    return "To install Sphinx type 'easy_install sphinx' "


def install():
    call(["easy_install", "sphinx"])
