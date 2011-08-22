import commands
from download import *
import os
import platform
import re
from subprocess import *
import sys
import urllib


def guide():
    return "To download pysvn go to http://pysvn.tigris.org ." \
           + "Download based on your python version and svn version."\
           + "Then Install pysvn"


def install():
    print "Nothing yet"
    dl_dir = "C:\\ReviewBoard\\Downloads\\"
    p = subprocess.Popen(["svn", "--version", "--quiet"], \
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    n = p.communicate()[0]
    m = re.search('[\d]+\W[\d]+\W[\d]+', n)
    svn_version = m.group(0)
    print svn_version
    if sys.version_info[0] == 2:
        p_version_minor = sys.version_info[1]
        if p_version_minor == 6 and svn_version == "1.5.6":
            url = "http://pysvn.tigris.org/files/documents/1233/47202/"\
                + "py26-pysvn-svn156-1.7.2-1280.exe"
            pysvn = "py26-pysvn-svn156-1.7.2-1280.exe"
        elif p_version_minor == 6 and svn_version == "1.6.12":
            url = "http://pysvn.tigris.org/files/documents/1233/48016/"\
                + "py26-pysvn-svn1612-1.7.4-1321.exe"
            pysvn = "py26-pysvn-svn1612-1.7.4-1321.exe"
        elif p_version_minor == 6 and svn_version >= "1.6.15":
            url = "http://pysvn.tigris.org/files/documents/1233/48844/"\
                + "py26-pysvn-svn1615-1.7.5-1360.exe"
            pysvn = "py26-pysvn-svn1615-1.7.5-1360.exe"
        elif p_version_minor == 7 and svn_version == "1.6.12":
            url = "http://pysvn.tigris.org/files/documents/1233/48019/"\
                "py27-pysvn-svn1612-1.7.4-1321.exe"
            pysvn = "py27-pysvn-svn1612-1.7.4-1321.exe"
        elif p_version_minor == 7 and svn_version >= "1.6.15":
            url = "http://pysvn.tigris.org/files/documents/1233/48847/"\
                + "py27-pysvn-svn1615-1.7.5-1360.exe"
            pysvn = "py27-pysvn-svn1615-1.7.5-1360.exe"
    download(url, dl_dir, pysvn)
    subprocess.Popen([dl_dir + pysvn, "/silent"]).wait()
