#!/usr/local/bin/python

import commands
import os
import platform
from subprocess import call
import sys
import time


def guide():
    return "To install Git type 'sudo yum install git-core' "


def install():
    call(["yum", "install", "git-core"])
