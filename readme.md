# CSV業務データの自動集約・集計ツール

## 概要
複数の担当者が個別に管理しているCSV形式の業務データを、
PythonとSQLiteを用いて自動で集約・集計するツールです。

手作業による集計の属人化や転記ミスを防止することを目的としています。

## 想定課題
- 担当者ごとにCSVファイルが分かれている
- 集計作業に時間がかかる
- 手作業によるミスが発生する

## 改善内容
- CSVファイルを一括で読み込み
- SQLiteに格納し、SQLで集計
- 担当者別の件数・合計金額を自動出力

## 使用技術
- Python
- pandas
- SQLite

## 実行方法
```bash
pip install -r requirements.txt
python merge_csv.py
