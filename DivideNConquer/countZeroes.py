def countZeroes(arr):
    left = 0
    right = len(arr) - 1
    while (left <= right):
        mid = (left+right) // 2
        if (arr[mid] == 0 and (mid == 0 or arr[mid-1] ==1)):
            return len(arr) - mid;
        if (arr[mid] == 1):
            left = mid +1
        else:
            right = mid - 1;
            
    return right - left + 1


print(countZeroes([1,0,0,0,0]));