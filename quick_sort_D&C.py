# D&C stands for Divide and Conquer and in computer science it is an algorithm design. D&C design contains two steps:
# firstly, we determine the simplest case and solution a problem, which is called the base case.
# secondly, we divide or decrease the problem until it becomes the base case.


# Let's imagine we have a task to sum all the elements of the array [2, 4, 6] but we cannot use loops.

# The first step from the D&C here is to identify the base case. It is if need to sum no or one element only
# like [7] = 7 or [] = 0

# Now we need to move closer to the base case. That is, decrease the number of elements inside the array to one
# 2 + sum([4, 6]) = sum([2, 4, 6])

def my_sum(array):
    if len(array) == 0:
        return 0
    else:
        return array[0] + my_sum(array[1:])


print(my_sum([2, 4, 6]))  # prints 12


# Task: write a recursive function to count the number of elements in a list

def count(array):
    if len(array) == 0:
        return 0
    return 1 + count(array[1:])


print(count([1, 5, 3, 9]))  # prints 4


# Task: write a recursive function to find the maximum number in a list

def max_number(array):
    if len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]
    sub_max = max_number(array[1:])
    return array[0] if array[0] > sub_max else sub_max


print(max_number([5324, 9, 123, 513, 352]))
# binary algorithm is also a D&C algorithm with the base case = (1 element left in the array) and recursive case is
# when we every time divide the whole list of elements by two


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([3, 1, -5, 83, 1, 3, 5, 9, 13, 52]))  # prints [-5, 1, 1, 3, 3, 5, 9, 13, 52, 83]










