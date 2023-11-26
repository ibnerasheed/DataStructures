"""
    Ek function hai jiska input ek array and ek num hoga, us array me se do number ko return krna hai ki us dono ka sum given  umber se barabar ho
"""


def arraySum(arr, num):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == num:
                return (arr[i], arr[j])

    return ()


result = arraySum([2, 4, 5, 7, 9], 9)
print(result)

result = arraySum([2, 4, 5, 7, 9, -1], 8)
print(result)

result = arraySum([2, 4, 5, 7, 9, -1, 0, 1], 0)
print(result)


result = arraySum([-4, -5, 78, 87. - 78, -701, 6, 44], 50)
print(result)
