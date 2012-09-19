import random

#partition in descending order
#randomly choose pivot
def partition(a, start, end):
    #random index, put it at the beginning
#    print 'in partition...'
    i = random.randint(start, end)
    a[start], a[i] = a[i], a[start]
    pivot = a[start]
    #print str(start)+' '+str(end)+' '+str(pivot)
    i = j = start + 1
    while j <= end:
        if a[j] > pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
        j += 1
    a[start], a[i - 1] = a[i - 1], a[start]
    #print 'pivot pos:'+str(i - 1)
    return i - 1 #new index of pivot

#recursive
def quick_sort(a, start, end):
    pivot = partition(a, start, end)
    if start < pivot:
        quick_sort(a, start, pivot - 1)
    if end > pivot:
        quick_sort(a, pivot + 1, end)

def find_kth(a, start, end, k):
    pivot = partition(a, start, end)
    new_index = pivot - start
    #print 'p th:'+str(new_index)
    #print a
    if new_index  == k:
        return a[pivot]
    if k < new_index:
     #   print 'left..'+str(k)
        return find_kth(a, start, pivot - 1, k)
    else:
      #  print 'right..'+str(k-new_index-1)
        return find_kth(a, pivot + 1, end, k - new_index -1)
    
def main():
    n = 50
    arr = random.sample(range(n), n)
    #quick_sort(arr, 0, len(arr) - 1)
    for i in range(4):
        print find_kth(arr, 0, len(arr) - 1, i)

if __name__ == '__main__':
    main()
