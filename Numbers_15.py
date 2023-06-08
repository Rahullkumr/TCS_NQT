# 15) Reverse digits of a number

no = input("Enter a no: ")
print(no[::-1])


# Longcut method
# num = int(input("Enter a number: "))
#
# rev = 0
# while num:
#     rem = num % 10
#     rev = rev * 10 + rem
#     num = num // 10
#
# print(f"Reversed number = {rev}")