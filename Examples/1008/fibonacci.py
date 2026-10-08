'''
    Fib sequence

    Authors:
        Lark, Bailey, Michael R, Declan, Jackson, 
'''

def fibonacci(n):
    fibs = [0, 1]
    for i in range(2, n+1):
        #last 2 numbers
        newfib = fibs[i-1] + fibs[i-2]
        fibs.append(newfib)
        #print(i, "->", newfib)
        #print(fibs)
    return fibs[n]

result = fibonacci(7)
print(result)
