import sys

largest = -1
fir = 1
sec = 1
factor1 = -1
factor2 = -1
def check(a):
    temp = 0
    b = a
    while b > 0:
        temp *= 10
        temp += b % 10
        b = (b-b%10)/10
    return temp == a

for i in range(999):
    #print(i)
    for j in range(999):
        
        guess = (999-i)*(999-j)
        if guess > largest:
            if check(guess):
                largest = guess
                factor1 = 999-i
                factor2 = 999-j
                #print(largest)
print(largest)
print(factor1)
print(factor2)




