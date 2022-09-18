def list_sort(lst):
    lst.sort(key=lambda x: abs(x), reverse=True)
    return lst
print(list_sort([1, 5, 77]))
print(list_sort([19, 8.3, -4, 11, 0, 5]))
print(list_sort([-33, -0.05, -4.18, 11.2, 13.12, 55, 7.1]))
