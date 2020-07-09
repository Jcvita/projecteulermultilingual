'''
Print the smallest positive number that is evenly divisible by all of the numbers from 1 to 20
'''

def is_divisible(num: int):
    for x in range(20):
        if num % (x + 1) is not 0:
            return False
    return True


def until_divisible():
    total = 20
    while not is_divisible(total):
        total += 20
    return total


print(until_divisible())

