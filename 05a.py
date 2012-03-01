# -*- coding: UTF-8 -*-
import os, sys
import codecs
import csv

FILENAME = "05.csv"

data = [
  (u"Item", u"Quantity"),
  (u"Python", u"£3.50"),
  (u"El Niño", "£4,000"),
]

with codecs.open (FILENAME, "wb", encoding="utf-8") as f:
  writer = csv.writer (f)
  writer.writerows (data)

