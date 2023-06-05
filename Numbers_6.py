# check if given no is Perfect number
# sum of factors(except no itself) of a no == no itself
# 6 --> 1 + 2 + 3 == 6(itself)

num = int(input('Enter a positive number: '))
factors = []
sum = 0
for i in range(1, num):
    if num % i == 0:
        factors.append(i)

for element in factors:
    sum = sum + element


print(f"Factors: {factors}")
if sum == num:
    print('Perfect no')
else:
    print('Not perfect no')

