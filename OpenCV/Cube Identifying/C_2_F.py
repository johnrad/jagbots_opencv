import rospy
from std_msgs.msg import Int8

print('Initiating')

def convert_to_f(data):
    while not rospy.is_shutdown():
        celsius_temp = data.data
        fahrenheit_temp = ((1.8)*(celsius_temp)+32)
        #print(fahrenheit_temp)
        
        pub = rospy.Publisher('f_temp', Int8, queue_size=10)
        #rospy.init_node('celsius_receiver', anonymous=True)
        rate = rospy.Rate(10)
    
        rospy.loginfo(fahrenheit_temp)
        pub.publish(fahrenheit_temp)
        rate.sleep()

def celsius_receiver():
    rospy.init_node('celsius_receiver', anonymous=True)

    rospy.Subscriber('raw_temp', Int8, convert_to_f)

    rospy.spin()




if __name__ == '__main__':
    try:
        celsius_receiver()
    except rospy.ROSInterruptException:
        pass
