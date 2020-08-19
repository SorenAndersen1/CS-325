import random
import time
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

itr = 1
for itr in range(1, 8): #generate array 7 times

	num_array = [0] * 5000 * itr #intervals of 5000 like instructions say
	start = time.clock() #takes system clock
	length = len(num_array) 

	for x in xrange(1,(5000 * itr)):
		num_array[x] = random.randint(0, 10000) 
	helpermerge(num_array) #call function with array
	print( itr * 5000) #print what size it was
	print((time.clock() - start )) #print the time to console

