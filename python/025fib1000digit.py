'''
What is the index of the first term in the fibonacci sequence to contain 1000 digits
'''


def fib_generator():
    cache = [0, 1]
    while cache[0] < 10**999:
        cache = [cache[0] + cache[1], cache[0]]
        yield cache[0]

print(len([x for x in fib_generator()]))
