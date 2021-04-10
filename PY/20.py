import sys

a = 1
for i in range(1,11):
    a *= i

strs = str(a)

summ = 0

for c in strs:
    summ += int(c)

print(summ)    
