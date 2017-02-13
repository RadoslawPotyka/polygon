import polygon

def get_user_input():
	coordinates = [];
	x = 0

	while(True):
		x = input("Set x value of coordinate. Type e to exit.")
		
		if x == "e":
			break 

		y = float(input("Set y value of coordinate."))
		coordinates.append((float(x),y))

	return coordinates

if __name__ == "__main__":
	print(polygon.polygon_area(get_user_input()))
