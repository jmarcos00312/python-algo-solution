# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array





def missing_number(nums):
    for i in range(len(nums) + 1):
        if i not in nums:
            return i
        
        
    
nums_1 = [9,6,4,2,3,5,7,0,1]
nums_2 = [3,0,1]
nums_3 = [0,1]
print(missing_number(nums_1))
print(missing_number(nums_2))
print(missing_number(nums_3))