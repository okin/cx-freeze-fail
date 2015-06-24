#! /usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import os

if os.name == 'posix':
    from duplicity import librsync
elif os.name == 'nt':
    import librsync

def librsyncSignature(filename, base64Encoded=True):
    (f, sf) = (None, None)
    try:
        f = open(filename, 'rb')
        sf = librsync.SigFile(f)
        if base64Encoded:
            sig = base64.encodestring(sf.read())
        else:
            sig = sf.read()
        f.close()
        sf.close()
        return sig
    except Exception as e:
        if f: f.close()
        if sf: sf.close()
        raise Exception(u"Failed to get librsync signature: %s" % e)


if __name__ == '__main__':
    print("Sig of self: {0}".format(librsyncSignature(__file__)))

