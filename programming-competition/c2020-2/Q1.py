import random

def Y(n):
    return n // 10 + n % 10 * 9

codes = 'ABCDEFGHJKLMNPQRSTUVXYW'
code_to_num = { c: Y(i+10) for i, c in enumerate(codes) }
code_to_num['I'] = Y(34)
code_to_num['O'] = Y(35)

num_to_codes = {}
for c in codes:
    num = code_to_num[c] % 10
    if num not in num_to_codes:
        num_to_codes[num] = set()
    num_to_codes[num].add(c)

def last_sum(last9):
    return sum(x*(8-i) for i, x in enumerate(last9))

def comp(code, last9):
    Z = (- code_to_num[code] - last_sum(last9)) % 10
    return 10 if Z == 0 else Z

def possible_code(last9):
    xs = last_sum(last9)
    num = (-xs - last9[-1]) % 10
    return num_to_codes[num]

def A():
    last9 = [int(c) for c in input()]
    print(', '.join(possible_code(last9)))

def B():
    last9 = [int(c) for c in input()]
    possible_set = possible_code(last9)
    choose_set = possible_set.copy()
    while len(choose_set) < 4:
        choose_set.add(random.choice(codes))
    choose_set = list(choose_set)
    print('第一英文碼: ', end='')
    print(' '.join('({}){}'.format(i+1, c) for i, c in enumerate(choose_set)))
    while True:
        code = input()
        if code in possible_set:
            print('檢查碼正確')
            break
        else:
            print('檢查碼={}，檢查碼錯誤'.format(comp(code, last9)))

if __name__ == '__main__':
    S = input('程式 A or 程式 B: (輸入 A 或 B) ')
    if S == 'A':
        A()
    if S == 'B':
        B()

