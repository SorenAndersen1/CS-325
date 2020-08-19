def badSort(num_array, n, current, pos):

	n = pos - current + 1
	if n == 2 and num_array[current] > num_array[current + 1]:
		num_array[current], num_array[current + 1] = num_array[current + 1], num_array[current]

	elif(n > 2):
		m = a * n
		m = int(m)
		badSort(num_array, n, current, current + m )
		badSort(num_array, n, pos - m , pos )
		badSort(num_array, n, current, current + m )



test = [19, 2, 123, 1, 77, 4, 9, 8]
a = .5
badSort(test, 8, 0, 7)
print(test)