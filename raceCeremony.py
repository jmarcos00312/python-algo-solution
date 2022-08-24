def race_podium(blocks):
    secondPlace = round(blocks/3 + 2/3)
    lastPlace = round(blocks/3 -2)
    firstPlace = blocks - secondPlace - lastPlace
    if lastPlace == 0:
        lastPlace = 1
        secondPlace -= lastPlace
    podium = [secondPlace, firstPlace, lastPlace]
    
    return podium








# print(race_podium(11)) #, (4,5,2))
print(race_podium(100000)) #, (33334,33335,33331))
# print(race_podium(10)) #,(4,5,1))
print(race_podium(7)) #, (2,4,1)
print(race_podium(8)) #, (3,4,1)