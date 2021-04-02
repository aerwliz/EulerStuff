import sys

n = 0
c = 1
ni = []

while n < 10001:
    f = True
    c += 1
    for i in ni:
        if (i * i > c):
            break
        if c % i == 0:
            f = False
            break
    if f:
        ni.append(c)
        n += 1

print(ni[10000])
    
