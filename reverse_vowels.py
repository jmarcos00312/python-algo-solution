# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:
    # Input: s = "hello"
    # Output: "holle"

# Example 2:
    # Input: s = "leetcode"
    # Output: "leotcede"
    
    
def reverseVowels(s):
    # creating a list of the vowels
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    # making the input to a list
    edited = list(s)
    # adding a place holder variable to hold the extracted vowels
    place_holder = []
    # looping through each char in s
    for char in s:
        # if the current item is in vowels
        if char in vowels:
            # append it to our place holder
            place_holder.append(char)
            # now loop through the s that was made it to array
    for i in range(len(edited)):
        # if our current position is in vowels
        if edited[i] in vowels:
            # we take the last item from the place holder and set it to the current postition
            edited[i] = place_holder.pop()
            # now join the edited list to a string
    return ''.join(edited)

s = "hello"
print(reverseVowels(s))