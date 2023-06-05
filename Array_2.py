arr = []
print('Enter 6 array elements: ')
for i in range(7):
  list = int(input())
  arr.append(list)

max = arr[0]
for i in range(7):
  if arr[i] > max:
    max = arr[i]
print("The largest element in array is: ", max)
