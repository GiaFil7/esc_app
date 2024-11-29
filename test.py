import pandas as pd # type: ignore
from utils import get_country_codes

ccs = get_country_codes("ESC 1956")
ccs = list(ccs['code'])
print(ccs)