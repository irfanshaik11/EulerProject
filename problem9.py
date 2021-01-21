breaktok = False
for i in range(1,1001):
    for j in range(i+1, 1001):
        k = 1000 - i - j
        a,b,c = sorted([i,j,k])

        if a**2 + b**2 == c ** 2:
            print(a*b*c)
            breaktok = True
            break
    if breaktok:
        break


