"""
Created by: Rishikesh Vanarse

03/09/19

Different ways of sampling for points
"""

"""
Import numpy in the RRT file

"""
def basic_sampling(x_min, x_max, y_min, y_max):
	y_range = y_max-y_min
	x_range = x_max-x_min
	(x,y) = (x_min + x_range*np.random.rand(), y_min + y_range*np.random.rand())


