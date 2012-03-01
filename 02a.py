# -*- coding: UTF-8 -*-
##
## Use python launcher
##

import os, sys
import csv

FILENAME = "02.csv"

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

os.startfile (FILENAME)
