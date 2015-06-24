#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from cx_Freeze import setup, Executable


buildOptions = {
    "packages": [
        "duplicity",
    ],
    "excludes": [],
    "include_files": [],
}


executables = [
    Executable('example.py', 'Console', targetName='example')
]

setup(name='example',
      version='0.1',
      description='includes librsync',
      options={"build_exe": buildOptions},
      executables=executables
)

