# check if a number is prime or not
# No divisible by 1 and itself
def isPrime(num):
    if num == 2:
        return True

    for divisor in range(2, num):
        if num % divisor == 0:
            return False
    return True


num = int(input('Enter a number greater than 1: '))
if isPrime(num):
    print('Prime')
else:
    print('Not prime')

