import numpy as np
from numpy import add
import pandas as pd

df = pd.read_csv ('client/invoice-data.csv') 
df['json'] = df.to_json(orient='records', lines=True).splitlines()


dfjson = df['json']
print(dfjson)

np.savetxt(r'./output.txt', dfjson.values, fmt='%s')