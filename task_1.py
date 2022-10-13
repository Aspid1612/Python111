# Определяем сложность каждой операции алгоритма
a = len(arr) - 1  #O(n)
out = list()  #O(n)

while a > 0: #O(log(n))
    out.append(arr[a])  #O(1)
    a = a // 1.7
out.merge_sort()  #O(n log(n))
