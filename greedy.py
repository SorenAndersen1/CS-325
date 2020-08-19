import math

out = open("change.txt", "w")


def coinfunc(c, k, n):

    store_arr = [0] * (k + 1) #set store_arr to one bigger than k just to be safe, and all 0s
    denom_arr = [0] * (k + 1) #Need this to be all 0s just in case.
    store_arr[k] = 1 #couldnt get this to work in the next for loop so just hard coded it
    for i in range(0, k):
        store_arr[i] = pow(c, k - i) #easy power function thank you python
        #denom_arr[i] = 0
    for j in range(0, k + 1):
        while (n >= store_arr[j]): #bulk of this algo, simple comparison between "weight" and price
            n -= store_arr[j] #if it can subtract it, since we are going from the top (greedy)
            denom_arr[j] += 1 #save how many of each denom are used
    for j in range(0, k + 1):
        out.write("Denomination: %s Quantity: %s \n" % (store_arr[j], denom_arr[j])) #print the array to file




def main():
  #  file = open("data.txt", "r")


   # data = file.read()
   # num_array = []
    i = 0



    with open('data.txt') as file: #out
        for line in file:
            num_array = list(map(int, line.split()))
            out.write("Data Input: c = %s , n = %s , k = %s \n" % (num_array[0],num_array[1], num_array[2])) #formatting stuff

            coinfunc(num_array[0], num_array[1], num_array[2])









    out.close() #closes file


if __name__ == "__main__": main()



