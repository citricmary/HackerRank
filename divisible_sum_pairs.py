ar = [1, 2, 3, 4, 5, 6]
k = 5
counter = 0

for i in range(len(ar)):
    for j in range(len(ar)):
        if i < j:
            if (ar[i] + ar[j]) % k == 0:
                counter += 1
print(counter)
