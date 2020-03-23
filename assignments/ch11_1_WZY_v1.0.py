def F(best_step):
    temp_step=best_step[-1]
    if temp_step%3==0:
        temp_step=min(temp_step,temp_step/3)
    if temp_step%2==0:
        temp_step=min(temp_step,temp_step/2)
    if temp_step!=1:
        temp_step=min(temp_step,temp_step-1)
    best_step.append(temp_step)
    if temp_step==1:
        return best_step
    else:
        return F(best_step)

i=100
best_step =[i]
print(str(F(best_step)))
    