#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from OPSI.Util import librsyncSignature


if __name__ == '__main__':
    for name in sys.argv[1:]:
        print("Sig of {0}: {1}".format(name, librsyncSignature(name).strip()))

