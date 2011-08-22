import os
import sys
import urllib
import zipfile


def get_unzipped(url, dl_dir,):
    if not dl_dir.endswith(':') and not os.path.exists(dl_dir):
        os.mkdir(dl_dir)

    name = os.path.join(dl_dir, 'temp.zip')

    try:
        name, hdrs = urllib.urlretrieve(url, name)
    except IOError, e:
        print "Can't retrieve %r to %r: %s" % (url, dl_dir, e)
        return

    try:
        z = zipfile.ZipFile(name)
        _createstructure(name, dl_dir)
    except zipfile.error, e:
        print "Bad zipfile (from %r): %s" % (url, e)
        return

    for n in z.namelist():
        if not n.endswith('/'):
            outfile = open(os.path.join(dl_dir, n), 'wb')
            outfile.write(z.read(n))
            outfile.flush()
            outfile.close()

    z.close()
    os.unlink(name)


def _createstructure(file, dir):
    _makedirs(_listdirs(file), dir)


def _makedirs(directories, basedir):
    for dir in directories:
        curdir = os.path.join(basedir, dir)

        if not os.path.exists(curdir):
            os.mkdir(curdir)


def _listdirs(file):
    zf = zipfile.ZipFile(file)
    dirs = []

    for name in zf.namelist():
        if name.endswith('/'):
            dirs.append(name)

    dirs.sort()
    return dirs
