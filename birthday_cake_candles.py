def birthdayCakeCandles(candles):
    max = candles[0]
    for i in range(1, len(candles)):
        if i <= candles[i]:
            max = candles[i]        
    result = candles.count(max)
    return result

print (birthdayCakeCandles([3, 2, 1, 3]))