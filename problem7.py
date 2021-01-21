
cnt = 0
n = 2
prev_primes = []
from time import time
start = time()

while cnt != 10001:
    for it in prev_primes:
        if n % it == 0:
            break
    else:
        prev_primes.append(n)
        cnt += 1
    n += 1
assert len(prev_primes) > 0

print("ans is: ", prev_primes[-1])
print("time taken: %s seconds" %  (time()-start))
