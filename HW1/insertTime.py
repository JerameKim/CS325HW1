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


def insert_sort(my_list):
    # loop through list from second value to the end
    for idx in range(len(my_list)):
        # value we are comparing (starts with second value in list )
        current_val = my_list[idx]
        # index position of the value we are comparing to current_val
        compare_idx = idx - 1
        # do comparison on each value that is larger than current_val
        while compare_idx >= 0 and current_val < my_list[compare_idx]:
            # switch values
            my_list[compare_idx + 1] = my_list[compare_idx]
            # move to next value to compare
            compare_idx = compare_idx - 1
        # update current_val
        my_list[compare_idx + 1] = current_val


print(f"Array Size: 5000  | Sort Time: {timeit.timeit(lambda: insert_sort(list_1), number=1)}")
print(f"Array Size: 10000 | Sort Time: {timeit.timeit(lambda: insert_sort(list_2), number=1)}")
print(f"Array Size: 15000 | Sort Time: {timeit.timeit(lambda: insert_sort(list_3), number=1)}")
print(f"Array Size: 20000 | Sort Time: {timeit.timeit(lambda: insert_sort(list_4), number=1)}")
print(f"Array Size: 25000 | Sort Time: {timeit.timeit(lambda: insert_sort(list_5), number=1)}")
print(f"Array Size: 30000 | Sort Time: {timeit.timeit(lambda: insert_sort(list_6), number=1)}")
print(f"Array Size: 35000 | Sort Time: {timeit.timeit(lambda: insert_sort(list_7), number=1)}")
