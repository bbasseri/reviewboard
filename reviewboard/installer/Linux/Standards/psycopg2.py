#!/usr/local/bin/python

import commands
import os
import platform
from subprocess import call
import sys
import time


def guide():
    return "To install Postgresql bindings type 'easy_install psycopg2' "


def install():
    call(["easy_install", "psycopg2"])
