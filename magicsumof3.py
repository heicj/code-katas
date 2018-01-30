"""
Blind4Basics, Belliot, rohin993
def magic_sum(arr):
    return arr and sum(x for x in arr if x%2 and '3' in str(x)) or 0
"""
def magic_sum(arr):
    total = 0
    if arr != None:
        for num in arr:    
            numtype = type(num/10)
            if num % 10 == 3 or isinstance(numtype,int):
                total = total + num
    return total
