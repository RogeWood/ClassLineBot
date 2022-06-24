# Class Line Bot

班群上的機器人

## Devlop Environment
Programming language: python

Server: heroku

Database: google sheet(類數據庫)


**註**: heroku不會儲存檔案，檔案必須存在數據庫上


## Feature

- 課表
    1. 整周課表
    2. 今天課表
    3. 下一節課
- 功課
    1. 紀錄作業
    2. 刪除作業
    3. 顯示作業
- 調課
    1. 紀錄調課
    2. 顯示調課
    3. 刪除調課
- 考試(待加中)

## 指令
- `bot help` --查詢指令

- 課程
    - `bot 課表` --查課表
    - `bot 今天課表/bot today` --查今天課表
    - `bot 下節課/bot next` --查下節課

- 作業
    - `bot hw` --顯示作業
    - `bot hw add` (作業內容) --加入作業
    - `bot hw rm` --移除最前面的作業
    - `bot hw rm` (數字) --移除第n個作業
    - `bot hw rm all` --刪除全部作業

- 調課
    - `bot class` --顯示調課
    - `bot class add (月/日) (科目) (月/日) (科目)` --加入
    - `bot class rm` --刪除全部調課
