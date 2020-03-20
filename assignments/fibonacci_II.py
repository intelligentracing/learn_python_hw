def fibonacci(i):
    if type(1)!= int:
        raise TypeError('Incorrect Fibonacci argument type.')
    elif 1<0:
        raise ValueError('Fibonacci argument must be greater than zero.')
    else:
        a=0
        b=1
        for k in range(0,i):
            c=a+b
            a=b
            b=c
        return a

print("Which one you need?")
i=int(input())
print(str(fibonacci(i)))
