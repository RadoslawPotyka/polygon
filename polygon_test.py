import polygon

def polygon_test():
	test_data1 = [(1.0, 1.0), (4.0, 1.0), (1.0, 4.0), (4.0, 4.0)]
	test_data2 = [(1.0, 2.0), (3.0, 4.0), (2.0, 5.0)]

	with open("test_results.txt", "w") as test_file:
		result1 = polygon(test_data1)
		result2 = polygon(test_data2)
		text = "Test data 1 {0} \n Result: {1} \n test data 2 {3} \n Result: {4}".format(test_data1, result1, test_data2, result2)

		test_file.write(text)
		print("Test successfull ...")