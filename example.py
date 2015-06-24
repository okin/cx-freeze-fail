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


def librsyncPatchFile(oldfile, deltafile, newfile):
    logger.debug(u"Librsync : %s, %s, %s" % (oldfile, deltafile, newfile))
    if oldfile == newfile:
        raise ValueError(u"Oldfile and newfile are the same file")
    if deltafile == newfile:
        raise ValueError(u"deltafile and newfile are the same file")
    if deltafile == oldfile:
        raise ValueError(u"oldfile and deltafile are the same file")

    (of, df, nf, pf) = (None, None, None, None)
    bufsize = 1024*1024
    try:
        of = open(oldfile, "rb")
        df = open(deltafile, "rb")
        nf = open(newfile, "wb")
        pf = librsync.PatchedFile(of, df)
        data = True
        while(data):
            data = pf.read(bufsize)
            nf.write(data)
        nf.close()
        pf.close()
        df.close()
        of.close()
    except Exception as e:
        if nf: nf.close()
        if pf: pf.close()
        if df: df.close()
        if of: of.close()
        raise Exception(u"Failed to patch file: %s" % e)


def librsyncDeltaFile(filename, signature, deltafile):
    (f, df, ldf) = (None, None, None)
    bufsize = 1024*1024
    try:
        f = open(filename, "rb")
        df = open(deltafile, "wb")
        ldf = librsync.DeltaFile(signature, f)

        data = True
        while(data):
            data = ldf.read(bufsize)
            df.write(data)
        df.close()
        f.close()
        ldf.close()
    except Exception as e:
        if df:  df.close()
        if f:   f.close()
        if ldf: ldf.close()
        raise Exception(u"Failed to write delta file: %s" % e)


if __name__ == '__main__':
    print("Sig of self: {0}".format(librsyncSignature(__file__)))

