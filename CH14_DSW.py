import os 
from matplotlib import image
from matplotlib import pyplot
#第一题
try:
    source_filename = 'nasdaqlisted.txt'
    result_filename = 'result.txt'
    # Obtain current python file's path
    path = os.path.dirname(os.path.abspath(__file__))
    # Open source file and the result file
    source_handle = open(path+'/'+source_filename,'r')
    result_handle = open(path+'/'+result_filename,'w')
    company = []
    for line in source_handle:
        line_list = list(line)
        num_list = []
        for i in range(len(line_list)):
            if '|' == line_list[i]:
                num_list.append(i)
        company_name_list = line_list[num_list[0] + 1:num_list[1]]
        company_name = "".join(company_name_list)
        company.append(company_name)
    company_sort = sorted(company)
    for x in range(len(company_sort)):
        result_handle.write(company_sort[x])
except IOError:
    print('IO Error! Please check valid file names and paths')
    exit
finally:
    source_handle.close()
    result_handle.close()
#第二题
# Read an image file
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/' + 'lenna.bmp'
data = image.imread(filename)

# Display image information
print('Image type is: ', type(data))
print('Image shape is: ', data.shape)

# Add some color boundaries to modify an image array
plot_data = data.copy()
for width in range(512):
    for height in range(10):
        plot_data[height][width] = [255, 0, 0]
        plot_data[511-height][width] = [0,0,255]

# use pyplot to plot the image
pyplot.imshow(plot_data)
pyplot.show()