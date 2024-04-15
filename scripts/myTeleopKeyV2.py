#!/usr/bin/env python
import rospy
import termios, sys, os
from turtlesim.srv import TeleportAbsolute, TeleportRelative, Spawn
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from numpy import pi
TERMIOS=termios
lScale=0.5
aScale=0.5
a=bytes('a','utf-8')
d=bytes('d','utf-8')
w=bytes('w','utf-8')
s=bytes('s','utf-8')
r=bytes('r','utf-8')
t=bytes(' ','utf-8')
q=bytes('q','utf-8')
dirty=False
pub = rospy.Publisher('/turtle1/cmd_vel', Twist)
rospy.init_node('velPub', anonymous=False)
vel = Twist()
teleportR = rospy.ServiceProxy('/turtle1/teleport_relative', TeleportRelative)
teleportA = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)

def getkey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c



while(True):
    linear=angular=0
    k=getkey()
    if(k==q):
        print('quit')
        break
    if(k==r):
        resp1 = teleportA(5.544445, 5.544445, 0)
        print('Position Reseted')
        dirty=True
    elif(k==t):
        resp1 = teleportR(0, pi)
        dirty=True
    elif(k==a):
        angular=1
        dirty=True
    elif(k==d):
        angular=-1
        dirty=True
    elif(k==w):
        linear=1
        dirty=True
    elif(k==s):
        linear=-1
        dirty=True
    vel.linear.x = lScale*linear
    vel.angular.z = aScale*angular
    if dirty:
        pub.publish(vel)
        dirty=False