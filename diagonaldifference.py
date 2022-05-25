arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]
sum = 0
sum_2 = 0

for i in range(len(arr)): 
    sum += arr[i][i]
    sum_2 += arr[i][-i - 1]

    
print(sum)
print(sum_2)


