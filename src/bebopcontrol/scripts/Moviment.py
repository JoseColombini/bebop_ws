'''
    FAVOR CORRIGIR A INCOERENCIA NO MOVIMENTO USADA APENAS PARA TESTAR
    POIS ESTAVA DANDO ERRO DE IDENTACAO????
'''

import rospy
import time ## controlling the time
from geometry_msgs.msg import Twist ## controlling the velocity
import os

velocity_message = Twist()


#New way of trating moviment
#y is the distance
#s is the speed [0, 1]
def set_y_relative_position(y, s):

    '''
    Input:
    (x,y,z) = vector of position
    (s) = speed that will be used in this case

    Task:
    publish velocity messages during the time linked to position
    '''

    global velocity_message

    #Note that the user will enter with the absolute value of Position
    #So the y will discribe the direction (positive or negative)
    vel = 4.0*s
    time_duration = abs(float(y/vel))

    print(time_duration)

    timeout = time.time() + time_duration # 0.5 minutes from now

    while True:

        if y > 0:
            #print(time.time())

			velocity_message.linear.x = 0.0
			velocity_message.linear.y = s
			velocity_message.linear.z = 0.0
			velocity_position_pub.publish(velocity_message)

			rate.sleep()



        if y < 0:

            velocity_message.linear.x = 0.0
            velocity_message.linear.y = s
            velocity_message.linear.z = 0.0
            velocity_position_pub.publish(velocity_message)

            rate.sleep()

            if time.time() > timeout:

                #print("[ bebop2 WARN] Position reached! x: %f y: %f z: %f" % abs_position_x, abs_position_y, abs_position_z)


                return



rospy.init_node('Bebop_2_Position_Control')

rate = rospy.Rate(20) # publish at 20 [Hz]

velocity_position_pub = rospy.Publisher('/bebop/cmd_vel', Twist, queue_size=10)

os.system("./bebop_takeoff.sh")

time.sleep(5)

print("[ bebop2 WARN] Takeoff succesfully")


set_y_relative_position(-1.2, 0.1)

time.sleep(2)


os.system("./land.sh")

print("[ bebop2 WARN] Land succesfully")
