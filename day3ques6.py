"""
    Ek function hai jiska input ek sorted ascending order array and ek num hoga, us array me se do number ko return krna hai ki us dono ka sum given  umber se barabar ho
"""
"""two pointer algorithm"""


def arraySum(arr, num):
    i = 0
    j = len(arr)-1
    while i < j:
        if arr[i] + arr[j] == num:
            return (arr[i], arr[j])
        elif arr[i] + arr[j] > num:
            j = j-1
        else:
            i = i + 1
    return ()


result = arraySum([2, 4, 5, 7, 9], 9)
print(result)

result = arraySum([-1, 2, 4, 5, 7, 9], 8)
print(result)

result = arraySum([-1, 0, 1, 2, 4, 5, 7, 9], 0)
print(result)
