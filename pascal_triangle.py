def pascal_triangle(n):

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

result = pascal_triangle(n)
print(result)

for row in result:
    print_string = ' '*(n - len(row))
    for index in range(len(row)):
        print_string = print_string + str(row[index]) + ' '
    print(print_string)