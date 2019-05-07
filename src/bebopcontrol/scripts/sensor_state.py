'''
Code made to aquire the altitude from ultrassonic sensor

The sensor just send massages when the altitude change, if there is no
change, it just do nothing at the topic, so the object "sensor"
will show the same altitude before
'''

import rospy
from bebop_msgs.msg import Ardrone3PilotingStateAltitudeChanged
import time

#need to set parameter true for the sensor start to transmit
rospy.set_param('~states/enable_pilotingstate_altitudechanged', True)

sensor = Ardrone3PilotingStateAltitudeChanged()

def sensor_state (bat):
    global sensor
    sensor = bat

rospy.init_node('Bebop_2_Altitude')

rate = rospy.Rate(5)

#always remember to write "/bebop/" before the topic that exist in the documentation
rospy.Subscriber('/bebop/states/ardrone3/PilotingState/AltitudeChanged', Ardrone3PilotingStateAltitudeChanged, sensor_state)

i = 0

while i < 10:
    print (sensor.altitude)
    i = i + 1
    time.sleep(3)
    rate.sleep()
