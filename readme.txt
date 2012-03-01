* CSV - standard? No RFC, just Excel

* pre-csv module (introduced 2.3)

writing: ",".join ([..])
reading: items = [i.strip ('"') for i in line.split (",")]

Pros: Simple; Python one-liner

Cons: Misses all the corner cases

* csv module for dummies

Writing: 02a.py

Reading: 02b.py


