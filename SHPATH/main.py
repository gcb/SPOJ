from sys import stdin

def solve( places, start, end, cost=0):
	print( "---------", start, "-->", end) 
	path = [start]
	if start == end:
		return path, cost
	roads = places[start]["to"]
	for destination, distance in roads.iteritems():
		name = places[destination]["name"]
		print( name )
		if( name != end ):
			pass
			#path.append(solve(places,r, end, visited) )
	return path

cases = int(stdin.next())
case = 1
while case <= cases:
	#print("case:", case, "of", cases)
	case += 1

	places = {}
	byname = {}
	cities = int(stdin.next())
	city = 1

	while city <= cities:
		name = stdin.next().strip("\n")
		#print("city:", city, "of", cities, name)
		places[city] = {'name': name, 'to': {}} # city is 1 based index
		byname[name] = city
		neighbours = int(stdin.next())
		neighbour = 0
		while neighbours > neighbour :
			#print("neighbour:", neighbour, "of", neighbours)
			line = stdin.next().split(' ', 1)
			places[city]['to'][int(line[0])] = int(line[1])
			neighbour += 1
		city += 1
	print(places)
	print(byname)
	
	paths = int(stdin.next())
	path = 1
	while path <= paths:
		print("path:", path, "of", paths)
		p = stdin.next().strip("\n").split(' ',1)
		solve( places, start=byname[p[0]], end=byname[p[1]] )
		path += 1
	




