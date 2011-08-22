#!/usr/local/bin/python

import commands
import os
import platform
from subprocess import call
import sys
import time


def guide():
    return "To install Memchached type 'sudo yum install memcached' "


def install():
    call(["yum", "install", "memcached"])
    call(["easy_install", "python-memcached"])
