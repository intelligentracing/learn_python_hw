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

#ex1.2
#(1)copy its submatrix of [:2,:2] ，the submatrix is：[[7,8],[1,3]]

# a = np.array([[7,8,8],[1,3,8],[9,2,1]])
# new_matrix = a[:2,:2]

# #(2)each column of the submatrix represents a vector and please change its length to one： sqrt(x0*x0 + x1*x1) = 1， and the direction doesn't change，eg：7/math.sqrt(7**2 + 1**2)
# new_matrix_cut = np.ones((2,2))
# new_matrix_cut[0,0] = new_matrix[0,0]/math.sqrt(new_matrix[0,0]**2 + new_matrix[1,0]**2)
# new_matrix_cut[1,0] = new_matrix[1,0]/math.sqrt(new_matrix[0,0]**2 + new_matrix[1,0]**2)
# new_matrix_cut[0,1] = new_matrix[0,1]/math.sqrt(new_matrix[0,1]**2 + new_matrix[1,1]**2)
# new_matrix_cut[1,1] = new_matrix[1,1]/math.sqrt(new_matrix[0,1]**2 + new_matrix[1,1]**2)

# #(3)）dot the submatrix with a rotation of 90 degrees clockwise and print the result。
# def rotationMatrix(degree):
#     '''逆时针旋转角度的函数'''
#     c = np.cos(np.radians(degree))
#     s = np.sin(np.radians(degree))
#     return np.array([[c, -s], [s, c]])

# rotation_matrix = rotationMatrix(270)
# new_matrix_dot = rotation_matrix.dot(new_matrix)
# #Print the matrix after rotation
# print(new_matrix)
# print(new_matrix_dot)

# #(4)use pyplot to display the vectors before and after the transformation in（2）

# #before transformation
# plt.arrow(0,0,new_matrix[0,0],new_matrix[1,0], head_width=0.4, head_length=0.4, color = 'b')
# plt.arrow(0,0,new_matrix[0,1],new_matrix[1,1], head_width=0.4, head_length=0.4, color = 'b')
# #after transformation
# plt.arrow(0,0,new_matrix_cut[0,0],new_matrix_cut[1,0], head_width=0.4, head_length=0.4, color = 'r')
# plt.arrow(0,0,new_matrix_cut[0,1],new_matrix_cut[1,1], head_width=0.4, head_length=0.4, color = 'r')
# plt.axis([0,10,0,10])
# plt.show()
# #(4)use pyplot to display the vectors before and after the transformation in（3）

# plt.figure()#Delete the last image displayed

# #before the rotation: new_matrix_cut
# plt.arrow(5,0,new_matrix[0,0],new_matrix[1,0], head_width=0.4, head_length=0.4, color = 'b')
# plt.arrow(5,0,new_matrix[0,1],new_matrix[1,1], head_width=0.4, head_length=0.4, color = 'b')
# #after the rotation: new_matrix_dot
# plt.arrow(5,0,new_matrix_dot[0,1],new_matrix_dot[1,1], head_width=0.4, head_length=0.4, color = 'r')
# plt.arrow(5,0,new_matrix_dot[0,0],new_matrix_dot[1,0], head_width=0.4, head_length=0.4, color = 'r')
# plt.axis([0,20,-10,10])
# plt.show()