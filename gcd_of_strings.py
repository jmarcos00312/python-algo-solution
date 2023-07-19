# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.


def gcd_of_string(str1, str2):
# Step 1: Finding the GCD
#   The length of str1 is 6, and the length of str2 is 3.
#   The GCD of 6 and 3 is 3.
# Step 2: Extracting Substring
#   We extract a substring of length 3 from either str1 or str2.
#   Let's choose str1 and extract the substring "ABC".
# Step 3: Checking if the Substring Divides Both Strings
#   We compare if the substring "ABC" can be repeated to form both str1 and str2.
#   We concatenate the substring to itself to form "ABCABC".
#   If str1 + str2 is equal to the repeated substring, we have found the largest string that divides both strings.
# Step 4: Decreasing the Substring Length
#   If the substring did not divide both strings, we decrease its length by 1.
#   The new substring becomes "AB".
#   We repeat Step 3 to check if the new substring divides both strings.
#   We continue decreasing the substring length until a common divisor is found or the length becomes 0.
# In this example, the largest string that divides both str1 and str2 is "ABC". 
# We visually examined the process of finding the common substring and checked if it divides both strings by repeating it. 
# If no common divisor is found, we return an empty string.
    pass