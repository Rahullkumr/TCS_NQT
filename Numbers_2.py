# 2. Find all Palindrome numbers in a given range

def isPalindrome(num):
    xerox = num
    rev = 0
    while num:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    if rev == xerox:
        return True
    else:
        return False


print("Give range to find Palindrome numbers")
start = int(input('starting position: '))
end = int(input('end position: '))
list = []
for num in range(start, end + 1):
    if isPalindrome(num):
        list.append(num)

print(list)