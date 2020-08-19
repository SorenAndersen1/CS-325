def mergesort(nums, left, right):

		x = 0 # Setting all iterators to 0 to start
		y = 0
		z = 0

		n1 = len(left) #length variables, the book illustrated the importance
		n2 = len(right)

		while x < n1 and y < n2: #while the iterators are still in the bounds for this subsection
			if left[x] <= right[y]:  #swap if right is bigger than left
				nums[z] = left[x] #left is the smaller element, thus the first element put back into the array
				x = x + 1 #continue comparisons
			else:
				nums[z] = right[y] #left was bigger, thus right goes first
				y = y + 1
			z = z + 1 #comparison continues

		while x < n1:
			nums[z] = left[x] #this is at the end of the comparison of subsection, this copies any elements left over
			x += 1 
			z += 1

		while y < n2:
			nums[z] = right[y] #same thing as above but just with right
			y += 1 
			z += 1



def helpermerge(nums):
	if len(nums) > 1: #BASE CASE FOR RECURSION
		half = len(nums) // 2 #interger not float
		left = nums[:half]
		right= nums[half:] #splits the array in half, thank god for python

		helpermerge(left) #recusive calls
		helpermerge(right)
		mergesort(nums, left, right) #actual sort call (on smallest section (recusive stair step back up))


#effective main
file = open("data.txt", "r")


nums = file.read()
length = nums[0]
data = nums[2:] #copied from my insertion sort

length = int(length)
num_array = [int(x) for x in data.split(' ')] #change info over to list of integers
helpermerge(num_array) 
length = len(num_array) #double check
out = open("mergesort.out", "w")
for x in range(length):
	if num_array[x] == "[" or num_array[x] == "[":
		continue
	else:
		out.write(str(num_array[x]))
		out.write(str(" "))
out.close()