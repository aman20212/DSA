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