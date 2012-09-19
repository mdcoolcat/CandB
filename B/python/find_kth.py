import random
from test_helper import test

#partition in descending order
#randomly choose pivot
def partition(a, start, end):
    #random index, put it at the beginning
    i = random.randint(start, end)
    a[start], a[i] = a[i], a[start]
    pivot = a[start]
    i = j = start + 1
    while j <= end:
        if a[j] > pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
        j += 1
    a[start], a[i - 1] = a[i - 1], a[start]
    return i - 1 #new index of pivot

#find the kth element in unsorted array a
def find_kth(a, start, end, k):
    pivot = partition(a, start, end)
    new_index = pivot - start
    if new_index  == k:
        return a[pivot]
    if k < new_index:
        return find_kth(a, start, pivot - 1, k)
    else:
        return find_kth(a, pivot + 1, end, k - new_index -1)
    
def main():
    k = 4
    n = 1000
    arr = random.sample(range(n), n / 3)
    sort = sorted(arr, reverse = True)
    print 'test result...'
    for i in range(k):
        test(find_kth(arr, 0, len(arr) - 1, i), sort[i])

if __name__ == '__main__':
    main()
