from getunzipped import *
import os
import shutil
from subprocess import call
import urllib
import win32api
import win32con
import zipfile


def guide():
    return "Download the apache installer from " \
    + "http://apache.raffsoftware.com//httpd/binaries/win32/" \
    + "httpd-2.2.19-win32-x86-openssl-0.9.8r.msi" \
    + "Follow the onscreen instructions."


def install():
    package_name = "mod_fcgid 2.3.6"
    archive_url = "http://www.apachelounge.com/download/mods/" + \
        "mod_fcgid-2.3.6-win32-x86.zip"
    get_unzipped(archive_url, "C:\\ReviewBoard\\")
    print " ".join(["copy",\
"\"C:\ReviewBoard\mod_fcgid 2.3.6\mod_fcgid.so\"", \
"\"C:\Program Files (x86)\Apache Software " + \
        "Foundation\Apache2.2\modules\""])
    shutil.copy("C:\ReviewBoard\mod_fcgid 2.3.6\mod_fcgid.so", \
        "C:\Program Files (x86)\Apache Software Foundation\Apache2.2\modules")

    # Open config file
    config_file = open("C:\Program Files (x86)\Apache Software Foundation" + \
        "\Apache2.2\conf\httpd.conf", 'r+')
    conf_lines = config_file.readlines()
    inserted_line = False

    for i in range(len(conf_lines)):
        l = conf_lines[i]

        if l.startswith("LoadModule"):
            print "inserting at", i
            conf_lines.insert(i, \
                "LoadModule fcgid_module modules/mod_fcgid.so \n")
            inserted_line = True
            break

    if not inserted_line:  # No LoadModule statements found so append one.
        conf_lines.append("LoadModule fcgid_module modules/mod_fcgid.so \n")

    config_file.writelines(conf_lines)
    config_file.close()
    print "Installation complete"
