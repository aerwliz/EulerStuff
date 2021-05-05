ref = [1]

for i in range(2000):
  ref.append(0)
tempref = ref
for i in range(1000):
  siz = len(ref)
  for j in range(siz):
    tempref[j] = ref[j] * 2
  for j in range(siz):
    if(tempref[j]>=10):
      tempref[j+1] += 1
      tempref[j] -= 10
  ref = tempref
sum = 0
for i in ref:
  sum += i
print(sum)
