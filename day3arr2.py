"""Create a function which takes input as array of a number and a number and returns the index, search the given input array and return the position in the array
and if number is not present return -1
"""


def findIndex(array, num):
    for index in range(len(array)):
        if array[index] == num:
            return index
    return -1


index = findIndex([2, 4, 5, 6], 6)
print(index)

index = findIndex([2, 4, 5, 6], 2)
print(index)

index = findIndex([2, 4, 5, 6], 4)
print(index)

index = findIndex([2, 4, 5, 6], 100)
print(index)
