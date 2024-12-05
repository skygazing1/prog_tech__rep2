
import pandas as pd

# считывание данных из файлов

file1_path = '1.xlsx'
file2_path = '2.xlsx'
file3_path = '3.xlsx'

df1 = pd.read_excel(file1_path)
df2 = pd.read_excel(file2_path)
df3 = pd.read_excel(file3_path)

# обновление идентификаторов

# для файла 1 с 1
df1['id'] = range(1, len(df1) + 1)

# для файла 2 с последнего id файла 1 + 1
start_id_2 = df1['id'].max() + 1
df2['id'] = range(start_id_2, start_id_2 + len(df2))

