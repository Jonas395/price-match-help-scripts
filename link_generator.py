import pandas as pd
import os

input_file = 'input/link_table.xlsx'
all_sheets = pd.read_excel(input_file, sheet_name=None)

output_folder = 'output/links'
os.makedirs(output_folder, exist_ok=True)

for sheet_name, df in all_sheets.items():
    url_domain = ""
    column0 = df.iloc[:, 0]
    for x in column0:
        if pd.notna(x):
            x = str(x).strip()
            if x:
                url_domain = f'{url_domain}{x}'

    print(f'Base URL template: {url_domain}')

    column1 = df.iloc[:, 1]
    column2 = df.iloc[:, 2]

    link_list = []

    for x_val, y_val in zip(column1, column2):
        x_val = "" if pd.isna(x_val) else str(x_val)
        y_val = "" if pd.isna(y_val) else str(y_val)
        link = url_domain.format(x=x_val, y=y_val)
        link_list.append(link)

    output_path = f'{output_folder}/{sheet_name}_links.txt'
    with open(output_path, 'w') as outfile:
        outfile.write('\n'.join(link_list))

    print(f'Links saved to {output_path}')
