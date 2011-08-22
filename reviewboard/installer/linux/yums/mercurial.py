#!/usr/local/bin/python

import commands
import os
import platform
from subprocess import call
import sys
import time


def guide():
    return "To install Mercurial type 'easy_install mercurial' "


def install():
    call(["easy_install", "mercurial"])
