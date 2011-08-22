#!/usr/local/bin/python

import commands
import imp
import os
import platform
from subprocess import call
import sys


class InstallerModuleError(Exception):
    pass

# List the different platforms to install dependencies on.
apt_platforms = ["Ubuntu", "Debian"]
yum_platforms = ["Fedora", "RedHat Enterprise", "Fedora", "CentOS"]
# Different user choices.
positivelist = ["Yes", "yes", "Y", "y"]
negativelist = ["No", "no", "N", "n"]
# Retreiving system information.
OperatingSystem = platform.uname()[0]
Version = platform.uname()[2]
Arch = platform.uname()[4]
# Finding the path of the dependency installer file.
if OperatingSystem == "Linux":
    OperatingSystem = "linux"
    SystemInfo = platform.linux_distribution()
    Platform = SystemInfo[0]
    if Platform in apt_platforms:
        kind = "standards"
    else:
        kind = "yums"
elif OperatingSystem == "Windows":
    OperatingSystem = "windows"
    try:
        imp.find_module("win32api")
    except ImportError:
        DependencyInstaller("win32ins", "install")
    kind = "x86"


# Based on the action selected (guide, install) executes the correct
# function from the dependency file.
def DependencyInstaller(module, action):
    ApplicationName = module
    filename = ("%s.%s.%s" % (OperatingSystem, kind, module))
    responsible_module = None
    try:
        responsible_module = __import__("reviewboard.installer." + filename,\
         fromlist=[filename])
    except ImportError:
        raise InstallerModuleError
    responsible_function = getattr(responsible_module, action)
    return responsible_function()


# main function that makes sure if the script has been called from the
# terminal or cmd, the user can specify which program they want to
# install or get the guide for.
def main():
    if len(sys.argv) == 1:
        empty = raw_input("You need to choose an application to install.\n"\
         + "(ex: python rb_install mysqldb)\n")
        sys.exit()
    else:
        module = sys.argv[1]
        filename = ("%s.%s.%s" % (OperatingSystem, kind, module))
        Ins = raw_input("Would you like us to install " + module \
        + " for you?(Yes,No)")
        if Ins in negativelist:
            action = "guide"
        elif Ins in positivelist:
            if(os.getuid() == 0):
                action = "install"
            else:
                print "You need to run this application as an administrator "\
                + "in order to install " + module
                sys.exit()
        else:
            print "Please select one of the two"
            sys.exit(1)
        print DependencyInstaller(module, action)

if __name__ == "__main__":
    main()
