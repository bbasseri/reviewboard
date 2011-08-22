import commands
from download import*
import os
import platform
from setpath import *
from subprocess import call
import sys
import urllib
import win32api
import win32con


def guide():
    return "Donwload the file from " \
    + "http://downloads.sourceforge.net/project/gnuwin32/patch/2.5.9-7/" \
    + "patch-2.5.9-7-setup.exe?r=http%3A%2F%2Fsourceforge.net%2Fproject" \
    + "%2Fdownloading.php%3Fgroupname%3Dgnuwin32%26file_name%3Dpatch-2." \
    + "5.9-7-setup.exe%26use_mirror%3Dsurfnet&ts=1308215304&use_mirror=" \
    + "cdnetworks-us-1 . Install the file then " \
    + "add the path.exe from the installed folder to the path" \
    + "(Usually in ProgramFiles/GNUWin32\bin"


def install():
    if platform.architecture()[0] == '32bit':
        path = "C:\\Program Files\\GnuWin32\\"
    else:
        path = "C:\\Program Files (x86)\\GnuWin32\\"
    file_name = "patch-2.5.9-7-setup.exe"
    url = \
    "http://downloads.sourceforge.net/project/gnuwin32/patch/2.5.9-7/" \
    + "patch-2.5.9-7-setup.exe?r=http%3A%2F%2Fsourceforge.net%2Fproject" \
    + "%2Fdownloading.php%3Fgroupname%3Dgnuwin32%26file_name%3Dpatch-2." \
    + "5.9-7-setup.exe%26use_mirror%3Dsurfnet&ts=1308215304&use_mirror=" \
    + "cdnetworks-us-1"
    dl_dir = "C:\\ReviewBoard\\Downloads"
    download(url, dl_dir, file_name)
    call([dl_dir + "\\" + file_name, "/silent"])
    setPath(path)
