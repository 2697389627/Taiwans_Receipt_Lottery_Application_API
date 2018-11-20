# Taiwans_Receipt_Lottery_Application_API

[中文版](#中文版)

## Description
This is a web server project use Python Flask to provide the information 
that Taiwans-Receipt-Lottery-Crawler project crawl from the internet.

There's two version , One is to use the SQLite database file to storage.
The SQLite file is provide in this project as :
```
ApplicationDatabase.db
```
and the Python file to use it is :
```
  LotteryApiProviderSQLite.py
```
and the structure is :
```
  .tables : LotteryTable
   rows   : time | this_time | last_time
```
and each row storage the data crawler crawled.
You can easily use
```
  python LotteryApiProviderSQLite.py
```
on your command line to start the service.But make sure to chage the URL which
```
  DATABASE = '~/ApplicationDatabase.db'
```
into the correct location!

And the other way is to use MySQL.
<br/>You should create and start your MySQL server on your computer And use this file :
```
  LotteryApiProviderSQLite.py
```
and your MySQL database , table should be like :
```
+----------------------------+
| Database                   |
+----------------------------+
| LotteryApplicationDatabase |
+----------------------------+

+--------------------------------------+
| Tables_in_lotteryapplicationdatabase |
+--------------------------------------+
| LotteryData                          |
+--------------------------------------+

+-----------+--------------+
| Field     | Type         |
+-----------+--------------+
| time      | varchar(100) |
| this_time | varchar(300) |
| last_time | varchar(300) |
+-----------+--------------+
```
----------------

<a name="中文版"/>

# 這是一個使用 Python Flask 撰寫，專門提供 發票中獎號碼 API 的 web server

## 描述
有兩種版本，一種是連接 SQlLite 和 MySQL 的版本
SQLite 的 .db 資料庫已經附上
```
ApplicationDatabase.db
```
然後對應使用 SQLite 的 Python 檔案是：
```
  LotteryApiProviderSQLite.py
```
這個 SQLite 檔案的結構是：
```
  .tables : LotteryTable
   rows   : time | this_time | last_time
```
每個單位儲存的都是爬蟲軟體爬到的資料。
<br/>如果想要啟動的話：
```
  python LotteryApiProviderSQLite.py
```
不過要記得更改 Python 檔案的這邊：
```
  DATABASE = '~/ApplicationDatabase.db'
```
記得要將 DATABASE 指向正確的位置。
<br/><br/>
或是你可以使用 MySQL，當你在你的計算機上創建完相關的 Database , table和相關資料後，啟動對應的檔案：
```
  LotteryApiProviderSQLite.py
```
你的 MySQL 資料庫結構應該長得像這樣 :
```
+----------------------------+
| Database                   |
+----------------------------+
| LotteryApplicationDatabase |
+----------------------------+

+--------------------------------------+
| Tables_in_lotteryapplicationdatabase |
+--------------------------------------+
| LotteryData                          |
+--------------------------------------+

+-----------+--------------+
| Field     | Type         |
+-----------+--------------+
| time      | varchar(100) |
| this_time | varchar(300) |
| last_time | varchar(300) |
+-----------+--------------+
```
