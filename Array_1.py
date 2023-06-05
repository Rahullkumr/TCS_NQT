# 1. Find smallest no in an array
arr = []
print('Enter 6 array elements: ')
for i in range(7):
  list = int(input())
  arr.append(list)

min = arr[0]
for i in range(7):
  if arr[i] < min:
    min = arr[i]
print("The smallest element in array is: ", min)
