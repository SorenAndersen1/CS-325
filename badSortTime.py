import random
import time
import sys


def badSort(num_array, n, current, pos):

	n = pos - current + 1
	if n == 2 and num_array[current] > num_array[current + 1]:
		num_array[current], num_array[current + 1] = num_array[current + 1], num_array[current]

	elif(n > 2):
		m = a * (n - 1)
		m = int(m)
		if(a == n):
			m -= 1
		badSort(num_array, n, current, current + m )
		badSort(num_array, n, pos - m , pos )
		badSort(num_array, n, current, current + m )






a = sys.argv[1]
a = float(a)



for itr in range(1, 8):

	num_array = [0] * 50 * itr #set iterations and array size
	start = time.clock() #take in time
	length = len(num_array) #size of array

	for x in xrange(1,(50 * itr)):
		num_array[x] = random.randint(0, 10000)
	badSort(num_array, int(length), 0, int(length) - 1) #call insert func
	print( itr * 50)
	print((time.clock() - start )) #state total time




