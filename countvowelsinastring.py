"""
def count_vowels(s = ''):
    return sum(x.lower() in 'aeoui' for x in s) if type(s) == str else None
"""
def count_vowels(s = ''):
    # your code
    count = 0
    if isinstance(s, int):
        return None
    else:
        vowels = ['a','e','i','o','u']
        for letter in s:
           if isinstance(letter, int):
              continue
           elif letter.lower() in vowels:
              
              count += 1
    if count > 0:
        return count
    else:
        return None
 
