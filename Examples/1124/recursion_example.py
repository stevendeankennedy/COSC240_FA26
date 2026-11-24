'''
    Recursion Time!

    Special thanks to Bailey, Rich, Declan, 
'''

def r(n):
    #base case
    if n == 0:
        print("stop")
        return

    #recursive case
    print(n)
    r(n-1)
    print(n)

def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1

    return fib(x-1) + fib(x-2)

# a to the power of b
def exp(a, b):
    # base, anything to the power of 0 is 1
    if b == 0:
        return 1
    elif b == 1:
        return a
    # recursive
    #return a * exp(a, b-1) # linear
'''
    # math-y version
    first = b//2
    second = b - first
    return (exp(a, first) * exp(a, second))
''' 

#x = 50
#result = fib(x)
#print(f"fib({x}) is {result}")

a = 2
b = 3
result = exp(a,b)
print(f"{a}^{b}={result}")















