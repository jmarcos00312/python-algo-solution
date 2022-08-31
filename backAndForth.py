
# Input Mutated
# def arrange(s):
#     copiedList = s
#     finalList =[]
#     middle = ""
#     if len(copiedList) % 2 !=0:
#         middle =copiedList[int(len(copiedList)/2)]
#         copiedList.pop(copiedList[int(len(copiedList)/2)])

#     while len(copiedList):
#         finalList += [copiedList[0], copiedList[-1]]
#         copiedList.remove(copiedList[0])
#         copiedList.remove(copiedList[-1])
#         copiedList.reverse()
#         if middle:
#             finalList.append(middle)
    
#     return finalList



# ===============================================================


def arrange(s):
    # creating an empty list
    finalList = []
    # setting a variable of left and right
    left, right = 0, len(s)-1
    # looping through each item via index of the list
    for idx in range(len(s)):
    # if i is divisible by 2
        if (idx+1//2) % 2 == 0:
            # add the current item
            finalList.append(s[left])
            # move the pointer to the next item to the right of it
            left += 1
            # if i is not divisible by 2
        else:
            # add the last item
            finalList.append(s[right])
            # move the pointer to the next item to the left of it
            right -= 1
    return finalList



print(arrange([9, 7, -2, 8, 5, -3, 6, 5, 1, 3]))


