## smth_mod модуль для импорта функций для работы

import pandas as pd

def update_ids():
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

# для файла 3 с последнего id файла 2 + 1
    start_id_3 = df2['id'].max() + 1
    df3['id'] = range(start_id_3, start_id_3 + len(df3))

# сохранение обновленных данных

    updated_file1_path = 'file1_updated.xlsx'
    updated_file2_path = 'file2_updated.xlsx'
    updated_file3_path = 'file3_updated.xlsx'

    df1.to_excel(updated_file1_path, index=False)
    df2.to_excel(updated_file2_path, index=False)
    df3.to_excel(updated_file3_path, index=False)

    print(f"Файлы успешно обновлены и сохранены: {updated_file1_path}, {updated_file2_path}, {updated_file3_path}")
    return [updated_file1_path, updated_file2_path, updated_file3_path]
