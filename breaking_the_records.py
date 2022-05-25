scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
temp_min = scores[0]
temp_max = scores[0]
max_count = 0
min_count = 0

for score in scores:
    if temp_max < score:
        temp_max = score
        max_count += 1
    elif temp_min > score:
        temp_min = score
        min_count += 1
print(max_count, min_count)
