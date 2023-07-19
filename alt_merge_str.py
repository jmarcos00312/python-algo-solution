# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.
# ================= answer is at the bottom =================










































def mergeAltStr(word1, word2):
    word1_len = len(word1)
    word2_len = len(word2)
    i = 0 # word1 index
    j = 0 # word2 index
    final = []
    
    while i < word1_len or j < word2_len:
        if i < word1_len:
            final.append(word1[i])
            i+=1
        # final = ["a"]
        # i = 1
            # final = ["a", "q", "b"]
            # i = 2
                # final = ["a", "q", "b", "w"]
                # j = 2
                # END
        if j < word2_len:
            final.append(word2[j])
            j+=1
        # final = ["a", "q"]
        # j = 1
            # final = ["a", "q", "b", "w"]
            # j = 2
                # final = ["a", "q", "b", "w", "e"]
                # j = 3
                    # final = ["a", "q", "b", "w", "e", "r"]
                    # j = 4
            
    result = ''.join(map(str, final))
    return result
            
    
    # while 0 is less than word1 length or j is less than word2 length
        # if i is less than word1 length:
            # append word1[i] to final then add 1 to move one
        # if j is less than word2 length:
            # append word1[j] to final then add 1 to move one
            
    # join to make it string


print(mergeAltStr("ab", "qwer"))