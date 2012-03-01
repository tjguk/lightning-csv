# -*- coding: UTF-8 -*-
import os, sys

IN_FILENAME = "06.csv"
OUT_FILENAME = "06-out.csv"

def run ():
  with open (IN_FILENAME, "rb") as inf:
    with open (OUT_FILENAME, "wb") as outf:
      for line in inf:
        in_data = (i.strip ().strip ('"') for i in line.split (","))
        outf.write (",".join ('"%s"' % j for j in in_data) + "\n")
