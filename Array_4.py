# reverse a given array, slicing concept not allowed
arr = []
print('Enter 6 array elements: ')
for i in range(6):
  list = int(input())
  arr.append(list)

new = []
print(arr)
# print(arr[::-1])
for i in range(-1, -7, -1):
  new.append(arr[i])
print(new)
