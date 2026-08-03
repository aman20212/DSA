function minSubArrayLen(arr, sum) {
  let currentSum = 0;
  let left = 0;
  let minimum = Infinity;

  for (let right = 0; right < arr.length ; right++) {
    currentSum+= arr[right];

    while (currentSum >= sum) {
      minimum = Math.min(minimum, right - left + 1);
      currentSum-= arr[left];
      left++;
      
    }
  }
  return minimum === Infinity ? 0 : minimum;
}


console.log(minSubArrayLen([2,3,1,2,4,3], 7));