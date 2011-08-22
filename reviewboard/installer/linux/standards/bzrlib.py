#!/usr/local/bin/python

import commands
import os
import platform
from subprocess import call
import sys
import time


def guide():
    return "To install Bazar bindings type 'sudo apt-get install bzr' "


def install():
    call(["sudo", "apt-get", "install", "bzr"])
