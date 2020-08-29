# School Programming Competition 2019-2

107 學年度第二學期，全校程式設計實作競賽

## 競賽題目
共兩題，第一題偏應用、第二題偏算法，不限程式語言。

程式檔分別取名為 `⟨姓名⟩_Q1`、`⟨姓名⟩_Q2`，放在資料夾 `⟨姓名⟩_Contest` 中。

- Q1：算眾數
  - 題目有提到眾數可能不存在，但競賽時沒有說明什麼情形不存在眾數 😕
  - 分成 A、B、Ｃ 三個部分
    - 但具體如何分並沒有規定 😕，似乎只要執行時能選擇即可
  - A 部分：
    - 輸出 `N=⟨n⟩，例如 ⟨x_1, ..., x_n⟩`
      - `n` 為隨機整數（`20 ≤ n ≤ 100`）
      - `x_1`、…、`x_n` 為 `n` 個隨機整數（`0 ≤ x_i ≤ 100`），以空白分隔
    - 輸出 `m`、`c`，以空白分隔
      - `m` 為 `x_1`、…、`x_n` 之中的眾數
      - `c` 為 `m` 的出現次數
      - 可能有 1 個以上的眾數，分行輸出
  - B 部分：
    - 輸出 `N=⟨n⟩，例如 ⟨x_1, ..., x_n⟩`
      - `n` 為隨機整數（`10 ≤ n ≤ 52`）
      - `x_1`、…、`x_n` 為 `n` 個隨機大小寫拉丁字母
    - 輸出 `m`、`c`，以空白分隔
      - `m` 為 `x_1`、…、`x_n` 之中的眾數
      - `c` 為 `m` 的出現次數
      - 可能有 1 個以上的眾數，分行輸出
  - C 部分：
    - 輸入檔名 `A`
    - 輸入檔名 `B`
    - 輸入（從 `A` 檔案）
      - 第 1 行，有整數 `n`
      - 第 2 行，有 `n` 段字串 `x_1`、…、`x_n`，以空白分隔
    - 輸出（至 `B` 檔案）`m`、`c`，以空白分隔
      - `m` 為 `x_1`、…、`x_n` 之中的眾數
      - `c` 為 `m` 的出現次數
      - 可能有 1 個以上的眾數，分行輸出
- Q2：計算成功通過機率
  - 輸入（從檔案）
    - 第 1 行，有整數 `n`
    - 第 2 行開始，共 `n` 行，有 `n` 個小數 `x_m1`、…、`x_mn`，以空白分隔
      - 這個 `n` × `n` 矩陣為加權有向圖
      - `x_mn` 為從 `m` 點移動到 `n` 點的通過機率（`0.0 ≤ x_mn ≤ 1.0`）
    - 第 `n+1` 行，有 2 個整數 `s`、`e`（`1 ≤ s,e ≤ n`），以空白分隔
      - `s` 為起點
      - `e` 為終點
  - 輸出小數，為成功從 `s` 點移動到 `e` 點的機率，走過的路不重複走
    - 競賽當天的測資答案似乎是「走過的點不重複走」的版本 😕

## 程式碼
- [`Q1.py`](./Q1.py)
- [`Q2.py`](./Q2.py)
