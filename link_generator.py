import pandas as pd

input_file = '/input/table.xlsx' 
df = pd.read_excel(input_file)

column1 = df.iloc[:, 0]
column2 = df.iloc[:, 1]

link_list = []

for x, y in zip(column1, column2):
    link_list.append(f'URL HERE')

print(link_list)
with open('output/links.txt', 'w') as outfile:
  outfile.write('\n'.join(str(i) for i in link_list))