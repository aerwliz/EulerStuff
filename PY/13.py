import sys

with open("eul.txt") as f:
    content = f.readlines()
list1 = []
for line in content:
    a = int(line)
    while a > 999999999999:
        a = (int)(a/10)
    list1.append(a)
summ = 0
for i in list1:
    summ += i
print(summ)
