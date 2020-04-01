import os
from matplotlib import image
from matplotlib import pyplot
import numpy

#ex1.1
source_filename = 'nasdaqlisted.txt'
result_filename = 'result.txt'  # 储存结果的文件

try:
    # Obtain current python file's path
    path = os.path.dirname(os.path.abspath(__file__))
    # Open source file and the result file
    source_handle = open(path + '/' + source_filename, 'r')
    result_handle = open(path + '/' + result_filename, 'w')
    #方法：用spilt()函数以'|'符号将每一行分成包含公司名称的列表
    company = []#为存放股票公司全称所事先定义的空列表

    for line in source_handle:
        line_list = line.split('|')#以'|'为分隔符，将每一行分成几个字符串组成的列表，其中第一个'|'和第二个'|'之间为公司名称
        company.append(line_list[1])#line_list[0]是ticker,line_list[1]是公司名称所以将line_list[1]添加到company中
    sorted_company = sorted(company)#对company排序
#将排序好的公司名称列表sorted_company里的元素依次添加到result.txt文件中
    for i in range(len(sorted_company)):
        result_handle.write(sorted_company[i])

        result_handle.write('\n\r')#该行作用是为了每添加一个公司名称就换一行


except IOError:
    print('IO Error! Please check valid file names and paths')
    exit
finally:
    source_handle.close()
    result_handle.close()
#ex1.2

# Read an image file
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/' + 'lenna.bmp'
filename1 = path + '/' + 'lena10.jpg'#读取lena10.jpg图像，它的文件位置要和lenna.bmp在一起
data = image.imread(filename)
data1 = image.imread(filename1)

# Add some color boundaries to modify an image array
plot_data = data.copy()
plot_data1 = data1.copy()
plot_data2 = data.copy()#为了求差值图所事先定义的图像
#为计算平均差值所事先定义的分别三个通道的差值总和
r_sum = 0
g_sum = 0
b_sum = 0
for width in range(512):
    for height in range(512):
        plot_data2[height][width] = abs(plot_data[height][width] -plot_data1[height][width] )#计算差值图
        r_sum += plot_data2[height][width][0]#R通道的差值总和
        g_sum += plot_data2[height][width][1]#G通道的差值总和
        b_sum += plot_data2[height][width][2]#B通道的差值总和
r_average = r_sum / (512* 512)#R通道的差值平均
g_average = g_sum / (512* 512)#G通道的差值平均
b_average = b_sum / (512* 512)#B通道的差值平均

# use pyplot to plot the image，显示差值图
pyplot.imshow(plot_data2)
pyplot.show()

print(r_average,g_average,b_average)
