

#### python binary search implement
import random
from time import time


def merge_sort(unsorted_list):
    pass


#divide and conquerer
def quick_sort(unsorted_list):
    quick_sort_partition(unsorted_list, 0, len(unsorted_list) -1)
    
def quick_sort_partition(myList, start, end):
    if start < end:
        pass

def partition(myList, start, end):
    pivot_val = myList[start]
    
    

# slow - O ( n^2 )
def bubble_sort(myList):
    sorted = False
    while not sorted:
        sorted = True
        for j in range(len(myList)-1):
            #flip the number to the end
            if myList[j] > myList[j +1]:
                sorted = False
                temp = myList[j+1]
                myList[j+1] = myList[j]
                myList[j] = temp
    return  myList
            


if __name__ == "__main__":
    
    #generate list
    unsorted_list = random.sample(range(1,1000), 100)
    print(unsorted_list)
    print("------------------")
   
    #bubble sort 
    t = time()
    sorted_list = bubble_sort(unsorted_list)
    print("Bubble sort: {}".format( time() - t))
    
    print(sorted_list)