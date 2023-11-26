"""ek sorted array hai,o/p bhi sorted chahye sq of each element"""


def sortSq(inputArray):
    length = len(inputArray)
    result = [None] * length
    index = len(inputArray)-1
    leftPointer = 0
    rightPointer = len(inputArray)-1

    while leftPointer <= rightPointer:
        leftvalue = inputArray[leftPointer]**2
        rightvalue = inputArray[rightPointer]**2

        if leftvalue > rightvalue:
            result[index] = leftvalue
            leftPointer = leftPointer + 1
        else:
            result[index] = rightvalue
            rightPointer = rightPointer - 1

        index = index - 1

    return result


result = sortSq([2, 9, 11, 20])
print(result)

result = sortSq([-100, 0, 9, 11, 20])
print(result)

result = sortSq([-34, -76, 56, 78, 90])
print(result)
