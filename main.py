import pandas as pd

name = 'all_seasons'

csv_file_path = name + '.csv'  
data_frame = pd.read_csv(csv_file_path, encoding='ISO-8859-1')

excel_file_path = name + '.xlsx' 
data_frame.to_excel(excel_file_path, index=False)

print(f'CSV file "{csv_file_path}" has been transformed and saved as Excel file "{excel_file_path}"')