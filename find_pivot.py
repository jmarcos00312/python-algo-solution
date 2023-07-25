# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.

#





def pivot_index_2 (nums):
    total = sum(nums)
    left = 0
    right = 0
    for i,x in enumerate(nums):
        right = total - x- left
        if left == right:
            return i
        left += x
    return -1









def pivotIndex(nums):
    # add up the array
    total_sum = sum(nums)
    # initializing the sum for the left side
    left = 0
    
        # loop through the array
    for i in range(len(nums)):
        # new variable: the right side is the sum of the array minus the current item and the left side
        right = total_sum - nums[i] - left
        # if the left side is the same as the right side of the index
        if left == right:
            # return it
            return i
        # if not we add the current index to the left
        left += nums[i]
        # move to the next item
    return -1
  
  
  
nums = [1,7,3,6,5,6]
# print(pivotIndex(nums))
print(pivot_index_2(nums))