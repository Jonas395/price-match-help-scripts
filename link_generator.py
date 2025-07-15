import pandas as pd

input_file = 'input/link_table.xlsx'
all_sheets = pd.read_excel(input_file, sheet_name=None)

for sheet_name, df in all_sheets.items():
    column1 = df.iloc[:, 0]
    column2 = df.iloc[:, 1]

    link_list = []

    for x, y in zip(column1, column2):
        link_list.append(f'URL HERE {x} {y}')

    output_path = f'output/{sheet_name}_links.txt'
    with open(output_path, 'w') as outfile:
        outfile.write('\n'.join(str(i) for i in link_list))

    print(f'Links saved to {output_path}')
