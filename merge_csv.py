import pandas as pd
from pathlib import Path
import sqlite3

# CSVが置いてあるディレクトリを明示する
data_dir = Path("data")
db_path = "work_data.db"
conn = sqlite3.connect(db_path)
conn = sqlite3.connect("work_data.db")
csv_files = list(data_dir.glob("*.csv"))

df_list = []
# 散在しているデータを統合する
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    df_list.append(df)

if df_list:
    all_data = pd.concat(df_list, ignore_index=True)
    all_data.to_csv("merged_data.csv", index=False)
    print("CSVを統合しました。")
else:
    print("CSVファイルが見つかりません。")

all_data = pd.concat(df_list, ignore_index=True)

all_data.to_sql(
    "work_records",
    conn,
    if_exists="replace",
    index=False
)
print("データベースに保存しました。")

check_df = pd.read_sql("SELECT * FROM work_records LIMIT 5;", conn)
print(check_df)

sql_count = """
SELECT
    担当者,
    COUNT(*) AS 件数
FROM work_records
GROUP BY 担当者
ORDER BY 件数 DESC;
"""

count_df = pd.read_sql(sql_count, conn)

sql_sum = """
SELECT
    担当者,
    SUM(金額) AS 合計金額
FROM work_records
GROUP BY 担当者
ORDER BY 合計金額 DESC;
"""

sum_df = pd.read_sql(sql_sum, conn)

count_df.to_csv("担当者別_件数.csv", index=False, encoding="utf-8-sig")
sum_df.to_csv("担当者別_合計金額.csv", index=False, encoding="utf-8-sig")

conn.close()
