import math
def sumofGP(a,n,r):
  total = (a*(math.pow(r,n)-1))/r-1
  return total
a = int(input("Enter first number of GP series\n"))
r = int(input("Enter common ratio of GP series\n"))
n = int(input("Enter total numbers in GP series\n"))
total = sumofGP(a,n,r)
print("Sum of GP series is:" , total)