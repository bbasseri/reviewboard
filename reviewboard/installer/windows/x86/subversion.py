import commands
from download import *
import os
import platform
from subprocess import call
import sys
import urllib

url = "http://www.sliksvn.com/pub/Slik-Subversion-1.6.17-win32.msi"
file_name = "Slik-Subversion-1.6.17-win32.msi"


def guide():
    return "To install Subversion download it from " + url \
           + ". Run the installer and follow the onscreen instructions."


def install():
    dl_dir = "C:\\ReviewBoard\\Downloads"
    download(url, dl_dir, file_name)
    call(["msiexec", "/i", \
    "C:\\ReviewBoard\\Downloads\\Silk-Subversion-1.6.17-win32.msi", "/qn"])
    print "end of installation"
