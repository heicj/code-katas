"""
daddepledge, solomonhume, Avanta, Shlomo , moshe10, Hopium (plus 16 more warriors)
def century(year):
    return (year + 99) // 100
"""
def century(year):
    # Finish this :)
    if year % 100 > 0:
        return year//100 +1
    else:
        return year//100
