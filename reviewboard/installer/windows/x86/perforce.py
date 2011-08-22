import commands
from download import *
import os
import platform
from setpath import *
from subprocess import call
import sys
import urllib
import win32api
import win32con


def guide():
    return "To install Perforce download the file from " \
    + "http://www.perforce.com/downloads/perforce/r10.2/bin.ntx86/"\
    + "perforce.exe"\
    + " Install perforce.exe, add p4.exe from the installed location to "\
    + "the path."


def install():
    if platform.architecture()[0] == '32bit':
        path = "C:\\Program Files\\Perforce\\"
    else:
        path = "C:\\Program Files (x86)\\Perforce\\"
    file_name = "perforce.exe"
    url = \
    "http://www.perforce.com/downloads/perforce/r10.2/bin.ntx86/perforce.exe"
    dl_dir = "C:\\ReviewBoard\\Downloads"
    download(url, dl_dir, file_name)
    call(["C:\ReviewBoard\Downloads\perforce.exe", "/S", "/v", "/qn"])
    setPath(path)
