
cnt = 0
n = 2
prev_primes = []
from time import time
start = time()

while n <= 2*(10**6):
    add = True
    for it in prev_primes:
        if n % it == 0:
            add = False
            break
    
    if add:
        prev_primes.append(n)
        cnt += 1
    n += 1

print("ans is: ", sum(prev_primes))
print("time taken: %s seconds" %  (time()-start))
