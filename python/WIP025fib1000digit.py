'''
What is the index of the first term in the fibonacci sequence to contain 1000 digits
'''


def fib_until_iter():
    tail = 0
    current_fib = 1
    index = 1
    while current_fib < 10**999:
        index += 1
        tail = current_fib
        current_fib = current_fib + tail
    return index


print(fib_until_iter())


