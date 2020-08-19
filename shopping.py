######## effective main
file = open("data.txt", "r")


#num_items = int(file.readline().strip().split())
nums = int(file.read())
P = []
W = []
for x in xrange(1,nums):
	#for y in xrange(1,):
		for z in line.split():
			P[y] = z
			W[y] = z


	


num_array = [int(x) for x in nums.split(' ')]
out = open("results.txt", "w") #open file to write to

for x in xrange(length): #this is the writing part of the function (to another file)
	if num_array[x] == "[" or num_array[x] == "[": #not sure if I need this part but it breaks if I take it out
		continue
	else:
		out.write(str(num_array[x]))
		out.write(str(" "))
out.close()
