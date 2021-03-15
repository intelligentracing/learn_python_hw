import os
from matplotlib import image
from matplotlib import pyplot
import numpy

#ex1.1
source_filename = 'nasdaqlisted.txt'
result_filename = 'result.txt'  # the file that stores the results

try:
    # Obtain current python file's path
    path = os.path.dirname(os.path.abspath(__file__))
    # Open source file and the result file
    source_handle = open(path + '/' + source_filename, 'r')
    result_handle = open(path + '/' + result_filename, 'w')

    #method：Use the spilt() function to split each line into a list of company names with the '|' symbol
    #An empty list defined in advance to hold the full name of the stock company
    company = []

    for line in source_handle:
        #With the '|' delimiter, divide each line into a list of several strings, with the company name between the first '|' and the second '|'
        #lLine_list [1] is the name of the company so line_list[1] is added to the company
        line_list = line.split('|')
        #print(line_list)
        company.append(line_list[1])
    sorted_company = sorted(company)#The company in order

    #Add the elements from the sorted list of company names sorted_company to the result.txt file
    for name in sorted_company:
        result_handle.write(name)

        result_handle.write('\n\r')#It is used to change a line for each company name added


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
filename1 = path + '/' + 'lena10.jpg'#read lena10.jpg，the location of it is the same with lenna.bmp
lenna_bmp = image.imread(filename)
lenna_jpg = image.imread(filename1)

# Add some color boundaries to modify an image array
# plot_data = lenna_bmp.copy()
# plot_data1 = lenna_jpg.copy()

#An image defined in advance in order to evaluate the difference graph
plot_data2 = lenna_bmp.copy()
print(plot_data2)


#The sum of the differences of the three channels defined in advance to calculate the average difference
r_sum = 0
g_sum = 0
b_sum = 0
for width in range(512):
    for height in range(512):
        plot_data2[height][width] = abs(lenna_bmp[height][width] -lenna_jpg[height][width] )#Calculate the difference graph
        r_sum += plot_data2[height][width][0]#Sum of the differences of R channels
        g_sum += plot_data2[height][width][1]#Sum of the differences of G channels
        b_sum += plot_data2[height][width][2]#Sum of the differences of B channels
r_average = r_sum / (512* 512)#The average difference of R channels
g_average = g_sum / (512* 512)#The average difference of G channels
b_average = b_sum / (512* 512)#The average difference of B channels

# use pyplot to plot the image，display difference graph
pyplot.imshow(plot_data2)
pyplot.show()

print(r_average,g_average,b_average)