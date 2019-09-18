"""
Created By: Rishikesh Vanarse
10/09/2019
"""


"""
Many grid-based/ sampling based algorithms use a 
graph-based shortest-path planner & graph-based optimizer.

Import the required graph-based path planner from here.

Planned Contents:
Dijkstra
Bellman-ford

Visibility graph 

"""

#-----------------------------------------------------------
import numpy
#from shapely.geometry import Polygon


""" 
SHORTEST PATH PLANNERS:

Standard Input format: 
Standard Output format:

"""

def dijkstra():
	pass



def bellmanford();
	pass


"""
OPTIMIZERS

Standard input format:
Standard Output format:
"""

def visibility_graph(path, obstacle_list):
	new_path =[]
	new_path.append(path[0])

	point1 = path[0]
	point2 = path[1]

	for i in range(1, len(path)):
		point2 = path[i]
		for obstacle in obstacle_list:
			if obstacle.intersects(LineString(point1, point2)):
				new_path.append(path[i-1])
				point1 = path[i-1]
				break
			pass
		pass
	new_path.append(path[-1])
	