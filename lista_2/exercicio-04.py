import math 

p = dict()
q = dict()

print("Ponto 1:")

# converting to radian
p['lat'] = math.radians(float(input("Latitude º (grau): "))) 
p['lng'] = math.radians(float(input("Longitudeº (grau): ")))

print("\nPonto 2:")

# converting to radian
q['lat'] = math.radians(float(input("Latitudeº (grau): ")))
q['lng'] = math.radians(float(input("Longitudeº (grau): ")))


# fórmula de Haversine
def d(p, q):
	
	distance = None
	r = 6371

	# r ~> 6371 km

	# distance = 2r * arcsin (√( sin²((q_lat - p_lat)/2) + cos(p_lat) * cos(q_lat) * sin²((q_lng - p_lng)/2)))

	# ***** exploding function ***** 

	# 1 part -> sin²((q_lat - p_lat)/2) -> 'sin1'
	sin1 = math.pow(math.sin((q['lat'] - p['lat'])/2), 2)

	# 2 part -> cos(p_lat) 'cos1' and cos(q_lat) -> 'cos2'
	cos1 = math.cos(p['lat'])
	cos2 = math.cos(q['lat'])

	# 3 part -> sin²((q_lng - p_lng)/2) -> 'sin2'
	sin2 = math.pow(math.sin((q['lng'] - p['lng'])/2), 2)

	# 4 part -> √( sin1 + cos1 * cos2 * sin2) -> 'sqrt'
	sqrt = math.sqrt(sin1 + (cos1 * cos2 * sin2))

	# 5 part -> 2r * arcsin (√(sqrt))
	distance = (2 * r) * math.asin(sqrt)

	return distance


print(d(p, q))