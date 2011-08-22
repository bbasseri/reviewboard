#!/usr/local/bin/python

import commands
import os
import platform
from subprocess import call
import sys
import time


def guide():
    return "To install wsgi for apache type "\
    + "'sudo apt-get install libapache2-mod-wsgi' "


def install():
    call(["sudo", "apt-get", "install", "libapache2-mod-wsgi"])
