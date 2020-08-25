def factorial(x):
    factorial = 1
    for i in range(1,x):
        factorial = factorial * i
    return factorial
def sin(x):
    return x - x**3/factorial(3) +