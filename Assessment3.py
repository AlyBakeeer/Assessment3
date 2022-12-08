from roboticstoolbox import Bicycle, RandomPath, VehicleIcon, RangeBearingSensor, LandmarkMap
from math import pi , atan2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg #implementing the classes used in the code

#Asking the user to enter the wanted coordinates
initx= float(input('Please enter the x coordinate you want to start from'))
inity= float(input('Please enter the y coordinate you want to start from'))
goalx= float(input('Please enter the x-axis coordinates of your goal'))
goaly= float(input('Please enter the y-axis coordinates of your goal'))
obst= int(input('Please enter the number of obstacles you want'))

anim = VehicleIcon('robo', scale = 3) #giving the code the name and the size of the picture to run it on the map
init_pos=(0,0) #starting point
veh_init=(plot=True)

veh = Bicycle(
    animation=anim,
    control=RandomPath,
    dim=100,  
) #figure's dimension

initial=[initx,inity] #defining the initial coordinates given by the user
goal=[goalx,goaly] #defining the goal coordinates given by the user

veh.init(plot=True)
map = LandmarkMap( 5, 50) #loading the map with the given Landmarks
map.plot()

sensor=RangeBearingSensor(robot=veh,map=map,animate=True) #rangebearing sensor

print('Sensor readings: \n', sensor.h(veh.x))
veh._animation.update(veh.x)
plt.pause(1000) #reading the output of the sensor

anim = VehicleIcon('robo', scale= 3)
veh = Bicycle(
    animation=anim,
    control=RandomPath,
    x0=(0,0,1.5),
    y0=(0,0,1.5), #inital position
)



background = import matplotlib('map.png', scale=5) #loading the given map with the exact size

def detect_obstacles(readings): #used to read if ther is any obstacle in a certain range
    for i in readings:
        if (i[0] < 4 and abs(i[1]) < pi/3):
            return False
        else:
            veh.step(0.5,0)
            veh._animation.update(veh.x)
            plt.pause(0.02)
run= True

run= True #the code that is used to stop the vehicle when it reads an obstacle
while (run):
    for i in sensor.h(veh.x):
        if (i[0] < 3):
            if(abs(i[1]) < pi/4):
                run = False
        else:
            veh.step(0.5,0)
            veh._animation.update(veh.x)
            plt.pause(0.02)
plt.pause(10)


while (run): #a function used to detect if there an obstacle so it can stop within a certain range
    if(detect_obstacles(sensor.h(veh.x)) is False):
        run = False
plt.pause(10)

map = LandmarkMap(5,10) #adding the map with the wanted size
map.plot()
image = mpimg.imread("map.png")
plt.imshow(image, extent = [-5,5,-10,10])
plt_pause=(10)

if:   #conditions to make sure the user choose a coordinate that is in the map 
    goalx < 1
    print('this coordinate cannot be used, please enter a number higher than one')
    goaly < 1
    print('this coordinate cannot be used, please enter a number higher than one')

if: #condition used to make sure the vehicle will not hit an obstacle
    input != for goalx list(2,3,5)
    input != for goaly list(1,2,3,6,7,8,9,10)
plt_pause=(1000)

print(veh.x,veh.y)
