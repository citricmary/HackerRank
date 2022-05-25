a = [2, 4]
b = [16, 32, 96]
numbers_between = range(a[-1], b[0] + 1)

counter = 0
for number in numbers_between:
    is_valid = True
    for other in a:
        if number % other != 0:
            is_valid = False
            break

    for other in b:
        if other % number != 0:
            is_valid = False
            break
    if is_valid:
        counter += 1

print(counter)


            



