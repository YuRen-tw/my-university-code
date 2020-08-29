import random

def count(xs):
    result = {}
    for x in xs:
        if x not in result:
            result[x] = xs.count(x)
    return result

def mode(xs):
    c = count(xs)
    num = max(c.values())
    return { k for k, v in c.items() if v == num }, num

def A():
    N = random.randint(20, 100)
    xs = [random.randint(0, 100) for _ in range(N)]
    result, num = mode(xs)
    print('N={}，例如'.format(N), ' '.join(str(x) for x in xs))
    for x in result:
        print(x, num)

def show(xs):
    result = []
    for x in xs:
        if x >= 26:
            x += 6  # - 26 + ord('a') - ord('A')
        result.append(chr(x + 65))  # + ord('A')
    return result
    
def B():
    N = random.randint(10, 52)
    xs = [random.randint(0, 51) for _ in range(N)]
    result, num = mode(xs)
    result = show(result)
    print('N={}，例如'.format(N), ' '.join(show(xs)))
    print('結果有 {} 個眾數'.format(len(result)))
    for x in result:
        print(x, num)

def C():
    input_file = input('input file name: ')
    output_file = input('output file name: ')
    with open(input_file, 'r') as f:
        xs = f.readlines()[1].split()
        result, num = mode(xs)
    with open(output_file, 'w') as f:
        f.writelines(['{} {}\n'.format(x, num) for x in result])


if __name__ == '__main__':
    import argparse
    
    AP = argparse.ArgumentParser()
    AP.add_argument('--function', '-f', required=True, choices=['a', 'b', 'c'],
                    help='function')
    args = AP.parse_args()
    {'a': A, 'b': B, 'c': C}[args.function]()

