import commands
from download import *
import os
import platform
from subprocess import call
import sys
import urllib


def guide():
    return "To install Git download the installer from " \
        + "http://msysgit.googlecode.com/files/Git-1.7.6-preview20110708.exe" \
        + " Follow the onscreen instructions to install"


def install():
    file_name = "Git-1.7.6-preview20110708.exe"
    url = "http://msysgit.googlecode.com/files/" + file_name
    dl_dir = "C:\\ReviewBoard\\Downloads"
    download(url, dl_dir, file_name)
    call([dl_dir + "\\" + file_name, "/silent"])
