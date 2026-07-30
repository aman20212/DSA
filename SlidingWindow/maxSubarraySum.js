function maxSubarraySum(arr, num) {
  let max = 0;
  let left = 0;
  let sum = 0;
  if (arr.length < num) {
    return null;
  }
  for (let i = 0; i < num; i++) {
    sum+= arr[i];
  }
  max = sum;
  for (let right = num; right < arr.length; right++) {
    sum = sum - arr[left] + arr[right];
    left++;
    max = Math.max(max, sum);
  }
  return max;
}


console.log(maxSubarraySum([100,200,300,400], 2));