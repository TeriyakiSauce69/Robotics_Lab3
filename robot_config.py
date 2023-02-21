import math
import numpy as np

import robot_model as rm
np.set_printoptions(precision=5, suppress=True)

# 𝑎_𝑖: link length
# 𝛼_𝑖: link twist
# 𝜃_𝑖: joint angle
# 𝑑_𝑖: link offset

link1 = rm.dh_transformation(1, 0, math.pi/2 , 0)
link2 = rm.dh_transformation(1, 0, math.pi/2 , 0)

homo_trans = rm.kinematic_chain([link1, link2])

x, y, z = rm.get_pos(homo_trans)
roll, pitch, yaw, = rm.get_rot(homo_trans)
print("Problem 1, part a :- x = ",x, "y =", y, "z =",z, "roll =", roll, "pitch =",pitch, "yaw =",yaw)

#Case2 putting them all in a array.
case1 = [rm.dh_transformation(0, math.pi / 2, 0, 0.1625),
rm.dh_transformation(-0.425, 0, 0, 0),
rm.dh_transformation(-0.3922, 0, 0, 0),
rm.dh_transformation(0, math.pi/2, 0, 0.1333),
rm.dh_transformation(0, -math.pi/2, 0, 0.0997),
rm.dh_transformation(0, 0, 0, 0.0996)]

#Run them to Kinetic function
homo_trans = rm.kinematic_chain(case1)

#Extract the good stuff.
x, y, z = rm.get_pos(homo_trans)
roll, pitch, yaw, = rm.get_rot(homo_trans)
print("Problem 2, case1 :- x =",x, "y =", y,"z =",z, "roll =", roll, "pitch =",pitch, "yaw =",yaw)

#Case 3 putting them all in a array.
case1 = [rm.dh_transformation(0, math.pi / 2, 0, 0.1625),
rm.dh_transformation(-0.425, 0, -(math.pi / 2), 0),
rm.dh_transformation(-0.3922, 0, 0, 0),
rm.dh_transformation(0, math.pi/2, 0, 0.1333),
rm.dh_transformation(0, -math.pi/2, 0, 0.0997),
rm.dh_transformation(0, 0, 0, 0.0996)]

#Run them to Kinetic function
homo_trans = rm.kinematic_chain(case1)

#Extract the good stuff.
x, y, z = rm.get_pos(homo_trans)
roll, pitch, yaw, = rm.get_rot(homo_trans)
print("Problem 2, case2 :- x =",x, "y =", y, "z =",z, "roll =", roll, "pitch =",pitch, "yaw =",yaw)