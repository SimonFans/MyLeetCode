import os
import pandas as pd

csv_list = []
for dirname, dirnames, filenames in os.walk('./Documents'):
    for file in filenames:
        if file == 'a.csv' or file == 'b.csv':
            csv_list.append(dirname + '/'+ file)
print(csv_list)
data1 = pd.read_csv(csv_list[0])
data2 = pd.read_csv(csv_list[1])
output1 = pd.merge(data1, data2,
                   on='ID',
                   how='inner')

output1 = pd.merge(data1, data2,
                   on='ID',
                   how='inner')
output2 = pd.merge(data1, data2,
                   on='ID',
                   how='inner')
df = pd.concat([output1, output2], ignore_index=True)
output_path = './Documents/test/out.csv'
df.to_csv(output_path, index=False)
