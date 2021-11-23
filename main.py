# todo list
# 1. Сделать простой excel файл таблицу с фиктивными данными заболевших covid
# 2. найти библиотеку для чтения xls xlsx файлов https://pythonru.com/uroki/chtenie-i-zapis-fajlov-excel-xlsx-v-python
# 3. найти библиотеку для записи xls xlsx файлов
# 4. объединить два excel файла в один с продолжением номера индекса

import pandas as pd

dataframe = pd.read_excel('./testfile.xlsx')
dataframe.head()

print(dataframe.columns[1])
print(dataframe.dtypes)

arr = dataframe.values
print(arr)