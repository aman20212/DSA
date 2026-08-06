def sortedFrequency(arr, num):
    left = checkLeftOccurence(arr, num)
    if left == -1:
        return -1
        
    right = checkRightOccurence(arr, num)
    return right - left + 1
    
def checkLeftOccurence(arr, num):
    left = 0
    result = -1
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if (arr[mid] == num):
            result = mid
            right = mid - 1
        elif arr[mid] < num:
            left = mid + 1
        else:
            right = mid -1
    return result
    
def checkRightOccurence(arr, num):
    left = 0
    result = -1
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if (arr[mid] == num):
            result = mid
            left = mid + 1
        elif arr[mid] < num:
            left = mid + 1
        else:
            right = mid -1
    return result
    



print(sortedFrequency([1,1,2,2,2,2,3],2))