import commands
import os
import platform
from subprocess import call
import sys


def guide():
    return "To install Amazon S3 Storage type 'easy_install django-stotages' "\
           + "in the command prompt. "


def install():
    call(["easy_install", "django-storages"])
