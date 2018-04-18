import math

# O(n) where n is the number of num2
def multiply(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0
    if num2 == 1:
        return num1
    else:
        return num1 + multiply(num1, num2 - 1)


def multiply_quicker(num1, num2):
    # Grab smallest and biggest numbers
    big = max(num1, num2)
    small = min(num1, num2)
    # Anything times 0 is zero
    if big == 0 or small == 0:
        return 0
    if small == 1:
        return big
    else:
        if small % 2 == 0:
            return multiply_quicker(big, small >> 1) + multiply_quicker(big, small >> 1)
        else:
            return big + multiply_quicker(big, small >> 1) + multiply_quicker(big, small >> 1)
