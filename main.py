# todo list
# 1. Сделать простой excel файл таблицу с фиктивными данными заболевших covid
# 2. найти библиотеку для чтения xls xlsx файлов https://pythonru.com/uroki/chtenie-i-zapis-fajlov-excel-xlsx-v-python
# 3. найти библиотеку для записи xls xlsx файлов

import pandas as pd

top_players = pd.read_excel('./testfile.xlsx')
top_players.head()