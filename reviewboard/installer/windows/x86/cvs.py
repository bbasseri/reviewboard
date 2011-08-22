import commands
from getunzipped import *
import os
import platform
from setpath import *
from subprocess import call
from subprocess import Popen
import sys
import urllib
import win32api
import win32con
import zipfile


def guide():
    return "Download the installer from " \
    + "http://ftp.gnu.org/non-gnu/cvs/binary/stable/x86-woe/cvs-1-11-22.zip" \
    + "Unzip the file. Add the cvs.exe to the enviroment path"


def install():
    package_name = "cvs-1-11-22"
    archive_url = "http://ftp.gnu.org/non-gnu/cvs/binary/stable/x86-woe/" \
    + "cvs-1-11-22.zip"
    get_unzipped(archive_url, "C:\\ReviewBoard\\" + package_name)
    setPath("C:\\ReviewBoard\\" + package_name)
