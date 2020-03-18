def pascal_triangle(n):

    if type(n)!=int:
        raise TypeError('Argument 1 must be integer.')
    elif n<=0:
        raise ValueError('Argument 1 integer must be > 0 for the pascal triangle level.')
    triangle = []
    triangle.append([1])
    for row in range(1, n):
        row_list = []
        row_list.append(1)
        for index in range(1, row):
            row_list.append(triangle[row-1][index-1] + triangle[row-1][index])
        
        row_list.append(1)
        triangle.append(row_list)
    
    

    return triangle

n = 8

result = pascal_triangle(5)
print(result)

for row in result:
    print_string = ' '*(n - len(row))
    for index in range(len(row)):
        print_string = print_string + str(row[index]) + ' '
    print(print_string)