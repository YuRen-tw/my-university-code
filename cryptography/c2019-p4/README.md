# Cryptography 2019 - Project 4

2019，107-2 學期，密碼學導論 4th Project：RSA 加解密與數位簽章

## 流程
- 分組，每組 2 個人：A、B
- A
  1. 生成指定長度的 2 個質數
  2. 以上面的質數生成一組 RSA 公鑰、密鑰，用來加解密
- B
  1. 生成指定長度的 2 個質數
  2. 以上面的質數生成一組 RSA 公鑰、密鑰，用來數位簽章
  3. 用 A 的公鑰加密指定的資料
  4. 用 B 的私鑰對加密後的資料做數位簽章
- A
  1. 用 B 的公鑰驗證數位簽章
  2. 用 A 的私鑰解密資料


## 程式碼
- [`maxima_interface.py`](./maxima_interface.py)：丟東西給 Maxima 算（主要用來生質數）
- [`num_theory.py`](./num_theory.py)：定義與數論相關的函數
- [`RSA.py`](./RSA.py)：主程式

