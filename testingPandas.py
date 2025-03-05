import pandas as pd
print(pd.__version__)

series_obj = pd.Series([1,7,9,13,17,99])
print(f'{series_obj}\n')

series_objeto2 = pd.Series ([4,7,8,-2], index = ['alfa','beta','teta','gama'])
print(f'{series_objeto2}\n')