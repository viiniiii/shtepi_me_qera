def faktorial(n):
    a = 1
    for i in range(1, n+1):
        a = a * i
    return a
b = int(input())
print(faktorial(b))

