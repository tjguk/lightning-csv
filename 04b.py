# -*- coding: UTF-8 -*-
import os, sys
import csv

FILENAME = "04.csv"

data = [
  ("Item", "Quantity"),
  ("Eggs", 5),
  ('"Farmhouse" Bread', 1),
  ("Apples, Granny Smith", 10),
  ("Apples, Golden Delicious", 5),
]

with open (FILENAME, "wb") as f:
  writer = csv.writer (f)
  writer.writerows (data)

with open (FILENAME) as f:
  reader = csv.DictReader (f)
  print reader.fieldnames
  for row in reader:
    print row

