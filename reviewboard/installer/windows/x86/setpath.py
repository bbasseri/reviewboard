import os
import platform
import re
import sys
import win32api
import win32con


# This script is used to add some of the install files to the system path
# of user's machine.
def setPath(path):
    print "setting path"
    regkey = win32api.RegOpenKeyEx(win32con.HKEY_LOCAL_MACHINE, \
    'SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment', 0, \
    win32con.KEY_ALL_ACCESS)
    value = str(win32api.RegQueryValueEx(regkey, "Path")[0])
    value = win32api.ExpandEnvironmentStrings(value)
    print value
    if path not in value:
        win32api.RegSetValueEx(regkey, "Path", 0, win32con.REG_SZ, value + ";"\
                               + path)
    win32api.RegCloseKey(regkey)
    print "Path set"
