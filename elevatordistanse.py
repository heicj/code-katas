"""
def elevator_distance(array):
    return sum(abs(array[i+1] - array[i]) for i in range(len(array)-1))
"""
def elevator_distance(array):
    d = 0
    for i in range(0, len(array) -1):
        d += abs(array[i] - array[i+1])
    return d
