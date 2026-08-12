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