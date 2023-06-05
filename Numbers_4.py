# Prime number in a given range

def isPrime(num):
    if num == 2:
        return True

    for divisor in range(2, num):
        if num % divisor == 0:
            return False
    return True


print("Enter range")
start = int(input('Enter start range: '))
end = int(input('Enter end range: '))

prime_nos = []
for no in range(start, end + 1):
    if isPrime(no):
        prime_nos.append(no)

print(prime_nos)

