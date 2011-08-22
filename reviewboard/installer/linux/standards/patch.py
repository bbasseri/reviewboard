#!/usr/local/bin/python

import commands
import os
import platform
from subprocess import call
import sys
import time


def guide():
    return "To install Patch type 'sudo apt-get install patch' "


def install():
    call(["apt-get", "install", "patch"])
