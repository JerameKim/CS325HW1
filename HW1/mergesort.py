def open_file(filename):
    # list of each line with numbers
    numbers_list = []

    # Read each line from data.txt and add to numbers_list as list of ints
    with open(filename, 'r') as reader:
        line = reader.readline()
        while line != '':  # End of file character is empty string
            numbers = []

            # make list from values in line
            numbers = line.split()

            # cast list values from string to int
            numbers = [int(i) for i in numbers]
            numbers.pop(0)

            numbers_list.append(numbers)

            # move to the next line
            line = reader.readline()

    return numbers_list

def merge_sort(my_list):

    # 1. Exit Statement 
    #   only gets called n number of times
    if len(my_list) <= 1: 
        return my_list

    middle_idx = len(my_list) // 2

    # 2. Recurse
    # left = merge_sort(my_list[0:middle_idx])
    left = merge_sort(my_list[:middle_idx]) # will return a sorted list from "left side"
    
    # right = merge_sort(my_list[middle_idx:len(my_list)-1])
    right = merge_sort(my_list[middle_idx:]) # will return a sorted list from "right side" 


    # 3. Resolve Recursion
    sorted_list = merge(left, right)
    return sorted_list

def merge(left, right) -> []: 
    
    combined = []

    left_idx = 0 
    right_idx = 0 

    # Run while there's uncompared values in both lists 
    while left_idx < len(left) and right_idx < len(right) :

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

def write_results(filename, sorted_numbers_list):
    # open file to write to
    with open(filename, 'w') as writer:
        # get each list from list of all the lines
        for number_list in sorted_numbers_list:

            # Write to file
            for num in number_list:
                writer.write(f"{num} ")

            writer.write("\n")


if __name__ == "__main__":
    read_file = "data.txt"
    write_file = "merge.out"

    data = open_file(read_file)

    sorted_numbers_list = []

    for my_list in data:
        sorted_list = merge_sort(my_list)
        sorted_numbers_list.append(sorted_list)


    write_results(write_file, sorted_numbers_list)
