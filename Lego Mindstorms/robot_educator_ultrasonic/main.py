#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Ultrasonic Sensor Driving Base Program
-----------------------------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""
# import os
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor, TouchSensor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the Ultrasonic Sensor. It is used to detect
# obstacles as the robot drives around.
obstacle_sensor = UltrasonicSensor(Port.S2)
stop = TouchSensor(Port.S1)

# Initialize two motors with default settings on Port B and Port C.
# These will be the left and right motors of the drive base.
left_motor = Motor(Port.D)
# positive_direction=Direction.COUNTERCLOCKWISE
right_motor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
lever_motor = Motor(Port.B)
# The DriveBase is composed of two motors, with a wheel on each motor.
# The wheel_diameter and axle_track values are used to make the motors
# move at the correct speed when you give a motor command.
# The axle track is the distance between the points where the wheels
# touch the ground.
robot = DriveBase(left_motor, right_motor, wheel_diameter=70, axle_track=170)

# Play a sound to tell us when we are ready to start moving
ev3.speaker.beep()

# The following loop makes the robot drive forward until it detects an
# obstacle. Then it backs up and turns around. It keeps on doing this
# until you stop the program.


# def clearConsole():
#     command = 'clear'
#     if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
#         command = 'cls'
#     os.system(command)


turn = 0

base_speed = 0
currrent_speed = base_speed

lever = {"up" : -330,
"down": -128}

dist = {
    "min" : 82,
    "mid" : 135,
    "max" : 179
}

def move():
    robot.drive(currrent_speed,turn)

    if obstacle_sensor.distance() < 500:
        turn = 50
        forward_speed = base_speed*0.7

    if obstacle_sensor.distance() > 500:
        turn = 0
        forward_speed = base_speed

    while obstacle_sensor.distance() < 50:
        turn = 0
        forward_speed = 0

# def print_dist():
#         if abs(prev - obstacle_sensor.distance()) > 5:
#         # print(abs(prev - obstacle_sensor.distance()))
#         prev = obstacle_sensor.distance()
#         print(obstacle_sensor.distance())




# dist.min
# dist["min"]
c = 0
ratio = 0.9
speed = 90
ac = 0
while True:
    if stop.pressed():
        robot.drive(0,0)
        break

    robot.drive(speed,0)
    distance = obstacle_sensor.distance()
    dist_diff = distance - dist["mid"]
    c += 1
    
    if c > 1000:
        if speed < 400:
            speed += 30
        if ac > -80:
            lever_motor.run(+20)
            ac += +20
        print("Distance:")
        print(dist_diff)
        print("Angle:")
        print(lever_motor.angle())
        c = 0


    if 


    # if not (lever_motor.angle() > -330 and lever_motor.angle() < -128):
    #     continue



    # if abs(dist_diff) > 5:
    #     if dist_diff > 0: 
    #         lever_motor.run(dist_diff*ratio)
        
    #     if dist_diff < 0: 
    #         lever_motor.run(dist_diff*ratio)

    # print(dist["min"])



    

    # robot.straight(-100)
