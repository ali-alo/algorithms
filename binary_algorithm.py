# Binary algorithm works with the sorted list/arrays. It determines the mid point of the list and then if the number
# does not match guess, it removes half of the list (upper or lower depends on the number location)
# This step is repeated until the number is found or until there are elements in the list


def binary_search(array, number):
    lowest = 0  # set the lowest item of the array
    highest = len(array) - 1  # set the highest number in the array

    while lowest <= highest:  # keep repeating code below while we have elements inside of the array
        mid = (lowest + highest) // 2  # determine the mid point. double slashes are used to floor floating numbers
        guess = array[mid]  # store representing mid point of the array in the guess variable
        if guess == number:  # congratulations we found a number
            return mid  # return index of that number inside of the array
        elif guess > number:  # if the number is LESS than the guess, do not go through higher numbers anymore
            highest = mid - 1
        else:  # if the number is BIGGER than the guess, do not go through lower numbers anymore
            lowest = mid + 1
    return None  # if the number is not in the list return None


test_array = [1, 2, 3, 5, 7, 8, 9, 14, 28, 52]

print(binary_search(test_array, 4)) # prints None
print(binary_search(test_array, 28))  # prints 8


# binary algorithm is written as ( log2(n) ). Where:
# 2 is the base, because every time we decrease the list by two
# n is the number of elements in the array/list
# if the logarithm equation gives floating number, we round it up to the integer

# That is, in the worst scenario it would take 4 steps to my program to find the number  (log2(10) ≈ 3.32)
