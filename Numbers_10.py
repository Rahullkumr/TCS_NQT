def sumofAP(a,n,d):
  total = (n*(2*a+(n-1)*d))/2
  return total
a = int(input("Enter first number of an AP series\n"))
n = int(input("Enter total numbers in an AP series\n"))
d = int(input("Enter common difference of an AP series\n"))
total = sumofAP(a,n,d)
print("Sum of an AP series is:" , total)