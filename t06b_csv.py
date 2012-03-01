# -*- coding: UTF-8 -*-
import os, sys
import csv

IN_FILENAME = "06.csv"
OUT_FILENAME = "06-out.csv"

def run ():
  with open (IN_FILENAME, "rb") as inf:
    reader = csv.reader (inf)

    with open (OUT_FILENAME, "wb") as outf:
      writer = csv.writer (outf)
      writer.writerows (reader)
