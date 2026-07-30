# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def maxSubarraySum(arr, num):
    if (len(arr) < num):
        return None
    left = 0
    sumS = 0
    maxS = 0
    for item in range(num):
        sumS = sumS + arr[item]
    maxS = sumS
    
    for item in range(num, len(arr)):
        sumS = sumS - arr[left] + arr[item]
        left = left+1
        maxS = max(maxS, sumS)
    return maxS
    
    
print(maxSubarraySum([100,200,300,400], 2))