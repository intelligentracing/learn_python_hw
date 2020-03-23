
def F(n):

    if n == 1:
        return 0

    if F_memory[n]==None:
        min_steps = F(n-1)
        if n%2 == 0:
            min_steps = min(min_steps, F(n//2))
        
        if n%3 == 0:
            min_steps = min(min_steps, F(n//3))

        F_memory[n] = 1 + min_steps
    
    return F_memory[n]

N = 40
F_memory = [None]*(N+1)
F_memory[1] = 0
print(F(N))