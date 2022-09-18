def sList(sl):
    n = len(sl) 
    temp = sl[0]
    sl[0] = sl[n - 1]
    sl[n - 1] = temp
    return sl
l = [10, 14, 5, 9, 56, 12]
print(l)
print("S list: ",sList(l))
