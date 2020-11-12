#Midium2 ex1_print_function.py
#Author: Yu Qiuhsuang

# def pascal_triangle(x,y):
#     '''x:第几行
#        y:第几个数
#        '''
#     if x == 1 and y == 1:
#         return 1
#     elif x < 1 or y < 1:
#         return 0
#     else:
#         return pascal_triangle(x - 1, y - 1) + pascal_triangle(x - 1, y)
# N = 11
# for x in range(1, N + 1):
#     for y in range(1, N - x + 1):
#         print("", end=' ')
#     for z in range(1, x + 1):
#         print(pascal_triangle(x, z),end=" ")
#     print()

def triangle(num):
    triangle=[[1]]
    for i in range(2,num+1):
        # i means to get the new line for the triangle
        triangle.append([1]*i)
        #refresh the value in the pascal triangle 
        for j in range(1,i-1):
            # next line's value equal to the sum of the last line's before value and next value
            triangle[i-1][j]=triangle[i-2][j]+triangle[i-2][j-1]
    return triangle
    
def printtriangle(triangle,width):
    #column is the length of the last line
    column=len(triangle[-1])*width
    #sublist is every row in the triangle
    for sublist in triangle:
        result=[]
        for contents in sublist:
            #'{0:^{1}}'is use to make contents in the middle of the line and the lenght of the line is width
            result.append('{0:^{1}}'.format(str(contents),width))
        print('{0:^{1}}'.format(''.join(result),column))
        
if __name__=='__main__':
    num=int(input('num:'))
    triangle=triangle(num)
    # width is the interval between two elements, and the interval is dynamic adjust
    # according to the middle element's digits
    print(str(triangle[-1][len(triangle[-1])//2]))
    width=len(str(triangle[-1][len(triangle[-1])//2]))+1
    printtriangle(triangle,width)
