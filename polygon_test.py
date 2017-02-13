import polygon

def polygon_test():
	test_data1 = [(4.0, 4.0), (1.0, 1.0), (1.0, 4.0), (4.0, 1.0)]
	test_data2 = [(1.0, 2.0), (3.0, 4.0), (2.0, 5.0)]

	test_file = open("test_results.txt", "w")
	print("created test_results.txt")
	result1 = polygon.polygon_area(test_data1)
	result2 = polygon.polygon_area(test_data2)
	text = "Test data 1 {0} \n Result: {1} \n test data 2 {2} \n Result: {3}".format(test_data1, result1, test_data2, result2)

	test_file.write(text)
	test_file.close()
	print("Test successfull ...")

if __name__ == "__main__":
	polygon_test()