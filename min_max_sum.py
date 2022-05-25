arr = [1, 3, 5, 7, 9]
b = arr.copy()

del arr[len(arr)- 1]
min = sum(arr)

del b[0]
max = sum(b)

print(min, max)