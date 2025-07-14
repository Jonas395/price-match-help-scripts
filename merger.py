import pandas as pd

input_file = 'input/input_to_merge.xlsx'
output_file = 'output/merged_output.xlsx'
xls = pd.read_excel(input_file, sheet_name=None)
merged_df = pd.concat(xls.values(), ignore_index=True)
merged_df.to_excel(output_file, index=False)
print(f"All sheets merged and saved to {output_file}")