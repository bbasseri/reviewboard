import commands
from getunzipped import *
import os
import platform
from subprocess import call
import urllib
import sys
import zipfile

pversionmajor = sys.version_info[0]
pversionminor = sys.version_info[1]

url = "http://www.voidspace.org.uk/downloads/pycrypto-2.3.win32-py2." \
+ str(pversionminor) + ".zip"
pycryptozip = "pycrypto-2.3.win32-py2." + str(pversionminor) + ".zip"
pycryptofile = "pycrypto-2.3.win32-py2." + str(pversionminor) + ".msi"


def guide():
    return "To install Pycrypto download the file from "\
    + "http://www.voidspace.org.uk/python/modules.shtml#pycrypto"\
    + "depending on your python version " \
    + "Download the one that matches your python version"\
    + "Run the installer and follow the onscreen instructions"


def install():
    archive_url = url
    get_unzipped(archive_url, "C:\\ReviewBoard")
    call(["msiexec", "/i", "C:\ReviewBoard\\" + pycryptofile, "/qn"])
    print "instalation complete"
