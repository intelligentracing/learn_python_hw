# def deleteNode(head, val):
#     """
#     :type head: ListNode
#     :type val: int
#     :rtype: ListNode
#     """
#     value = 0
#     for i in head:
#         if i == val:
#             head.pop(head[value + 1])
#         else:
#             value += 1
#     return head

# print(deleteNode([4,5,1,3], 5))

# def run_in_series(self, next_waypoint: Transform, **kwargs) -> VehicleControl:
#     throttle = self.long_pid_controller.run_in_series(next_waypoint=next_waypoint,
#                                                         target_speed=kwargs.get("target_speed", self.max_speed))
#     steering,x,y,z= self.lat_pid_controller.run_in_series(next_waypoint=next_waypoint)
#     if y>0.8 or (x>-390 and x<0 and z<91):
#         if steering>0:
#             steering=0.01
#         else:
#             steering=-0.01


# if steering>-0.4 and steering<-0.05 and y<0.8 and x<0:
#         steering=steering*1.3
#     if x> 360 and x<390 and z>-60 and z<20:
#         throttle=0.9
#         steering = 0.9
#     if x> -570 and x<-420 and z<80 and z>10:
#         # throttle=0.9
#         steering = -0.4




def do_twice(a,b):
   return func(a,b), func(a,b)

def func(a,b):
    c = a + b
    print(c)

func(1,2)
print(do_twice(1,2))