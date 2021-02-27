def factorial(x):
    factorial = 1
    for i in range(1,x + 1):
        factorial = factorial * i
    return factorial
def sin(x,n):
    if type(n) != int or n < 1:
        raise ValueError('the value of n is wrong')
    y = 0
    for i in range(n):
        m = 2*i + 1
        y += (-1)**i * x**(m)/factorial(m)
    return y

def cos(x,n):
    if type(n) != int or n < 1:
        raise ValueError('the value of n is wrong')
    y = 0
    for i in range(n):
        m = 2*i
        y += (-1)**i * x**(m)/factorial(m)
    return y

def derivative_sin(x,n):
    if type(n) != int or n < 1:
        raise ValueError('the value of n is wrong')
    y = 0
    for i in range(n):
        m = 2*i + 1
        y += ((-1)**i * x**(m -1))/factorial(m - 1)
    return y

def derivative_cos(x,n):
    if type(n) != int or n < 1:
        raise ValueError('the value of n is wrong')
    y = 0
    for i in range(1,n+1):
        m = 2*i
        y += (-1)**i * x**(m - 1)/factorial(m - 1)
    return y

if derivative_sin(3,3) == cos(3,3):
    print('dsin(x)/x = cos(x), the result is true')

if derivative_cos(3,3) == -sin(3,3):
    print('dcos(x)/x = -sin(x), the result is true')
