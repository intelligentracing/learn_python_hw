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
plot_data = lenna_bmp.copy()
plot_data1 = lenna_jpg.copy()

#An image defined in advance in order to evaluate the difference graph
plot_data2 = lenna_bmp.copy()
print(plot_data2)


#The sum of the differences of the three channels defined in advance to calculate the average difference
r_sum = 0
g_sum = 0
b_sum = 0
for width in range(512):
    for height in range(512):
        plot_data2[height][width] = abs(plot_data[height][width] -plot_data1[height][width] )#Calculate the difference graph
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









import numpy as np
import matplotlib.pyplot as plt
import math
#ex1.1

def rotationMatrix(degree):
    '''input: A function of the counterclockwise rotation Angle
       output:rotation matix
    '''
    c = np.cos(np.radians(degree))
    s = np.sin(np.radians(degree))
    return np.array([[c, -s], [s, c]])

input_times = input('input any time in XX:XX format：')

#Input_times is a string format in which the time is extracted by the spilt function
input_times_spilt = input_times.split(':')
hours = int(input_times_spilt[0])#Change from string to integer format
minutes = int(input_times_spilt[1])

#The Angle of rotation in the hour hand, because the rotation matrix is rotating counterclockwise, so you have to subtract it from 360
hours_degree = 360 - (30 * (hours + minutes/60))
minutes_degree = 360 - (6 * minutes)

#The original vectors of the hour hand and the minute hand, they represent in the x and y coordinates
#the vertical and vertical lengths are 1 and 2, respectively
v1 = np.array([[0.,1.]]).T 
v2 = np.array([[0.,2.]]).T 
rotation_hours = rotationMatrix(hours_degree)
rotation_minutes = rotationMatrix(minutes_degree)

#dot product and get the rotated version of the vector
v1_new = rotation_hours.dot(v1)#shape of rotation hours(2,2) ; shape of v1(2,1); shape of v1_new(2, 1)
v2_new = rotation_minutes.dot(v2)

#print results
plt.arrow(0,5,v1_new[0, 0],v1_new[1, 0], head_width=0.4, head_length=0.4, color = 'b')
plt.arrow(0,5,v2_new[0, 0],v2_new[1, 0],head_width=0.4, head_length=0.4, color = 'r')

#Parameter represents the value range of horizontal and vertical coordinates
plt.axis([-5,5,0,10])
plt.show()

