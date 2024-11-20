#mport pandas as pd # type: ignore

#data = pd.read_excel('country_codes.xlsx', sheet_name='1956_codes')
#html = data.to_html()

#print(html)

#x = 10 * [True]
#print(x)

#import numpy as np

n = 5
x = [0, 0, 0, 0, 0]
t = [[0, 0, 0, 0, 0, 0] for _ in range(n)]

t2 = [[0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0]]

if t == t2:
    print("Yes")
else:
    print("No")

t[0][2] = 1
t2[0][2] = 1
print(t)
print(t2)

