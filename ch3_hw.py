# 7.625 = 4 * 1.90625
# 4 = 2 ** 2
# #e10*e9*...e0 - 1023 = 2
# #e10*e9*...e0 = 1025
# #10进制转2进制
# 1025 == 10000000001
# 0.90625 == 111010…0
# 7.625 == 0 | 10000000001 | 111010…0

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