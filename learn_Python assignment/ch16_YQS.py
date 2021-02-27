import numpy as np
import matplotlib.pyplot as plt
import math

#ex1.1
# def rotationMatrix(degree):
#     '''input: A function of the counterclockwise rotation Angle
#        output:rotation matix
#     '''
#     c = np.cos(np.radians(degree))
#     s = np.sin(np.radians(degree))
#     return np.array([[c, -s], [s, c]])

# input_times = input('input any time in XX:XX format：')

# #Input_times is a string format in which the time is extracted by the spilt function
# #['8','10']
# input_times_spilt = input_times.split(':')
# hours = int(input_times_spilt[0])#Change from string to integer format
# minutes = int(input_times_spilt[1])

# #The Angle of rotation in the hour hand, because the rotation matrix is rotating counterclockwise, 
# # so you have to subtract it from 360
# if hours > 12:
#     hours = hours - 12
#     hours_degree = 360 - (30 * (hours + minutes/60))
# else:
#     hours_degree = 360 - (30 * (hours + minutes/60))
# minutes_degree = 360 - (6 * minutes)

# #The original vectors of the hour hand and the minute hand, they represent in the x and y coordinates
# #the vertical and vertical lengths are 1 and 2, respectively
# #vecter transpose
# v1 = np.array([[0.,1.]]).T 
# v2 = np.array([[0.,2.]]).T 
# rotation_hours = rotationMatrix(hours_degree)
# rotation_minutes = rotationMatrix(minutes_degree)

# #dot product and get the rotated version of the vector
# v1_new = rotation_hours.dot(v1)#shape of rotation hours(2,2) ; shape of v1(2,1); shape of v1_new(2, 1)
# v2_new = rotation_minutes.dot(v2)

# #print results
# plt.arrow(0,5,v1_new[0, 0],v1_new[1, 0], head_width=0.2, head_length=0.4, color = 'b')
# plt.arrow(0,5,v2_new[0, 0],v2_new[1, 0],head_width=0.2, head_length=0.4, color = 'r')

# #Parameter represents the value range of horizontal and vertical coordinates
# plt.axis([-5,5,0,10])
# plt.show()


#ex1.2
#(1)copy its submatrix of [:2,:2] ，the submatrix is：[[7,8],[1,3]]

a = np.array([[7,8,8],[1,3,8],[9,2,1]])
new_matrix = a[:2,:2]

#(2)each column of the submatrix represents a vector and please change its length to one： 
# sqrt(x0*x0 + x1*x1) = 1， and the direction doesn't change，eg：7/math.sqrt(7**2 + 1**2)
new_matrix_cut = np.ones((2,2))
new_matrix_cut[0,0] = new_matrix[0,0]/math.sqrt(new_matrix[0,0]**2 + new_matrix[1,0]**2)
new_matrix_cut[1,0] = new_matrix[1,0]/math.sqrt(new_matrix[0,0]**2 + new_matrix[1,0]**2)
new_matrix_cut[0,1] = new_matrix[0,1]/math.sqrt(new_matrix[0,1]**2 + new_matrix[1,1]**2)
new_matrix_cut[1,1] = new_matrix[1,1]/math.sqrt(new_matrix[0,1]**2 + new_matrix[1,1]**2)

#(3)）dot the submatrix with a rotation of 90 degrees clockwise and print the result。
def rotationMatrix(degree):
    '''逆时针旋转角度的函数'''
    c = np.cos(np.radians(degree))
    s = np.sin(np.radians(degree))
    return np.array([[c, -s], [s, c]])

rotation_matrix = rotationMatrix(270)
new_matrix_dot = rotation_matrix.dot(new_matrix)
#Print the matrix after rotation
print(new_matrix)
print(new_matrix_dot)

#(4)use pyplot to display the vectors before and after the transformation in（2）

#before transformation
plt.arrow(0,0,new_matrix[0,0],new_matrix[1,0], head_width=0.2, head_length=0.4, color = 'b')
plt.arrow(0,0,new_matrix[0,1],new_matrix[1,1], head_width=0.2, head_length=0.4, color = 'b')
#after transformation
plt.arrow(0,0,new_matrix_cut[0,0],new_matrix_cut[1,0], head_width=0.2, head_length=0.4, color = 'r')
plt.arrow(0,0,new_matrix_cut[0,1],new_matrix_cut[1,1], head_width=0.2, head_length=0.4, color = 'r')
plt.axis([0,10,0,10])
plt.show()
#(4)use pyplot to display the vectors before and after the transformation in（3）

plt.figure()#Delete the last image displayed

#before the rotation: new_matrix
plt.arrow(5,0,new_matrix[0,0],new_matrix[1,0], head_width=0.2, head_length=0.4, color = 'b')
plt.arrow(5,0,new_matrix[0,1],new_matrix[1,1], head_width=0.2, head_length=0.4, color = 'b')
#after the rotation: new_matrix_dot
plt.arrow(5,0,new_matrix_dot[0,1],new_matrix_dot[1,1], head_width=0.2, head_length=0.4, color = 'r')
plt.arrow(5,0,new_matrix_dot[0,0],new_matrix_dot[1,0], head_width=0.2, head_length=0.4, color = 'r')
plt.axis([0,20,-10,10])
plt.show()







# #ex1.2

# # Initialization, define some constant
# path = os.path.dirname(os.path.abspath(__file__))
# filename = path + '/airplane.bmp'
# background = plt.imread(filename)

# second_hand_length = 200
# second_hand_width = 2
# minute_hand_length = 150
# minute_hand_width = 6
# hour_hand_length = 100
# hour_hand_width = 10
# center = np.array([256, 256])

# def clock_hand_vector(angle, length):
#     return np.array([length * np.sin(angle), -length * np.cos(angle)])

# # draw an image background
# fig, ax = plt.subplots()

# while True:
#     plt.imshow(background)
#     plt.axis('off')#不显示横纵坐标
#     # First retrieve the time
#     now_time = datetime.now()
#     hour = now_time.hour + now_time.minute / 60 + now_time.second /3600#把当前的分钟和秒钟也变换为小时，换算成时针需要转的角度
#     if hour>12: hour = hour - 12
#     minute = now_time.minute + now_time.second / 60#把当前的秒钟也变换为分钟，换算成分针需要转的角度
#     second = now_time.second

#     # Calculate end points of hour, minute, second

#     hour_vector = clock_hand_vector(hour/12*2*np.pi, hour_hand_length)
#     minute_vector = clock_hand_vector(minute/60*2*np.pi, minute_hand_length)
#     second_vector = clock_hand_vector(second/60*2*np.pi, second_hand_length)

#     plt.arrow(center[0], center[1], hour_vector[0], hour_vector[1], head_length = 3, linewidth = hour_hand_width, color = 'black')
#     plt.arrow(center[0], center[1], minute_vector[0], minute_vector[1], linewidth = minute_hand_width, color = 'black')
#     plt.arrow(center[0], center[1], second_vector[0], second_vector[1], linewidth = second_hand_width, color = 'red')

#     plt.pause(0.1)#根据pyplot绘制图像，每隔0.1s执行一遍
#     plt.clf()
