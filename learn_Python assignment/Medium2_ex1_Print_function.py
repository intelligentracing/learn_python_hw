#Midium2 ex1_print_function.py
#Author: Yu Qiuhsuang

#get each line values for the triangle and save them in the triangle list
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
    # according to the middle element's digits, and the last number you add is free by yourself
    print(str(triangle[-1][len(triangle[-1])//2]))
    width=len(str(triangle[-1][len(triangle[-1])//2]))+3
    printtriangle(triangle,width)
