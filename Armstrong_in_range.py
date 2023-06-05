# This program generates Armstrongs of 3 digit nos only
def isArmstrong(num):
    xerox = num
    sum = 0
    while num:
        rem = num % 10
        sum = sum + (rem ** 3)
        num = num // 10

    if xerox == sum:
        return True
    else:
        return False

A_list = []
for no in range(1, 1000):
    if isArmstrong(no):
        A_list.append(no)

print(A_list)