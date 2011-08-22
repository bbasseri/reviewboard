import os
import sys
import urllib


def download(url, dl_dir, file_name):
    print "Starting download"
    if not dl_dir.endswith(':') and not os.path.exists(dl_dir):
        os.mkdir(dl_dir)
        print "built folder"
    print url
    name = os.path.join(dl_dir, file_name)

    try:
        name, hdrs = urllib.urlretrieve(url, name)
    except IOError, e:
        print "Can't retrieve %r to %r: %s" % (url, dl_dir, e)

    install_file = ("%s\%s" % (dl_dir, file_name))
    print install_file
    print "end of download"
