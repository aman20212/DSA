function power(num, base) {
  if (base === 0) {
    return 1;
  } else {
    return num * power(num, base - 1);
  }
}


function factorial(num) {
  if (num === 1 || num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

function productOfArray(arr) {
  console.log(arr);
  if (arr.length === 0) {
    return 1;
  } else {
    return arr[0] * productOfArray(arr.slice(1));
  }
}


function recursiveRange(num){
   if (num === 0) return 0;
   else {
    return num + recursiveRange(num-1);
   }
}

function fib(n){
  // add whatever parameters you deem necessary - good luck! 
  if (n === 1 || n === 2) return 1;
  else {
    return fib(n-1) + fib(n-2);
  }
}

function isPalindrome(str) {
  if (str.length <= 1) {
    return true;
  }
  if (str[0] !== str[str.length - 1]) {
    return false;
  }
  return isPalindrome(str.slice(1,-1));
}

function someRecursive(arr, callback){
    if (arr.length === 0) {
        return false
    }
    if (callback(arr[0])){
        return true
    }
    return someRecursive(arr.slice(1), callback)
  // add whatever parameters you deem necessary - good luck!
}

function flatten(arr) {
  let output = [];
  if (arr.length === 0) {
    return false
  }
  if (!Array.isArray(arr[0])){
    output.push(arr[0])
  }
}

function capitalizeFirst(arr) {
  // Base case: empty array returns an empty array
  if (arr.length === 0) {
    return [];
  }

  // Capitalize first letter + attach the rest of the string
  const capitalized = arr[0][0].toUpperCase() + arr[0].slice(1);

  // Return capitalized word in an array concatenated with the recursive call
  return [capitalized].concat(capitalizeFirst(arr.slice(1)));
}



function nestedEvenSum (obj) {
  // add whatever parameters you deem necessary - good luck!
  let sum = 0;
  for (let key in obj) {
    let value = obj[key];
    if (typeof value === 'number' && value % 2 === 0) {
      sum += value
    } else if (typeof(value) === 'object' && value != null) {
      sum += nestedEvenSum(value);
    }
  }
  return sum;
}


var obj1 = {
  outer: 2,
  obj: {
    inner: 2,
    otherObj: {
      superInner: 2,
      notANumber: true,
      alsoNotANumber: "yup"
    }
  }
}

var obj2 = {
  a: 2,
  b: {b: 2, bb: {b: 3, bb: {b: 2}}},
  c: {c: {c: 2}, cc: 'ball', ccc: 5},
  d: 1,
  e: {e: {e: 2}, ee: 'car'}
};

console.log(nestedEvenSum(obj1)); // 6
console.log(nestedEvenSum(obj2)); // 10


function capitalizeWords (arr) {
  // add whatever parameters you deem necessary - good luck!
  if (arr.length === 0) {
    return [];
  }
  return [arr[0].toUpperCase()].concat(capitalizeWords(arr.slice(1)))
}



function stringifyNumbers(obj) {
  let newObj = {};

  for (let key in obj) {
    let value = obj[key];

    if (typeof value === 'number') {
      newObj[key] = value.toString();
    } else if (typeof value === 'object' && value !== null && !Array.isArray(value)) {
      newObj[key] = stringifyNumbers(value);
    } else {
      newObj[key] = value;
    }
  }

  return newObj;
}