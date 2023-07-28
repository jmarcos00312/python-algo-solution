def mySqrt(x):
    if x == 0:
        return 0

    # Initialize the range for the binary search
    low, high = 0, x

    # Perform binary search until low becomes greater than high
    while low <= high:
        # Calculate the middle value
        mid = (low + high) // 2

        # Calculate the square of the middle value
        square = mid * mid

        # Check if the square of the middle value matches the given number
        if square == x:
            return mid
        elif square < x:
            # If the square is less than the given number, update the lower bound (low)
            # The square root lies in the range [low, mid]
            low = mid + 1
        else:
            # If the square is greater than the given number, update the upper bound (high)
            # The square root lies in the range [mid+1, high]
            high = mid - 1

    # When low becomes greater than high, we have found the largest integer
    # whose square is less than or equal to x. So, the square root is high.
    return high

# Test cases
print(mySqrt(4))  # Output: 2 (The square root of 4 is 2)
print(mySqrt(8))  # Output: 2 (The square root of 8 is between 2 and 3. We round down to 2.)
print(mySqrt(9))  # Output: 3 (The square root of 9 is 3)
print(mySqrt(0))  # Output: 0 (The square root of 0 is 0)

print(mySqrt(25))  # Output: 0
