'''
    Suppose you are given an array of sorted integers 
    that has been circularly shifted K positions to the right. 
    For example taking (1 3 4 5 7) and circularly shifting it 2 positions to the right
    you get (5 7 1 3 4). 
    Design an efficient algorithm a number X in the array in O(log n) time.
'''
def main():
    '''
    Thought Process:
        + First, find a pivot point by dividing the given array into two sub-array. O(1)
        + If the pivot point is greater than the leftmost
            Then the pivot point belong the left portion.
        + Else the pivot point belongs to the right portion
        + Then, we need to look for the  
        + Perform binary search to look for a pivot point --> O(logN)
        + 
    '''
    input_array = [4, 5, 6, 7, 0, 1, 2, 3]
    left, right = 0, len(input_array) - 1
    target = 3
    while left <= right:
        mid = (left + right) // 2
        if input_array[mid] == target:
            print('Target value: {} at the index {}'.format(input_array[mid], mid))
        
        #if the target is located in the left sorted portion of the array
        if input_array[left] <= input_array[mid]:
            #Check the target
            if target < input_array[left] or target > input_array[mid]:
                left = mid + 1
            else:
                right = mid - 1
        #If the target is located in the right sorted portion of the array
        else:
            if target < input_array[mid] or target > input_array[right]:
                right = mid - 1
            else:
                left = mid + 1
    print('No target is found!!!')
    a = (5 + 4)//2
    print(a)
     
if __name__=='__main__':
    main()