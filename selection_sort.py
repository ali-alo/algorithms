# When we want to select a particular list or array we use selection sort.
# Selection sort is a type of sorting algorithm
# It receives an array and then creates a new array with sorted (ascending in this example) items

def find_smallest(array):
    smallest = array[0]  # store the smallest value
    smallest_index = 0  # store the index if the smallest element
    for i in range(1, len(array)):  # loop for every other element in the array
        if array[i] < smallest:  # if you find number less than the first number of the array
            smallest = array[i]  # store it now in the smallest variable
            smallest_index = i  # also change the index position of the smallest value
    return smallest_index  # after finding the smallest element, return its index position


def selection_sort(array):
    new_array = []  # create a new array where elements will be sorted
    for i in range(len(array)):  # for every element in the array
        smallest = find_smallest(array)  # give the index of the smallest element
        new_array.append(array.pop(smallest))  # remove the element from the array and add it to the new_array
    return new_array  # finally, return sorted array


test_array = [3, 8, 2, 15, 9, 11]

print(selection_sort(test_array))  # prints [2, 3, 8, 9, 11, 15]
print(test_array)  # prints []


# O(n^2) is the Big O representation of the selection sort algorithm. It might be confusing because of the number of
# elements of the array gets decreased after every loop, hence, the correct answer would be O(n * 1/2 * n).
# However, bear in mind that all constants in the Big O notation are not counted. So, the correct answer is O(n^2)

