# -*- coding: UTF-8 -*-
import os, sys
import csv

FILENAME = "03.csv"

with open (FILENAME) as f:
  for row in csv.reader (f, delimiter="|", quoting=csv.QUOTE_ALL, skipinitialspace=True):
    print row
