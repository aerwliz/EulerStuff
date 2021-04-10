import sys

for a in range(1,1001):
    for b in range(1,1001-a):
        c = 1000-a-b
        if c == 0:
            continue
        if a*a+b*b==c*c:
            print(a*b*c)

