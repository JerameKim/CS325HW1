import random
import timeit

def make_list(size): 
    test_list = []
    for _ in range(size):
        number = random.randint(-10000, 10000)
        test_list.append(number)
    return test_list

list_1 = make_list(5000)
list_2 = make_list(10000)
list_3 = make_list(15000)
list_4 = make_list(20000)
list_5 = make_list(25000)
list_6 = make_list(30000)
list_7 = make_list(35000)

def merge_sort(my_list):

    # 1. Exit Statement
    #   only gets called n number of times
    if len(my_list) <= 1:
        return my_list

    middle_idx = len(my_list) // 2

    # 2. Recurse
    # left = merge_sort(my_list[0:middle_idx])
    # will return a sorted list from "left side"
    left = merge_sort(my_list[:middle_idx])

    # right = merge_sort(my_list[middle_idx:len(my_list)-1])
    # will return a sorted list from "right side"
    right = merge_sort(my_list[middle_idx:])

    # 3. Resolve Recursion
    sorted_list = merge(left, right)
    return sorted_list


def merge(left, right) -> []:

    combined = []

    left_idx = 0
    right_idx = 0

    # Run while there's uncompared values in both lists
    while left_idx < len(left) and right_idx < len(right):

        # if left's value smaller than right's value
        if left[left_idx] < right[right_idx]:
            # add the left value in
            combined.append(left[left_idx])

            # increment to compare to next left element
            left_idx += 1

        else:
            combined.append(right[right_idx])
            right_idx += 1

    # If there's uncompared values in right list, add the uncompaed values into combined
    while right_idx < len(right):
        combined.append(right[right_idx])
        right_idx += 1

    # if there's uncompared values values in left list, add the uncompared values into combined
    while left_idx < len(left):
        combined.append(left[left_idx])
        left_idx += 1
    return combined

print(f"Array Size: 5000  | Sort Time: {timeit.timeit(lambda: merge_sort(list_1), number=1)}")
print(f"Array Size: 10000 | Sort Time: {timeit.timeit(lambda: merge_sort(list_2), number=1)}")
print(f"Array Size: 15000 | Sort Time: {timeit.timeit(lambda: merge_sort(list_3), number=1)}")
print(f"Array Size: 20000 | Sort Time: {timeit.timeit(lambda: merge_sort(list_4), number=1)}")
print(f"Array Size: 25000 | Sort Time: {timeit.timeit(lambda: merge_sort(list_5), number=1)}")
print(f"Array Size: 30000 | Sort Time: {timeit.timeit(lambda: merge_sort(list_6), number=1)}")
print(f"Array Size: 35000 | Sort Time: {timeit.timeit(lambda: merge_sort(list_7), number=1)}")

