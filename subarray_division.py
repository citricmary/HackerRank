s = [2, 2, 1, 3, 2]
d = 4
m = 2 #len of the subarray
subarray = []
counter = 0


for i in range(len(s) - m + 1):
    subarray = s[i:m+i]
    print(subarray)
    if sum(subarray) == d:
        counter += 1
print(counter)