from SortsTestHarness import doSort
import timeit

types = ["b", "i"]
sizes = [10, 50, 100, 500]
orders = ["a", "d", "r", "n"]
repeats = 3
times = []
for sortType in types:
    for arrayType in orders:
        for n in sizes:
            times.append(timeit.timeit("doSort(n, sortType, arrayType)", setup="from __main__ import doSort, sortType, arrayType, n", number=repeats))

print("Sort Type\tArray Type\tSize\tTime")
for i in range(len(types)):
    for j in range(len(orders)):
        for k in range(len(sizes)):
            print(types[i], "\t\t", orders[j], "\t\t", sizes[k], "\t", times[i*len(orders)*len(sizes) + j*len(sizes) + k])
