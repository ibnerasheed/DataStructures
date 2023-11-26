"""
    Write a function which takes array of number(int) as input and returns max and min values as a tuple 
"""


def maxMin(arr):
    val = arr
    maximum = val[0]
    minimum = val[0]

    for item in arr:
        if item > maximum:
            maximum = item

        if item < minimum:
            minimum = item

    return (minimum, maximum)


result = maxMin([4, 1, 3, 2])
print(result)

result = maxMin([40, 18, 43, 2887897])
print(result)

result = maxMin([84, 1, 39, 208, 8767])
print(result)

result = maxMin([])
print(result)
