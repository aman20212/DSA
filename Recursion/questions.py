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


def someRecursive(a, callback):
    if (len(a) == 0):
        return False
    if (callback(a[0])):
        return True
    return someRecursive(a[1:], callback)

def flatten(a):
    if (len(a) == 0):
        return []
    head = a[0]
    tail = a[1:]
    flathead = flatten(head) if (isinstance(head, list)) else [head]
    # use + to return a new list, avoid using extend() which modifies the original list
    return flathead + flatten(tail)
    
print(flatten([[1,2], [3], [4,5]]))

# 1. Using .append() (Accumulator / Tail Recursion)
# Idea: .append() adds a single item to the end of an existing list in-place. 
# We pass an accumulator list (output) down through each recursive frame and 
# append one capitalized string at a time before moving to the next element.

def capitalize_first_append(arr, output=None):
    # Initialize output list on the very first call
    if output is None:
        output = []

    # Base case: when no elements remain, return accumulated list
    if len(arr) == 0:
        return output

    # Build the single capitalized string
    capitalized_word = arr[0][0].upper() + arr[0][1:]
    
    # .append() adds the single string to the accumulator in-place
    output.append(capitalized_word)

    # Pass the mutated accumulator to the next recursive call
    return capitalize_first_append(arr[1:], output)

print(capitalize_first_append(['car', 'taco', 'banana']))
# Output: ['Car', 'Taco', 'Banana']

# 2. Using .extend() (Merging Lists In-Place)
# Idea: .extend() unpacks an entire iterable (the list returned by the recursive call) 
# and merges its 
# elements directly into the current list in-place. 
# We wrap the current word inside a 1-element list [word], call .extend() with the r
# ecursive result, and return the modified list.

def capitalize_first_extend(arr):
    # Base case: return empty list to terminate recursion
    if len(arr) == 0:
        return []

    # Capitalize word and wrap it as a single-element list
    result = [arr[0][0].upper() + arr[0][1:]]

    # .extend() mutates 'result' in-place by unpacking the recursively returned list
    # Note: .extend() returns None, so we call it as a separate statement
    result.extend(capitalize_first_extend(arr[1:]))

    # Return the in-place extended list
    return result

print(capitalize_first_extend(['car', 'taco', 'banana']))
# Output: ['Car', 'Taco', 'Banana']


# 3. Using += (In-Place Concatenation Operator)
# Idea: When applied to lists, 
# += calls Python's __iadd__ method, which is the operator equivalent of .extend(). 
# It updates the left-hand list in-place by appending all items from the recursive call.

def capitalize_first_iadd(arr):
    # Base case: return empty list
    if len(arr) == 0:
        return []

    # Wrap the capitalized word in a list
    result = [arr[0][0].upper() + arr[0][1:]]

    # '+=' modifies 'result' in-place by unpacking elements from the recursive list
    result += capitalize_first_iadd(arr[1:])

    # Return the mutated list
    return result

print(capitalize_first_iadd(['car', 'taco', 'banana']))
# Output: ['Car', 'Taco', 'Banana']



def nestedEvenSum(obj):
    total = 0  # Replaces 'let sum = 0'

    # Matches: for (const [key, value] of Object.entries(obj))
    for key, value in obj.items():
        
        # Matches: typeof value === 'number' && value % 2 === 0
        if isinstance(value, int) and not isinstance(value, bool) and value % 2 == 0:
            total += value
            
        # Matches: typeof value === 'object' && value !== null
        elif isinstance(value, dict):
            total += nestedEvenSum(value)

    return total


# Test case 1
obj1 = {
    "outer": 2,
    "obj": {
        "inner": 2,
        "otherObj": {
            "superInner": 2,
            "notANumber": True,
            "alsoNotANumber": "yup"
        }
    }
}
print(nestedEvenSum(obj1))  # Output: 6

# Test case 2
obj2 = {
    "a": 2,
    "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
    "c": {"c": {"c": 2}, "cc": "ball", "ccc": 5},
    "d": 1,
    "e": {"e": {"e": 2}, "ee": "car"}
}
print(nestedEvenSum(obj2))  # Output: 10



def capitalizeWords(words):
    if (len(words) == 0):
        return []
    return [words[0].upper()] + capitalizeWords(words[1:])


words = ['i', 'am', 'learning', 'recursion'];
print(capitalizeWords(words));



def stringifyNumbers(obj):
    new_obj = {}
    
    for key, value in obj.items():
        # Check for numbers (int/float) while excluding booleans
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            new_obj[key] = str(value)
        elif isinstance(value, dict):
            new_obj[key] = stringifyNumbers(value)
        else:
            new_obj[key] = value
            
    return new_obj


# Test Case
obj = {
    "num": 1,
    "test": [],
    "data": {
        "val": 4,
        "info": {
            "isRight": True,
            "random": 66
        }
    }
}

print(stringifyNumbers(obj))
# Output:
# {'num': '1', 'test': [], 'data': {'val': '4', 'info': {'isRight': True, 'random': '66'}}}



def collect_string(obj):
    arr = []
    for key, value in obj.items():
        if isinstance(value, str):
            arr.append(value)
        elif isinstance(value, dict):
            arr.extend(collect_string(value))  # or: arr += collect_string(value)
    return arr


# Cleaned up top-level indentation (starts at column 0)
obj = {
    'stuff': "foo",
    'data': {
        'val': {
            'thing': {
                'info': "bar",
                'moreInfo': {
                    'evenMoreInfo': {
                        'weMadeIt': "baz"
                    }
                }
            }
        }
    }
}

print(collect_string(obj))
# Output: ['foo', 'bar', 'baz']