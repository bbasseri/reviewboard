#!/usr/local/bin/python

import commands
import os
import platform
from subprocess import call
import sys
import time


def guide():
    return "To install Amazon S3 Storage type 'easy_install django-stotages' "


def install():
    call(["easy_install", "django-storages"])
