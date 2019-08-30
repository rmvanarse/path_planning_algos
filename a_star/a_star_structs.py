"""
Created by: Rishikesh Vanarse

30/08/2019
"""

"""
Import file to driver (astar.py)
Assumoptions:
 --------------------------------------------------------------
|	Global vars in driver: nodes[], source, dest, node_count
|	Global functions: h_func(node, dest)
 --------------------------------------------------------------
"""

class Node_astar:
	
	def __init__(self, name, pos, adj_list):
		#Elements of adj_list: touples - (neighbour_name, edge_weight)
		self.neighbours = []

		self.name = name
		#preferably integer

		self.pos = pos
		#pos = point (x,y)

		for N in adj_list:
			self.neighbours.append(N)
		
		self.h=heristic(self, dest)		
		#Global nodes array -
		nodes.append(self)
		node_count = node_count+1


def heuristic(node, dest, multiplier = 1.5):
	#d(node, dest)*multiplier
	pass