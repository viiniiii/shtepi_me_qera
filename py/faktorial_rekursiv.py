def faktorial(n):
    if(n == 1):
        return 1
    else: 
        return faktorial(n-1) * n
a = 5
print(faktorial(a))
