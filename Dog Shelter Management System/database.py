import sqlite3
import pandas as pd

conn = sqlite3.connect('veritabani.db')

excelPath = 'Data/data.xlsx'
sheet_dict = pd.read_excel(excelPath, sheet_name=None)

for sheetName, df in sheet_dict.items():
    df.to_sql(sheetName, conn, if_exists='replace', index=False)

cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabloNames = [row[0] for row in cursor.fetchall()]

for tableName in tabloNames:
    df = pd.read_sql_query(f"SELECT * FROM {tableName}", conn)
    print(df)

conn.close()