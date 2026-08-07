def findRotatedIndex(arr, num):
    left = 0
    right = len(arr) - 1;
    while (left <= right):
        mid = (left+right) // 2
        if arr[mid] == num:
            return mid
        if arr[left] <= arr[mid]:
            if arr[left] <= num < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < num <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


print(findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 8));