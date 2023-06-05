# Check whether a given no is Armstrong (only 3digit nos)
# sum of cube(in case of 3d nos) of digits of a no, if == given no
# eg: 153 => 1^3 + 5^3 + 3^3 == 153

num = int(input("Enter a number: "))
xerox = num
sum = 0
while num:
    rem = num % 10
    sum = sum + (rem ** 3)
    num = num // 10

if xerox == sum:
    print('Armstrong')
else:
    print('Not Armstrong')