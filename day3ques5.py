"""
    Ek function hai jiska input do  sorted ascending order array and ek num hoga, us array me se do number ko return krna hai ki us dono ka sum given  umber se barabar ho

    sample = (45, 67, 89, 100)
    sample2 = (1, 50 , 63, 77, 91)
    result = (1, 45, 50, 63, 67, 77, 89, 91, 100)
"""


def sortedArray(arr1, arr2):
    result = []

    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1

        else:
            result.append(arr2[j])
            j += 1

    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result


sample = [45, 67, 89, 100]
sample2 = [1, 50, 63, 77, 91]


print(sortedArray(sample, sample2))
