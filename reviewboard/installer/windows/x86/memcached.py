import commands
from getunzipped import *
import os
import platform
from subprocess import call
import sys
import urllib
import zipfile


def guide():
    return "To install Memchached Download the file from the web. " \
           + "Extract to a folder, then run 'memcached.exe /a -d installtype'"\
           + " using cmd in that folder. After installation " \
           + "run 'easy_install python-memcached' for python dependencies."


def install():
    package_name = "memcached-1.2.6-win32-bin"
    archive_url = "http://code.jellycan.com/files/" + package_name
    dl_dir = "C:\\ReviewBoard\\Memcached"
    get_unzipped(archive_url, dl_dir)
    call([dl_dir + "\memcached.exe", "/a", "-d", "install"])
    call(["easy_install", "python-memcached"])
    print "installation done"
