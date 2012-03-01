# -*- coding: UTF-8 -*-

import os, sys

FILENAME = "01.csv"

data = [
  ("Item", "Shop"),
  ("Eggs", "Tesco"),
  ("Bread", "Morrisons"),
  ("Apples", "Tesco"),
]

with open (FILENAME, "w") as f:
  for d in data:
    f.write (",".join (d))
    f.write ("\n")

os.startfile (FILENAME)
