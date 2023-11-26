"""
    palindrome without reverse 
"""


def palidrome(word):
    left = 0
    right = len(word) - 1

    while left <= right:
        if word[left] != word[right]:
            return False
        left = left + 1
        right = right - 1

    return True


result = palidrome('adil')
print(result)

result = palidrome('a')
print(result)

result = palidrome('aba')
print(result)

result = palidrome('red rum, sir, is murder')
print(result)

result = palidrome('lemon, no melon')
print(result)


result = palidrome('never odd or even')
print(result)
