# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, 
# return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

# Example 1:
        # Input: flowerbed = [1,0,0,0,1], n = 1
        # Output: true
        
# Example 2:
        # Input: flowerbed = [1,0,0,0,1], n = 2
        # Output: false
 
def canPlaceFlowers(flowerbed, n):
        if len(flowerbed) <= 2:
                return False
        
    # Iterate through the flowerbed to check for available spots to plant flowers
        for i in range(len(flowerbed)):
        # If the current spot is empty (0), we can potentially plant a flower
                if flowerbed[i] == 0:
            # Check if it's safe to plant a flower at the current spot:
                        if i == 0 or flowerbed[i-1] == 0:
                                if i == len(flowerbed) - 1 or flowerbed[i+1] == 0:
                                        n -= 1
                                        flowerbed[i] = 1
        if n <= 0:
                return True
        else:
                return False

print(canPlaceFlowers(flowerbed = [1,0,0,0,0,1], n = 2))
# print(canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2))
# print(canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1))

    # Iterate through the flowerbed to check for available spots to plant flowers
        # If the current spot is empty (0), we can potentially plant a flower
            # Check if it's safe to plant a flower at the current spot:
            # 1. If the current spot is the first position (i == 0) or the previous spot is empty (flowerbed[i - 1] == 0).
            # 2. If the current spot is the last position (i == len(flowerbed) - 1) or the next spot is empty (flowerbed[i + 1] == 0).
                    # Increment the counter since we can plant a flower here
                    # Plant a flower at the current spot (update flowerbed[i] to 1)

    # After iterating through the flowerbed, check if we have enough empty spots to plant n flowers