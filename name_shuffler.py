from turtle import st


def name_shuffler(str):
    strToArr = str.split(' ')
    strToArr.sort()
    return " ".join(strToArr)
    




print(name_shuffler('john McClane'))