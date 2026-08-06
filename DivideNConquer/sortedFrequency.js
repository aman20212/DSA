function sortedFrequency(arr, num) {
  left = checkLeftOccurence(arr, num);
  if (left === -1) return 0;
  right = checkRightOccurence(arr, num);
  return right - left + 1;
}

function checkLeftOccurence(arr, num) {
  let left = 0;
  let right = arr.length - 1;
  let result = -1;
  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (arr[mid] === num) {
      result = mid;
      right = mid - 1;
    }
    else if (arr[mid] < num) {
      left = mid + 1
    } else {
      right = mid - 1;
    }
  }
  return result;
}

function checkRightOccurence(arr, num) {
    let left = 0;
    let right = arr.length - 1;
    let result = -1;
    while (left <= right) {
      let mid = Math.floor((left + right) / 2);
      if (arr[mid] === num) {
        result = mid;
        left = mid + 1;
      }
      else if (arr[mid] < num) {
        left = mid + 1
      } else {
        right = mid - 1;
    }
  }
  return result;
}

console.log(sortedFrequency([1,1,2,2,2,2,3],3))
// console.log(checkLeftOccurence([1,1,2,2,2,2,3],2))
// console.log(checkRightOccurence([1,1,2,2,2,2,3],2))