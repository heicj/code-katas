"""
Unnamed
def multi_table(number):
    return '\n'.join(f'{i} * {number} = {i * number}' for i in range(1, 11))
"""

def multi_table(number):
    str = ''
    for i in range(1, 11):
        n = number * i
        str += '{} * 5 = {}\n'.format(i, n)
    
    return str
