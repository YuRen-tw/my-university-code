L = 10
F = 10 ** L

def prob_times(a, b):
    return a * b // F

def prob_prod(xs):
    result = F
    for x in xs:
        result = prob_times(result, x)
    return result

def prob_sum(xs):
    return F - prob_prod(F - x for x in xs)


def make_matrix(lines):
    matrix = []
    for line in lines:
        row = []
        for f in line.split():
            num = int(f.split('.')[1].ljust(L, '0'))
            row.append(num)
        matrix.append(row)
    return matrix

def clean(matrix, r, c):
    next_matrix = []
    for i, row in enumerate(matrix):
        if i == r:
            row = ((0 if j == c else x) for j, x in enumerate(row))
        next_matrix.append(row)
    return next_matrix

def move(matrix, start, end, total_prob=F):
    if start == end:
        return total_prob
    result = []
    for next_p, prob in enumerate(matrix[start]):
        if prob != 0:
            next_matrix = clean(matrix, start, next_p)
            next_total_prob = prob_times(total_prob, prob)
            result.append(move(next_matrix, next_p, end, next_total_prob))
    return prob_sum(result)



if __name__ == '__main__':
    import argparse
    
    AP = argparse.ArgumentParser()
    AP.add_argument('--input', '-i', required=True, help='input file')
    args = AP.parse_args()
    
    with open(args.input, 'r') as f:
        lines = f.readlines()
    num = int(lines[0])
    matrix_str = lines[1:num+1]
    start, end = (int(x)-1 for x in lines[num+1].split())
    
    M = make_matrix(matrix_str)
    result = move(M, start, end)
    
    print('0.{}'.format(result)[:-5])

