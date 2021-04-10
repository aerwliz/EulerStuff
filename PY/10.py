import sys

primes = []

primes.append(2)

for i in range(3,2000000):
    bonk = True
    for j in primes:
        if j * j > i:
            break
        if i % j == 0:
            bonk = False
            break
    if(bonk):
        primes.append(i)

ans = 0
for k in primes:
    ans += k

print(ans)
