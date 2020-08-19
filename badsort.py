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





######## effective main
file = open("data.txt", "r")


nums = file.read() 
length = nums[0]
data = nums[2:] #ignore first element as it specifies the length(nums)
a = sys.argv[1]
a = float(a)
length = (int(length))
num_array = [int(x) for x in data.split(' ')]
out = open("bad.out", "w") #open file to write to
badSort(num_array, int(length), 0, int(length) - 1) #call insert func
print(num_array)

for x in xrange(length): #this is the writing part of the function (to another file)
	if num_array[x] == "[" or num_array[x] == "[": #not sure if I need this part but it breaks if I take it out
		continue
	else:
		out.write(str(num_array[x]))
		out.write(str(" "))
out.close()




