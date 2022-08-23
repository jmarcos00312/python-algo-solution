def find_it(seq):
    # making a empty dictionary
    seqTodict = {}
    # looping through the argument list
    for x in seq:
        # .get(x, 0)
        # x is the key to be searched in the dictionary
        # 0 is the value to be returned if the key is not found
        #  if its the first time since x is not found in keys, it will set the value to 0
        # if x is in the dictionary, it will add 1
        seqTodict[x] = seqTodict.get(x, 0) + 1
        # looping through the object
    for item in seqTodict:
        # if the of item's remainder divided by 2 is not equal to 0 then we return that item
        if(seqTodict[item] % 2 != 0):
            return item
    



print(find_it([1,1,1,1,1,1,10,1,1,1,1])) # should return 10
