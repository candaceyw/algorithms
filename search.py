import random
import time

my_range = 100
my_size = 15

nums = list(range(0, my_size))
random_nums = random.sample(range(my_range), my_size)

# shuffled_nums = list(range(0, my_size))
# random.shuffle(shuffled_nums)

# print(random_nums)
# print(shuffled_nums)

num_to_find = 12


# O(n) Linear time
def linear_search(arr, target):
    for num in arr:
        if num == target:
            return True
    return False


# print(linear_search(random_nums, num_to_find))
# print(linear_search(nums, num_to_find))

random_nums.sort()
# print(random_nums)

random_nums = [4, 10, 13, 17, 21, 26, 29, 31, 32, 50, 67, 70, 74, 85, 92]

def binary_search(arr, target):
    # get the middle point
    # compare the value in the middle with target
    # [4, 10, 13, 34, 36, 48, 56, 57, 62, 66, 71, 74, 85, 87, 92]
    start = 0
    end = (len(arr) -1)

    found = False
    while end >= start and not found:
        # get the middle point
        middle_index = (start + end) // 2
        # compare the value in teh middle with target
        # if the middle value is the same as target, set found to True
        if arr[middle_index] == target:
            found = True
        # move start or end index closer to one another, and shrink our search space
        else:
            if target < arr[middle_index]:
                end = middle_index - 1
            if target > arr[middle_index]:
                start = middle_index + 1

    return found

print(binary_search(random_nums, 12))