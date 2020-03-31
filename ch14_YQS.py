import os
from matplotlib import image
from matplotlib import pyplot
import numpy

#ex1.1
source_filename = 'nasdaqlisted.txt'
result_filename = 'result.txt'#储存结果的文件

try:
    # Obtain current python file's path
    path = os.path.dirname(os.path.abspath(__file__))
    # Open source file and the result file
    source_handle = open(path+'/'+source_filename,'r')
    result_handle = open(path+'/'+result_filename,'w')
    #提取source_filename中前两个"|"之间的股票公司名称
    #方法：将每一行转变为list, 得到前两个“|”所在的位置索引，最后再每一行这两个索引之间的值输出
    company = []#为存放股票公司全称所事先定义的空列表
    for line in source_handle:
        line_list = list(line)#将每一行变成一个list
        num_list = []#w为存放索引所事先定义的空列表
        for i in range(len(line_list)):
            if '|' == line_list[i]:
                num_list.append(i)
        company_name_list = line_list[num_list[0] + 1:num_list[1]]#只取前两个“|”所在的位置索引，所以是num_list[0] + 1:num_list[1]
                                                                  #得到股票公司全称
        company_name = "".join(company_name_list)#将股票公司全称转化为字符串形式，然后加入到事先定义好的company空列表中
        company.append(company_name)
    company_sort = sorted(company)#按照字母顺序进行排序

    #将排序好的列表中的每一个字符串元素，写入我们事先定义的result.txt中
    for x in range(len(company_sort)):
        result_handle.write(company_sort[x])
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