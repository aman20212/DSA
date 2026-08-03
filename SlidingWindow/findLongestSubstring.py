def findLongestSubstring(str):
    left = 0
    maximum = 0
    seen = set()
    for i in range(len(str)):
        while(str[i] in seen):
            seen.remove(str[left])
            left = left+1
        seen.add(str[i])
        maximum = max(maximum, i - left +1)
    return maximum



print(findLongestSubstring('rithmschool'));