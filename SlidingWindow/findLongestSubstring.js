function findLongestSubstring(str) {
  let left = 0;
  let maximum  = -Infinity;
  let seen = new Set();
  if (str.trim().length === 0) return 0;
  for (let right = 0; right < str.length; right++) {
    while(seen.has(str[right])) {
      seen.delete(str[left]);
      left++;
    }
    seen.add(str[right]);
    maximum = Math.max(maximum, right - left + 1);
  }
  return maximum;
}



console.log(findLongestSubstring('rithmschool'));