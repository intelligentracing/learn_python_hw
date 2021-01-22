#ex1.(1)
p2 = Rp1 + T
p2 -T = Rp1
inv(R)(p2 -T) = p1
p1 = inv(R)p2 - inv(R)*T

R' = inv(R)
T' = inv(R)*T

#ex1.(2)
M = [R T; 0, 1]
M = np.asarray([[R[0,0], R[0,1], R[0,2], T[0]],
                              [R[1,0], R[1,1], R[1,2], T[1]],
                              [R[2,0], R[2,1], R[2,2], T[2]],
                              [0.0, 0.0, 0.0, 1.0]])
