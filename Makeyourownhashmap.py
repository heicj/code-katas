"""
Voile
from functools import reduce
from collections import defaultdict

def my_hash_map(list_of_strings):
    return reduce(lambda h,s: h[sum(map(ord,s))].append(s) or h, list_of_strings, defaultdict(list))
"""

def my_hash_map(list_of_strings):
    #return hashmap
    total = 0
    dict = { }
    for i in range(0, len(list_of_strings)):
        word = list_of_strings[i]
        
        for letter in word:
            total = total + ord(letter)
        dict[total] = [word]
        total = 0
    return dict

