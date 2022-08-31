def solution(number):
    toTotal = 0
    for x in range(number):
        if x % 3 == 0 or x % 5 == 0:
            toTotal += x
    return toTotal


  
  
  
print(solution(16))