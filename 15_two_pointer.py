#two pointers are used for ,1 - searching - search for median, or predefined substructure, that satisfy certain conditions such as finding minimum subarray length where in subarray equals to targeteted sum. or finding sub structure satisfy string pattern
# 2. adjusting - adjust ordering or arrangement of items in data stucture such as removing duplicates from sorted array

# 1. slow fast pointers:
# two pointers i and j , where one moves fasters and other moves slower
# algorthm is called sliding window algorithm
# application 1: remove duplicates from sorted array

from os import remove


def removeDuplicates(array):
    fast,slow = 0,0
    while(fast<len(array)):
        if(array[slow]!=array[fast]):
            slow+=1
            array[slow]=array[fast]
        fast+=1
    return slow+1,array[:slow+1]

if __name__=="__main__":
    array = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicates(array))
    print(array)