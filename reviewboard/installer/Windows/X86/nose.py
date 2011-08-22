import commands
import os
import platform
from subprocess import call
import sys


def guide():
    print "To install Nose, type 'easy_install nose' in cmd."


def install():
    call(["easy_install", "nose"])
