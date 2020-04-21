import pandas as pd
from pandas.io.json import json_normalize
import json
import csv


# read jason file
data=pd.read_json(r'input.json')
# normalize based on different keys
df = json_normalize(data["needs"])
df2=json_normalize(data["values"])
#join keys
frames = [df, df2]
result = pd.concat(frames)
#write to csv
output_csv=result.to_csv(r'output_csv.csv', index = None, header=True)
#write to excel, each key in different sheets
with pd.ExcelWriter('output_excel.xlsx') as writer:  
    df.to_excel(writer, sheet_name='needs',index = None, header=True)
    df2.to_excel(writer, sheet_name='values',index = None, header=True)