def polygon_area(coordinates):
    length = len(coordinates)
    area = 0.0
    
    for i in range(length - 1):
        j = (i + 1) % length
        area += abs(coordinates[i][0] * coordinates[j][1] - coordinates[j][0] * coordinates[i][1])
    area = area / 2.0
    return area
