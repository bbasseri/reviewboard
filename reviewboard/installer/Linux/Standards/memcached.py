#!/usr/local/bin/python

import commands
import os
import platform
from subprocess import call
import sys
import time


def guide():
    return "To install Memchached type 'sudo apt-get install memcached'."\
           + " Then type 'easy_install python-memcached' for dependencies "


def install():
    call(["apt-get", "install", "memcached"])
    call(["easy_install", "python-memcached"])
