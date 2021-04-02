import sys

ans = 600851475143
i = 2
largest = -1
while ans >= i:
    if ans % i == 0:
        ans /= i
        if i > largest:
            largest = i
    else:
        i = i+1

print(largest)
