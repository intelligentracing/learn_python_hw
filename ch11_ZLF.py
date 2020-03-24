def DP_num(n):
    times = 1
    if n < 0:
        raise ValueError('Fibonacci argument must be greater than zero.')
    if n > 1:
       if n % 3 == 0:
           times += DP_num(n/3)
       elif n % 2 == 0:
           times += DP_num(n/2)
       else:
           times +=DP_num(n - 1)

    print (times)
    return times

print(DP_num(5))