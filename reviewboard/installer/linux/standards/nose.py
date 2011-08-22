#!/usr/local/bin/python

import commands
import os
import platform
from subprocess import call
import sys
import time


def guide():
    return "To install Nose 'easy_install nose' "


def install():
    call(["easy_install", "nose"])
