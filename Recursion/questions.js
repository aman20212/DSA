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

