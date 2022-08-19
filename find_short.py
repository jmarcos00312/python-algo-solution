def find_short(s):
    argsToList = s.split(' ')
    l = len(argsToList[0])
    # your code here
    for x in argsToList:
        if len(x) < l:
            l = len(x)
    return l # l: shortest word length








print(find_short("bitcoin take over the world maybe who knows perhaps"))