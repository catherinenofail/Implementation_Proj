import math
import random 
import timeit
#import pylab as pl
#import numpy as np

def makeRandomData(numPoints,radii):
	#"Generate a list of random points within a unit circle.

	# Fill a unit circle with random points.
	t, u , r, x, y = 0, 0, 0, 0, 0
	P = []
	
	for i in range(0,numPoints):
	#random() should be within 0 and 1
		t = 2*math.pi*random.random()
		
		goodR = False
		while (goodR == False): 
			u = random.random()+random.random()
		
			if u > 1:
				r = 2-u
			else:
				r = u
			if r >= radii:
				goodR = True
			else:
				goodR = False
				  
		x = r*math.cos(t)
		y = r*math.sin(t)
		P.append((x, y))

	return P

def convexHull(points):
    """Computes the convex hull of a set of 2D points.
 
    Input: an iterable sequence of (x, y) pairs representing the points.
    Output: a list of vertices of the convex hull in counter-clockwise order,
      starting from the vertex with the lexicographically smallest coordinates.
    Implements Andrew's monotone chain algorithm. O(n log n) complexity.
    """
 
    # Sort the points lexicographically (tuples are compared lexicographically).
    # Remove duplicates to detect the case we have just one unique point.
    points = sorted(set(points))
 
    # Boring case: no points or a single point, possibly repeated multiple times.
    if len(points) <= 1:
        return points
 
    # 2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product.
    # Returns a positive value, if OAB makes a counter-clockwise turn,
    # negative for clockwise turn, and zero if the points are collinear.
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
 
    # Build lower hull 
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
 
    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
 
    # Concatenation of the lower and upper hulls gives the convex hull.
    # Last point of each list is omitted because it is repeated at the beginning of the other list. 
    return lower[:-1] + upper[:-1]

def test():
	start = timeit.default_timer()
	k = 500
	r = 0.1

	numIt = [0] * k
	meanArray = [0] * 4
	stdArray = [0] * 4

	nArray = [20, 100, 500, 2000]
 
	for i in range (0,4):
		n = nArray.pop(0)

		for trials in range (0,k):
 
			p = makeRandomData(n,r)
			iterations = 0

			while len(p) != 0:
				iterations = iterations + 1
				c = convexHull(p)
				while len(c) != 0:
					x = c.pop()
					p.remove(x)
			numIt[trials] = iterations

		mean = 0
		for trials in range (0,k):
			mean += numIt[trials]
		mean = mean/k	
	
		std = 0
		for trials in range (0,k):
			std += (numIt[trials] - mean)**2

		std = (std/k) ** 0.5

		meanArray[i] = mean
		stdArray[i] = std	
	
	#pl.plot(nArray, stdArray)
	#pl.show()

	stop = timeit.default_timer()
	print('For {0} radii...' .format(r))
	print('Algorithm took {0} seconds' .format(stop-start))

test()

