Introduction: The goal of this assesment was to use the functions, classes, libraries, etc. that we learned from the previous weeks. We wrote a code that should create a map and will give the user the option to choose the coordinates that he wants the vehicle to reach. the vehicle is coded to not hit any obstacle as asked in the assessment.

First, we implemented the classes needed to make the code work. let me explain briefly what each class does. 1- Bicycle: Represents the kinematics of the vehcle. 2- RandomPath: Represents the vehicle's driver which will make he vehicle to move freely so it would not hit an obstacle. 3- VehicleIcon: Shows the graphical photo chosen to represent the vehicle. 4- RangeBearingSensor: Imports the sensors and the bearings used in the code. 5- LandmarkMap: Models a 2D enviroment which will be used to import the map. 6- pi & atan2: will be used to calculate the range needed to move away from the obstacle. 7- matplotlib.pyplot: Responsible for creating the map. 8- numpy: Makes the symbolic operation to work. 9- matplotlib.image: Responsible for importing the wanted images.

from roboticstoolbox import Bicycle, RandomPath, VehicleIcon, RangeBearingSensor, LandmarkMap from math import pi , atan2 import matplotlib.pyplot as plt import numpy as np import matplotlib.image as mpimg

This part of the code should result to printing the questions between apostrophes since the user should give all the information of his goal, initial coordinates, and number of obstacles.

initx= float(input('Please enter the x coordinate you want to start from')) inity= float(input('Please enter the y coordinate you want to start from')) goalx= float(input('Please enter the x-axis coordinates of your goal')) goaly= float(input('Please enter the y-axis coordinates of your goal')) obst= int(input('Please enter the number of obstacles you want'))

This line is responsible for showing the vehicle's photo and its size.

anim = VehicleIcon('robo', scale = 3)

The inital points in the map.

init_pos=(0,0) veh_init=(plot=True)

This part is responsible for importing the classes needed, defining "anim", and giving the figure's dimensions.

veh = Bicycle( animation=anim, control=RandomPath, dim=100, )

Responsible for using the user's inputs of the starting and ending coordinates.

initial=[initx,inity] goal=[goalx,goaly]

This part of the code is responsible for loading the map with the specified coordinates.

veh.init(plot=True) map = LandmarkMap( 5, 50) map.plot()

Used to activate the RangeBearingSensor class.

sensor=RangeBearingSensor(robot=veh,map=map,animate=True)

Responsible for reading the output of sensor to sense if there is any obstacle near the vehicle.

print('Sensor readings: \n', sensor.h(veh.x)) veh._animation.update(veh.x) plt.pause(1000)

Loading the Vehicle's image with a specified size in the initial coordinates.

anim = VehicleIcon('robo', scale= 3) veh = Bicycle( animation=anim, control=RandomPath, x0=(0,0,1.5), y0=(0,0,1.5), )

Loading the map image with a specified scale.

background = import matplotlib('map.png', scale=5)

This part is responsible for calculating the distance between the Vehicle and the obstacle.

def detect_obstacles(readings): for i in readings: if (i[0] < 4 and abs(i[1]) < pi/3): return False else: veh.step(0.5,0) veh._animation.update(veh.x) plt.pause(0.02) run= True

This part is responsible for moving the vehicle away from the obstacle.

run= True #the code that is used to stop the vehicle when it reads an obstacle while (run): for i in sensor.h(veh.x): if (i[0] < 3): if(abs(i[1]) < pi/4): run = False else: veh.step(0.5,0) veh._animation.update(veh.x) plt.pause(0.02) plt.pause(10)

Responsible for stoping the vehicle within a certain range.

while (run): if(detect_obstacles(sensor.h(veh.x)) is False): run = False plt.pause(10)

This part is responsible for addidng the image map of the given map in a certain coordinates.

map = LandmarkMap(5,10) e map.plot() image = mpimg.imread("map.png") plt.imshow(image, extent = [-5,5,-10,10]) plt_pause=(10)

This part is responsible for checking the inserted coordinates are found in the map.

if:
goalx < 1 print('this coordinate cannot be used, please enter a number higher than one') goaly < 1 print('this coordinate cannot be used, please enter a number higher than one') else: veh._animation.update(veh.x,veh.y) plt_pause=(10)

This part is responsible for not entering a coordinate that already contains a wall.

if: input != for goalx list(2,3,5) input != for goaly list(1,2,3,6,7,8,9,10) plt_pause=(1000)

This is the final step after running all the code.

print(veh.x,veh.y)

A) The code was written by Aly Bakeer & Abdelrahman Elhagin. We both worked at all the points together after revising the Lab handouts. we used the gaps between the classes and we met outside the university several times to complete the project since we ran into errors.

B) The required user inputs was the initial coordinates, the final coordinates, and the number of obstacles wanted.

C) We used Ubuntu 18.04, Virtual Studio to write the code.

D) The code is supposed to use the user's input to move the vehicle towards wanted goal without hitting an obstacle.

E) The code would have been better if the obstacles where moving at slow pace and the vehicle would use the senors to now colapse with any obstcle.

Conclusion: In conclusion, we have learned how to use Robotics Toolbox which can be used in real life in several ways. We could apply this code on a reel robot wich can move in any environment without colapsing with any wall, obstacle, person, etc..
