from collections import Counter

def sockMerchant(n, ar):
    new_ar = Counter(ar)
    pairs = 0
    for value in new_ar.values():
        if value >= 2:
            pairs += int(value / 2)
    return pairs    


