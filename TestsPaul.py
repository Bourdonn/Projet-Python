# MAIN TEST
#import matplotlib.pyplot as plt

from class_robot import *
from read_map import *

[n,m,nb_rob,obstacles,robots,visited] = ReadFile("Case_Aspi_R_3.txt")

room = Room([n,m],obstacles)

Robots = [Robot(robot,room) for robot in robots]

"""
distances = {}
for Rob in Robots:
    print("Robot ", Rob.get_color(), " position ", Rob.get_position())
    directions = Rob.directions(obstacles, Robots)
    print("directions :",directions)
    distance = Rob.distances(directions, obstacles, Robots)
    print("distances : ", distance , "\n\n")
    distances.update(distance)

print("Premiere ligne de la matrice 'possibilities':\n",distances)
path = []
Rob.move('E',5,room,path,1)
print("Room apres un deplacement:\n",room)
print("path apres un deplacement: ", path)
"SYNTAXE PR SUPPRIMER UN ELT: "
# del distances['BE']
"""
