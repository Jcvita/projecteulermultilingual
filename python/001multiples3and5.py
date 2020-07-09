'''
Find the sum of all the multiples of 3 and 5 below 1000.
'''

def sum_multiples_of_3_and_5(below: int):
    return sum([x for x in range(below) if not (x % 3 and x % 5)])

print(sum_multiples_of_3_and_5(1000))
    
