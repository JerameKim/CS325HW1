
def open_file(filename): 
    # list of each line with numbers
    numbers_list = []

    # Read each line from data.txt and add to numbers_list as list of ints
    with open(filename, 'r') as reader:
        line = reader.readline()
        while line != '':
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

def insert_sort(my_list):

    # loop through list from second value to the end
    for idx in range(len(my_list)):

        # value we are comparing (starts with second value in list )
        current_val = my_list[idx]

        # index position of the value we are comparing to current_val
        compare_idx = idx - 1

        # do comparison on each value that is larger than current_val
        while compare_idx >=0 and current_val < my_list[compare_idx]:
            # switch values
            my_list[compare_idx + 1] = my_list[compare_idx]
            # move to next value to compare
            compare_idx = compare_idx - 1
        
        # update current_val
        my_list[compare_idx + 1] = current_val
    # print(my_list)



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
    write_file = "insert.out"

    data = open_file(read_file)

    for my_list in data: 
        insert_sort(my_list)


    write_results(write_file, data)
