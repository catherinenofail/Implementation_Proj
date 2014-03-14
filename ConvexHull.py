import math
import random 
import timeit

def makeRandomData(numPoints):
	#"Generate a list of random points within a unit circle."
	# numPoints = 10

	# Fill a unit circle with random points.
	t, u , r, x, y = 0, 0, 0, 0, 0
	P = []
	
	for i in range(0,numPoints):
	#random() should be within 0 and 1
		t = 2*math.pi*random.random() 
		u = random.random()+random.random()
		
		if u > 1:
			r = 2-u
		else:
			r = u  
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
	n = 3000 
	p = makeRandomData(n)
	iterations = 0

	while len(p) != 0:
		iterations = iterations + 1
		c = convexHull(p)
		#print('There are {0} points in p' .format(len(p)) )
		#print('There are {0} convex hull points' .format(len(c)))
		pop = 0 
		while len(c) != 0:
			x = c.pop()
			p.remove(x)

	stop = timeit.default_timer()
	print('For {0} vertices...' .format(n))
	print('Algorithm took {0} seconds' .format(stop-start))
	print('There are {0} iterations' .format(iterations)) 

test()

