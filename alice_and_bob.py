def compareTriplets(a, b):
    result_a = 0
    result_b = 0
    for i in a, b:
        if a[i] > b[i]:
            result_a += 1
        if a[i] < b[i]:
            result_b += 1
        else:
            pass
        return (result_a, result_b)

compareTriplets((1, 2, 3), (4, 2, 1))
