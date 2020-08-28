# Cryptography 2018 - Project 3

106 學年度第二學期，破解密碼競賽（密碼學課程第三次 Project）

## 競賽流程
- 總共 4 關卡
  - 起點關卡在數學系教室，其他關卡設置在台北捷運站
  - 前 3 個關卡給一段密文
    - 明文為下個關卡的站名以及一個名字片段
    - 加密方式見下方
  - 在終點關卡拍照
- 將各個名字片段組合成完整名字
- 回到數學系辦公室列印該名字的人物影像

## 加密法
- 仿射密碼（affine cipher）：`E(x) = (ax + b) mod 26`
  - `a` 為任意可逆整數（與 26 互質）
  - `b` 為任意整數
  - `x` 為明文字母
- 3×3 希爾密碼（Hill cipher）：`E(x) = A x mod 26`
  - `A` 為任意 3 × 3 可逆矩陣
    - 解密時提供挖 3 個洞的加密矩陣
  - `x` 為明文向量，每 3 個字母一組
- 縱欄式移項密碼（columnar transposition cipher）


## 程式碼
- 仿射密碼
  - [`MRT_name.py`](./MRT_name.py)：一個 `list` 包含台北捷運站名的拼音、漢字對應
  - [`_mk_axb.py`](./_mk_axb.py)：生成所有加密可能
  - `axb_MRT_name.py`：一個 `list` 包含所有加密可能與其漢字對應
  - [`axb.py`](./axb.py)：解密主程式
- 3×3 希爾密碼
  - [`matrix.py`](./matrix.py)：解密主程式
- 縱欄式移項密碼
  - [`rect.py`](./rect.py)：解密主程式
