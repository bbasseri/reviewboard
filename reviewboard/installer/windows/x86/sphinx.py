import commands
import os
import platform
from subprocess import call
import sys


def guide():
    print "To install Sphinx type 'easy_install sphinx' "


def install():
    call(["easy_install", "sphinx"])
