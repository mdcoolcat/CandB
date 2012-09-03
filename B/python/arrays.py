# search, sort of array

# check an unsorted array if 2 values' sum to given x, return all the pairs
# dictionary is not allowed
# assuming number in arr is not necessarily unique
# O(nlogn)
def check_array(arr, x):
    #sorted(arr)
    arr.sort()
    left = 0
    right = len(arr) - 1
    result = []
    while left < right:
        if (arr[left] + arr[right] < x):
            left += 1
        elif (arr[left] + arr[right] > x):
            right -= 1
        else:
            result.append((arr[left], arr[right]))
            if arr[left] == arr[left + 1]:
                left += 1
            elif arr[right] == arr[right - 1]:
                right -= 1
            else:
                left += 1
    return result

def main():
    #print check_array([0, 0, 3, 8, 5, 0, -1, 8], 8)
    print check_array([0, -1, 0, 0, 8], 0)

if __name__ == '__main__':
    main()
