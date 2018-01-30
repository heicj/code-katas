"""
siebenschlaefer
def check_exam(arr1, arr2):
    return max(0, sum(4 if a == b else -1 for a, b in zip(arr1, arr2) if b))
"""
def check_exam(arr1,arr2):
    total = 0
    for i in range(0, len(arr1)):
        if arr1[i] == arr2[i]:
            total = total + 4
        elif arr2[i] == '':
            total = total + 0
        else:
            total = total - 1
    if total < 0:
        return 0
    else:
        return total
