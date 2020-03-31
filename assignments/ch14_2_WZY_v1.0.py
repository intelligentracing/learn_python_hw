from matplotlib import image
from matplotlib import pyplot
import os
def list_avarage(l):
    tot=0
    for i in range (len(l)):
        tot+=l[i]
    return tot/len(l)

# Read an image file
path = os.path.dirname(os.path.abspath(__file__))
lenna1 = path + '/' + 'lenna.bmp'
lenna2 = path + '/' + 'lena10.jpg'
data1 = image.imread(lenna1)
data2 = image.imread(lenna2)

# Add some color boundaries to modify an image array
plot_data = data1.copy()
avarage_list_R=[]
avarage_list_G=[]
avarage_list_B=[]
for width in range(512):
    for height in range(512):
        temp_R=abs(data1[height][width][0]-data2[height][width][0])
        temp_G=abs(data1[height][width][1]-data2[height][width][1])
        temp_B=abs(data1[height][width][2]-data2[height][width][2])
        plot_data[height][width] = [temp_R, temp_G, temp_B]
        avarage_list_R.append(temp_R)
        avarage_list_G.append(temp_G)
        avarage_list_B.append(temp_B)
avarage_R=list_avarage(avarage_list_R)
avarage_G=list_avarage(avarage_list_G)
avarage_B=list_avarage(avarage_list_B)
# use pyplot to plot the image
pyplot.imshow(plot_data)
print("the avarage for R is ",avarage_R,"for G is ",avarage_G,"for B is ",avarage_B)
pyplot.show()