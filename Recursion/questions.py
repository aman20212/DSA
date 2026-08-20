def power(num: int, base: int):
    if base == 0:
        return 1
    else:
        return num * power(num, base-1)
        
        


def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num-1)
print(factorial(4))


def productOfArray(arr):
    if len(arr) == 0:
        return 1
    else:
        return arr[0] * productOfArray(arr[1:])
print(productOfArray([1,2,3,10]))

def fib(n):
    # Base cases: the 1st and 2nd Fibonacci numbers are both 1
    if n == 1 or n == 2:
        return 1
    # Recursive case: sum of the previous two numbers
    return fib(n - 1) + fib(n - 2)

# Examples
print(fib(1))  # Output: 1
print(fib(2))  # Output: 1
print(fib(4))  # Output: 3
print(fib(6))  # Output: 8


def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 1 or n == 2:
        return 1
    
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

print(fib_memo(50))  # Output: 12586269025 (Calculates instantly!)


def isPalindrome(str):
    if (len(str) <= 1):
        return True
    if (str[0] != str[len(str) - 1]):
        return False
    return isPalindrome(str[1:-1])
    
print(isPalindrome("121"))