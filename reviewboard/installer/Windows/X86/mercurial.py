import commands
from download import *
import os
import platform
from subprocess import call
import sys
import urllib


def guide():
    return "To install Mercurial Download the installation file from " \
           + "http://mercurial.berkwood.com/ depending on your python"\
           + "version. Follow the onscreen instructions to install."


def install():
    if sys.version_info[0] == 2:
        url = "http://mercurial.berkwood.com/binaries/"
        p_version_minor = sys.version_info[1]

        if p_version_minor < 4:
            mercurial_version = "Mercurial-1.0.exe"
        elif p_version_minor > 4 and p_version_minor < 5:
            mercurial_version = "Mercurial-1.4.exe"
        elif p_version_minor >= 5:
            mercurial_version = "Mercurial-1.4.3.exe"

        url += mercurial_version

    folder = "C:\\ReviewBoard\\Downloads\\"
    download(url, folder, mercurial_version)
    call([folder + mercurial_version, "/qn"])
