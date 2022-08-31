# def wave(people):
#     finalWave = []
#     splitPeople = list(people)
#     pos = 0
#     toJoin = ""
#     peeps = people
#     while pos != len(splitPeople):
#         if peeps[pos] != peeps[pos+1]:
#             finalWave.append(peeps.replace(peeps[pos],peeps[pos].upper()))
#         elif peeps[pos] == peeps[pos].upper():
#             pass
#         pos+=1
        
#     return finalWave
        
        
def wave(people):

    waveList=[]
    # looping through the string
    for i in range(len(people)):
        # print(i)
        # capitallize the letter that we are currently in
        capLetter=people[i].upper()
        # add the capitalized letter to the rest of the 
            # eachWOrdCapped = Hello => hEllo => heLlo => helLo => hellO
        eachWordCapped=people[:i] + capLetter + people[i+1:]
# [].append("Hello") => [Hello].append("hEllo") => [Hello, hEllo].append("HeLlo") => [Hello, hEllo, HeLlo].append("HelLo") => [Hello, hEllo, HeLlo, HelLo].append("HellO") => [Hello, hEllo, HeLlo, HelLo, HellO] => end
        waveList.append(eachWordCapped)
    print(waveList)
        




print(wave("hello")) # => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
# print(wave("Codewars")) # => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]



# def wave(str):
#     # Code here
#     if str == []:
#         return []
#     else:
#         result = []
#         for i in range(len(list(str))):
#             # if 0 does not equal to white space
#             if str[i] != " ":
#                 str_update = list(''.join(str).lower())
#                 str_update[i] = str_update[i].upper()
#                 result.append(''.join(str_update))
#         return result