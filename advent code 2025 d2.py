#One day we WILL write efficient code
#I'm confident you could do this with substring shenanigans
#I unknowingly coded the P2 solution for P1 (I didn't read properly)
#Pretty convenient for me overall, since I just had to modify my code back to it's old state!
#improvements for p1:
#only need to check numbers with an even amount of digits
#only need to check the middle split of those numbers
#(inefficiencies from bandaiding what ended up P2's solution show up really hard)

def main():
    codes = read_file()
    total_sum_p1 = 0
    for line in codes:
        total_sum_p1 += iterate_each_num_p1(line)
    print(f"Part One Total Sum: {total_sum_p1}")

    total_sum_p2 = 0
    for line in codes:
        total_sum_p2 += iterate_each_num_p2(line)
    print(f"Part Two Total Sum: {total_sum_p2}")


def read_file(filename):
    filename = input("Enter the path to the file: ")
    file = open(filename, "r")
    file_content = file.read().split(",")
    file.close()
    return file_content

def iterate_each_num_p1(line):
    starting_num, ending_num = int(line.split("-")[0]), int(line.split("-")[1])
    current_sum = 0
    # print(f"Checking from {starting_num} to {ending_num}.")
    for number in range(starting_num, ending_num + 1):
        if check_for_pattern_p1(number):
            current_sum += number
    return current_sum



def iterate_each_num_p2(line):
    starting_num, ending_num = int(line.split("-")[0]), int(line.split("-")[1])
    current_sum = 0
    # print(f"Checking from {starting_num} to {ending_num}.")
    for number in range(starting_num, ending_num + 1):
        if check_for_pattern_p2(number):
            current_sum += number
    return current_sum



def check_for_pattern_p1(number):
    str_number = str(number) #str number useful so make it now
    for i in range(1, len(str_number) // 2+1): #ensure we only check numbers we have to
        if len(str_number) % i == 0: #extra check to make sure we're splitting number by a divisble amount (probably useless)
            split_num = [str_number[j:j+i] for j in range(0, len(str_number), i)] #make list from equal 'sections' of num
            # print(f"{split_num}, which was {str_number}.")
            if all(num == split_num[0] for num in split_num) and len(split_num) == 2: #are all elements in the list equal?
                # print(f"{split_num} is a repeated pattern in {str_number}.") 
                return True
    # print(f"{number} doesn't have a pattern.")
    return False



def check_for_pattern_p2(number):
    str_number = str(number)
    for i in range(1, len(str_number) // 2+1):
        if len(str_number) % i == 0:
            split_num = [str_number[j:j+i] for j in range(0, len(str_number), i)] #make list from equal 'sections' of num
            # print(f"{split_num}, which was {str_number}.")
            #are all elements in the list equal?
            if all(num == split_num[0] for num in split_num) and len(split_num): 
                # print(f"{split_num} is a repeated pattern in {str_number}.") 
                return True
    # print(f"{number} doesn't have a pattern.")
    return False

main()