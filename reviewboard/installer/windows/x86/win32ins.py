import commands
from download import *
import os
import platform
import re
from subprocess import *
import sys
import urllib


def guide():
    print "Win32Api is required to be installed on your computer."


def install():
    dl_dir = "C:\\ReviewBoard\\Downloads\\"
    if platform.architecture()[0] == '32bit':
        bit = "win32"
    else:
        bit = "win-amd64"
    file_name = "pywin32-216." + bit + "-py" + str(sys.version_info[0]) \
    + "." + str(sys.version_info[1]) + ".exe"
    url = "http://sourceforge.net/projects/pywin32/files/pywin32/Build216/" \
    + file_name + "/download"
    download(url, dl_dir, file_name)
    subprocess.Popen([dl_dir + file_name, "/silent"]).wait()
