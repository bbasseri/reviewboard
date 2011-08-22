import commands
from download import *
import os
import platform
from subprocess import call
import sys
import urllib

pversionmajor = sys.version_info[0]
pversionminor = sys.version_info[1]

url = \
"http://effbot.org/downloads/PIL-1.1.7.win32-py2." + str(pversionminor) \
+ ".exe"
pil = "PIL-1.1.7.win32-py2." + str(pversionminor) + ".exe"
pilpath = \
"C:\\ReviewBoard\\Downloads\\" + "PIL-1.1.7.win32-py2." \
+ str(pversionminor) + ".exe"
file_name = "PIL-1.1.7.win32-py2." + str(pversionminor) + ".exe"


def guide():
    return "To install Python Imaging Library download the .exe"\
           + "depending on your python version from: "\
           + "http://www.pythonware.com/products/pil/"\
           + "Download the one that matches your python version"\
           + "Run the installer and follow the onscreen instructions"


def install():
    dl_dir = "C:\\ReviewBoard\\Downloads"
    download(url, dl_dir, file_name)
    call([pilpath, "/qn"])
