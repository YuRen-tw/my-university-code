def listize(S):
    result = []
    digit_temp = []
    for c in S:
        if c in '0123456789':
            digit_temp.append(c)
        if c in '+*':
            result.append(int(''.join(digit_temp[-4:])))
            digit_temp = []
            result.append(c)
    result.append(int(''.join(digit_temp[-4:])))
    return result

def compute(S):    
    result = 0
    num_temp = 1
    for i in S:
        if i == '+':
            result = (result + num_temp) % 10000
            num_temp = 1
        elif i == '*':
            continue
        else:
            num_temp = (num_temp * i) % 10000
    result = (result + num_temp) % 10000
    return result

if __name__ == '__main__':
    while True:
        S = input('輸入運算式: (輸入 @ 結束) ')
        if S == '@':
            break
        print('運算結果: {}'.format(compute(listize(S))))

