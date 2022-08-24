# def solution(n):
#     # n = 984
#     bluePrintDict = {
#         "M" : 1000,
#         "CM": 900,
#         "D" : 500,
#         "CD": 400,
#         "C" : 100,
#         "XC": 90,
#         "L" : 50,
#         "XL": 40,
#         "X" : 10,
#         "IX": 9,
#         "V" : 5,
#         "IV": 4,
#         "I" : 1,
#         }
#     blueprintKeys = list(bluePrintDict)
#     subtracted = n
#     final = ""
#     pos = 0
#     # while the argument is greater than 0
#         # if the argument - the value of the key that we are in is greater than or equals to 0
#             # add the dictionary key that we are in to the final string
#             # and subtract the value of that key to the argument
#         # else add 1 to the position 
#     while subtracted > 0:
#         #     n       -      1000 = -999 so the else statement runs and move to the next item in the dictionary bc its not greater than or equal to 0
#         if subtracted - bluePrintDict[blueprintKeys[pos]] >= 0:
#             final += blueprintKeys[pos]
#             subtracted -= bluePrintDict[blueprintKeys[pos]]
#         else:
#             pos += 1
            
            
#     # TODO convert int to roman string
#     return final




# print(solution(1))
# print(solution(4))
# print(solution(6))
# print(solution(14))
# print(solution(1))
# print(solution(89))
# print(solution(91))
# print(solution(984))
# print(solution(1000))
# print(solution(1989))


def solution(n):
    roman_numerals = {
        1000:'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    roman_string = ''
    for key in sorted(roman_numerals.keys(),reverse=True):
        print(key)
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    print(sorted(roman_numerals.keys()))
    return roman_string
print(solution(984))