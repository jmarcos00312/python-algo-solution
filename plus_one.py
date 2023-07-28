def plusOne(nums):
    list_to_string = (''.join(str(x) for x in nums))
    str_to_int = int(list_to_string)
    str_to_int += 1
    newlist = [int(i) for i in str(str_to_int)]
    return newlist
    print(type(str_to_int))
    
    
    
    
print(plusOne([1,2,3,4,5,6,7]))