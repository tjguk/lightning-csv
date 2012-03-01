# -*- coding: UTF-8 -*-
import os, sys
import csv

FILENAME = "02.csv"

with open (FILENAME) as f:
  reader = csv.reader (f)
  for row in reader:
    print row
