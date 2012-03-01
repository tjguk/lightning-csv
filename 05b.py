# -*- coding: UTF-8 -*-
import os, sys
import csv

FILENAME = "05.csv"

data = [
  ("Item", "Quantity"),
  ("Python", "£3.50"),
  ("El Niño", "£4,000"),
]

with open (FILENAME, "w", encoding="mbcs", newline="") as f:
  writer = csv.writer (f)
  writer.writerows (data)

os.startfile (FILENAME)
