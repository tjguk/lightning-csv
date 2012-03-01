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
  reader = csv.reader (f)
  fields = reader.next ()
  data = [dict (zip (fields, row)) for row in reader]

for item in data:
  print data
