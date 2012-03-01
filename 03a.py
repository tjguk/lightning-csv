# -*- coding: UTF-8 -*-
import os, sys
import csv

FILENAME = "03.csv"

data = [
  ("Item", "Quantity"),
  ("Eggs", 5),
  ('"Farmhouse" Bread', 1),
  ("Apples, Granny Smith", 10),
  ("Apples, Golden Delicious", 5),
]

with open (FILENAME, "wb") as f:
  writer = csv.writer (f, delimiter="|", quoting=csv.QUOTE_ALL, skipinitialspace=True)
  writer.writerows (data)

os.startfile (FILENAME)
