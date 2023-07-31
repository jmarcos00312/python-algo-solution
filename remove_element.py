def removeElement(nums, val):
    result = len(nums)
    x = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[i] = nums[x]
            x+=1
        else:
            result-=1
        
    return result
            


# arr = [3,2,2,3]

# val = 3
arr = [0,1,2,2,3,0,4,2]
val = 2


print(removeElement(arr, val))

# Input arraya  == arr
# Value to remove == val

# The expected answer with correct length.
# It is sorted with no values equaling val.
# Calls your implementation
# assert k == ex
# Sort the first k elements of nums
