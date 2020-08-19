Insertsort: This works exactly like the books pseudocode, execept I use pythons features to swap the elements.
First the data is read in and then placed into an array, which has a known length. This length is the base of the
actual function, in which compares each element swapping the element when it finds an approriate spot 
(i.e. x < z < y where z is the element and x and y are the elements to the -1 and +1 spaces)

Mergesort: This one is closer to the books pseudocode, as I tried to stay as close as possible to the books implementation
After using the exact same lines as insertsort to read in "data.txt"'s information the function is called  on the newly made array
This function is simply a helper function that acts as the recursive body for the entire system, calling itself on the subsections
of the array. This is where the divide and conquer comes in, as this helper function breaks down the entire array into single parts
The subsection'd array is then analyzed to find the how each number should be ordered in the subsection, then put into the main array (nums).

Both the timed versions of these algorithims use the same code to time it. In a for loop the there are arrays generated 7 times at size
intervals of 5000 that have randomly generated numbers from 1 to 10000, the time is taken before the function starts, then when the function ends,
then subtracted from each other.