import numpy as np
import math

def dh_transformation(link_length, link_twist, joint_angle, link_offset):
    #𝑎_𝑖: link length
    #𝛼_𝑖: link twist
    #𝜃_𝑖: joint angle
    #𝑑_𝑖: link offset

    trans = np.array(
            [[math.cos(joint_angle), -math.sin(joint_angle) * math.cos(link_twist), math.sin(joint_angle) * math.sin(link_twist), link_length * math.cos(joint_angle)],
             [math.sin(joint_angle), math.cos(joint_angle) * math.cos(link_twist), -math.cos(joint_angle) * math.sin(link_twist), link_length * math.sin(joint_angle)],
             [0, math.sin(link_twist), math.cos(link_twist), link_offset],
             [0, 0, 0, 1]])

    return trans

def kinematic_chain(DH):
    #Numpy method to create Transformation Matrix
    #Iterate through row and multiply
    total_transformation = np.identity(4)
    for row in DH:
        total_transformation = np.matmul(total_transformation, row)
    return total_transformation

def get_pos(HT):
    #Return Numpy Matrix Indix Elements
    return HT[0, 3], HT[1, 3],HT[2, 3]

def get_rot(HT):
    #Using atan2 to allow for fraction
    #Returns roll-pith-yaw angles
    return math.atan2(HT[2,1] , HT[2,2]), math.atan2(-HT[2, 0], (math.sqrt(HT[2, 1] + HT[2, 2]))), math.atan2(HT[1 , 0], HT[0 , 0])








