# -*- coding: UTF-8 -*-

import os, sys

FILENAME = "01.csv"

with open (FILENAME) as f:
  for line in f:
    print [i.strip ().strip ('"') for i in line.split (",")]
