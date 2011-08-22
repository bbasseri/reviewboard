import httplib
import re
from reviewboard.__init__ import *
import simplejson
from subprocess import call
import urllib
import xml.dom.minidom
from xml.dom import minidom

# This Script is used to Upgrade ReviewBoard. The user requires
# Admin privilages in order to upgrade.


# Returns and array which includes the final stable version
# and the final development version of ReviewBoard.
# Using JSON to interact with the API and to retrieve the
# Latest version of the code.
def GetLatestVersion():
    path = "/api/products/reviewboard/?expand=development_version,"\
    + "stable_version&api_format=json"
    headers = {"Accept": "application/json"}
    conn = httplib.HTTPConnection("www.reviewboard.org")
    conn.request("GET", path, headers=headers)
    jsonresponse = conn.getresponse()
    data = jsonresponse.read()
    conn.close()

    jsdict = simplejson.loads(data)
    dev_array = []
    stable_array = []

    devMajorVersion = jsdict['product']['development_version']['major_version']
    devMinorVersion = jsdict['product']['development_version']['minor_version']
    devVersion = str.lower(re.sub(r'\s', '', jsdict['product']\
    ['development_version']['version']))
    dev_array = (devMajorVersion, devMinorVersion, devVersion)

    stableMajorVersion = jsdict['product']['stable_version']['major_version']
    stableMinorVersion = jsdict['product']['stable_version']['minor_version']
    stableVersion = str.lower(re.sub(r'\s', '', jsdict['product']\
    ['stable_version']['version']))
    stable_array = (stableMajorVersion, stableMinorVersion, stableVersion)

    result_array = (stable_array, dev_array)
    return result_array


# Returns an array of the version the user is using.
def GetCurrentVersion():
    return VERSION


# Returns True of the user is using the final released version.
def Check():
    if get_package_version() != str(GetLatestVersion()[0][2]) and \
    get_package_version() != str(GetLatestVersion()[1][2]):
        return False
    return True


# Upgrades the ReviewBoard version the user is using.
# Major is "major_version.minor_version" and version is the complete version.
def Upgrade(major, version):
    if version:
        call(["easy_install", "-f",\
        "http://downloads.reviewboard.org/releases/ReviewBoard/%s/" % major,\
        "-U", "Reviewboard==%s" % version])


if __name__ == "__main__":
    stableVersion = GetLatestVersion()[0]
    devVersion = GetLatestVersion()[1]
    Upgrade(str(stableVersion[0]) + "." + \
    str(stableVersion[1]), stableVersion[2])
    print devVersion
    print stableVersion
