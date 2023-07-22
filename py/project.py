'''
# S = 2 - 4 + 8 - 16 + ...
def vargu(poz):
    s = 0
    shenja = 1
    for j in range (1,poz + 1):
        s = s + 2**j * shenja
        shenja = shenja * -1
    return s
print(vargu(6))
'''
'''
def shuma(nr):
    sh = 0
    for i in range (1,nr+1):
        sh = sh + i
    return sh
print(shuma(100))
'''
'''
n = 5
for i in range(n):
    for j in range(i):
        print('*', end="")
    print("")

for i in range(n,0,-1):
    for j in range(i):
        print('*', end="")
    print("")
'''
'''
def funk(a):
    if a <= 0:
        return 3*a + 20
    else:
        return a - 10
print(funk(-1))
'''
'''
def abs(a):
    if a < 0:
        return a * -1
    else: return a
print(abs(-5))
'''
