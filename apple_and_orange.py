count_a = 0
count_o = 0
a = 4
b = 12
s = 7
t = 10
apples = [2, 3, -4]
oranges = [3, -2, -4]
for i in range(0, (len(apples) - 1)):
    apples[i] += a
    if apples[i] > s and apples[i] < t:
        count_a += 1
for j in range(0, (len(oranges) - 1)):
    oranges[i] += b
    if oranges[i] > s and oranges[i] < t:
        count_o += 1
print(count_a, count_o)