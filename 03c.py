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

csv.register_dialect ("QuotedPiper", delimiter="|", quoting=csv.QUOTE_ALL)

with open (FILENAME, "wb") as f:
  writer = csv.writer (f, dialect="QuotedPiper")
  writer.writerows (data)

os.startfile (FILENAME)
