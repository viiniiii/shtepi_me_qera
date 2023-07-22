def fuqia(baza, eksponenti):
    res = 1
    for index in range (eksponenti):
        res = res * baza
    return res
print(fuqia(2,3))
