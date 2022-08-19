def switcheroo(s):
    newStrin = ""
    for x in s:
        if x == "a":
            newStrin+= "b"
        elif x == "b":
            newStrin+= "a"
        else:
            newStrin += x
    return newStrin

    
print(switcheroo("abcde"))