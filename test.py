#mport pandas as pd # type: ignore

#data = pd.read_excel('country_codes.xlsx', sheet_name='1956_codes')
#html = data.to_html()

#print(html)

#x = 10 * [True]
#print(x)

#import numpy as np

for place in range(1,50):
    if (place >= 11 and place <=19) or place % 10 == 0 or (place % 10 >=4 and place % 10 <=9):
        text = f"{place}th"
    elif place % 10 == 1:
        text = f"{place}st"
    elif place % 10 == 2:
        text = f"{place}nd"
    elif place % 10 == 3:
        text = f"{place}rd"
    print(text)

