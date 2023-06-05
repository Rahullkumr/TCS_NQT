# 1. Check if a number is palindrome or not
# eg = 121 --> 121(after reverse)

num = int(input("Enter an integer: "))
xerox = num
rev = 0
while num:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10

if rev == xerox:
    print('Palindrome')
else:
    print('Not Palindrome')

