'''
Interact with Maxima (a computer algebra system) via command line
'''
from subprocess import getoutput as CLI


def maxima(command):
    command = 'display2d:false$' + command
    output = CLI('maxima --batch-string=\'{}\''.format(command))
    '''
    (%i1) display2d:false$
    (%i2) <CMD>
    (%o2) <RESULT>
    '''
    return output[output.index('(%o2)')+5:].strip()

def primep(n):
    output = maxima('primep({});'.format(n))
    return output == 'true'

def factor(n):
    output = maxima('factor({});'.format(n))
    result = []
    for prime_power in output.split('*'):
        prime_power = (prime_power+'^1').split('^')[:2]
        result.append(tuple(int(i) for i in prime_power))
    return result

def next_prime(n):
    output = maxima('next_prime({});'.format(n))
    return int(output)
