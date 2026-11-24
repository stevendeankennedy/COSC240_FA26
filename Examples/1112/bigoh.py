'''
    Big Oh example
'''

def linear(n):
    count = 0
    for i in range(n):
        count += 1
    print(f"linear - {n}:{count}")

def quadratic(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    print(f"quadratic - {n}:{count}")

def cubic(n):
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                count += 1
    print(f"cubic - {n}:{count}")

def logarithm_base2(n):
    count = 0
    oldn = n
    n = n // 2
    while n > 0:
        n = n // 2
        count += 1
    print(f"log - {oldn}:{count}")

n = 500
linear(n)
quadratic(n)
cubic(n)
logarithm_base2(n)
