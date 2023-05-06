def bubbleSort(list_a):
    n = len(list_a)
    for i in range(n-1):
        for j in range(0, n-1-i):
            if list_a[j] > list_a[j+1]:
                list_a[j], list_a[j+1]= list_a[j+1], list_a[j]

list_a = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(list_a)
print(list_a)
