# -*- coding: UTF-8 -*-
import os, sys
import csv

FILENAME = "03.csv"

csv.register_dialect ("QuotedPiper", delimiter="|", quoting=csv.QUOTE_ALL)

with open (FILENAME) as f:
  for row in csv.reader (f, dialect="QuotedPiper"):
    print row
