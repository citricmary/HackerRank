from collections import Counter

arr = [1, 1, 2, 2, 3]

birds = Counter(arr)
max = max(birds.values())
temp = []
for key, value in birds.items():
    if value == max:
        temp.append(key)
print(min(temp))


