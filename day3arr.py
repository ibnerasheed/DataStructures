def maximum(a, b, c):
    if (a >= b) and (a >= c):
        return a
    elif (b >= a) and (b >= c):
        return b

    else:
        return c


maxm = maximum(3, 4, 757678)
print(maxm)

maxm = maximum(3, 757678, 4)
print(maxm)

maxm = maximum(757678, 3, 4)
print(maxm)


