# sort karne ni aa rha hai btao bsdk

arr = []
print('Enter 6 array elements: ')
for i in range(7):
  list = int(input())
  arr.append(list)
  
sortedA = []
for i in range(0, len(arr)):
  for j in range(i + 1, len(arr)):
    if arr[i] < arr[j]:
      sortedA.append(arr[i])
    else:
      
      # adhura hai pura kro