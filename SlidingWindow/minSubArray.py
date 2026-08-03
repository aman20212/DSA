# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Start small. Ship something.")
def minSubArrayLen(arr, sum):
    currentSum = 0
    minimum = float('inf')
    left = 0
    for i in range(len(arr)):
        currentSum = currentSum + arr[i]
        while (currentSum >= sum):
            minimum = min(minimum, i - left + 1)
            currentSum -= arr[left]
            left = left+1
    return 0 if minimum == float('inf') else minimum



print(minSubArrayLen([2,3,1,2,4,3], 7))