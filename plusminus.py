def plusMinus(arr):
    pos = 0
    neg = 0
    zeros = 0
    for i in (arr):
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zeros += 1
    formatted_string = "{:.6f}".format(pos/len(arr))
    print(formatted_string)
    print(f"{float(pos/len(arr))} \n {float(neg/len(arr))} \n {float(zeros/len(arr))}")

plusMinus([1,1,0,-1,-1])