


def insertsort(nums, length):
	out = open("insertsort.out", "w") #open file to write to
	for x in range(0, length):
		end = x
		while end > 0 and nums[end] < nums[end - 1]: #if the element to the left is bigger, do insertion 
			nums[end], nums[end - 1] = nums[end - 1], nums[end] #Basically the most important part, this does the insertion by swapping the elements of the list
			end -= 1 #Go back another position
	for x in range(length): #this is the writing part of the function (to another file)
		if nums[x] == "[" or nums[x] == "[": #not sure if I need this part but it breaks if I take it out
			continue
		else:
			out.write(str(nums[x]))
			out.write(str(" "))
	out.close()


######## effective main
file = open("data.txt", "r")


nums = file.read() 
length = nums[0]
data = nums[2:] #ignore first element as it specifies the length

length = int(length)
num_array = [int(x) for x in data.split(' ')]
insertsort(num_array, length) #call insert func




