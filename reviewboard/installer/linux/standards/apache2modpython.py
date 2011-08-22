#!/usr/local/bin/python

import commands
import os
import platform
from subprocess import call
import sys
import time


def guide():
    return "To install mod_python for apache type "\
    + "'sudo apt-get install libapache2-mod-python' "


def install():
    call(["sudo", "apt-get", "install", "libapache2-mod-python"])
