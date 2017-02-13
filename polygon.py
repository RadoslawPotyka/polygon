def polygonArea(coordinates):

    area = 0.0
    for i in range(len(coordinates)):
        j = (i + 1) % n
        area += coordinates[i][0] * coordinates[j][1]
        area -= coordinates[j][0] * coordinates[i][1]

    area = abs(area) / 2.0
    return area
