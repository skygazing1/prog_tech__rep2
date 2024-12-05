
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

