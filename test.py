#mport pandas as pd # type: ignore

#print(html)

#x = 10 * [True]
#print(x)

#import numpy as np

cols = ['1st','2nd','3rd','4th','5th','Last']
logical_index = 5

sort_by = cols[logical_index]
cols.insert(0, cols.pop(cols.index(cols[logical_index])))
print(f"If sorting by {sort_by} column: {cols}")
