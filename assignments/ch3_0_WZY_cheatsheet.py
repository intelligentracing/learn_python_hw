accuracy = 5 #  小数部分精度
string="Give me your float"
num = input(string)
if num == int(float(num)): #判断是否为浮点数
    integer = str(bin(num)) #若为整数
    integer = integer[2:]        
    print(integer)
else:#若为浮点数
    integer = int(float(num))#取整数部分
    flo = float(num) - float(integer)#取小数部分      
    integercom = str(bin(integer))#整数部分进制转换
    integercom = integercom[2:]
    tem = flo#小数部分进制转换
    tmpflo = []
    for i in range(accuracy):
        tem *= 2
        tmpflo += str(int(tem))
        tem -= int(tem)
        flocom = tmpflo
    print(integercom + '.' + ''.join(flocom))
    