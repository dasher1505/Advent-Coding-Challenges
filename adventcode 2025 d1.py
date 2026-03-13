def main():
    print("Part ONE")
    password = part_one()
    print(f"The password is {password}!")
    print("-----------------------------------------")
    print("Part TWO")
    password_p2 = part_two()
    print(f"The password for part two is {password_p2}!")

def part_one():
    filename = input("Input the path to the file: ")
    lines = read_file(filename)
    concurrent_val = 50
    password = 0
    for line in lines:
        val_to_add = parse_line(line)
        concurrent_val, password = run_equation(concurrent_val, val_to_add, password)
    return password
    
def read_file(filename):
    file = open(filename, "r")
    file_content = file.readlines()
    file.close()
    return file_content

def parse_line(line):
    if line[0] == "L":
        return int(line[1::]) * -1
    else:
        return int(line[1::])
    
def run_equation(concurrent_val, val_to_add, password):
    concurrent_val = (concurrent_val + val_to_add) % 100
    if concurrent_val == 0:
        password += 1
    return concurrent_val, password


# this one wasn't playing nice with doing generic modulo stuff so instead
# i bruteforced it with an array. definitely one of the uglier ways of
# doing it but I'll make it more beautiful another day.
def part_two():
    filename = input("Input the path to the file: ")
    lines = read_file(filename)
    concurrent_val = 50
    password = 0
    for line in lines:
        val_to_add = parse_line(line)
        concurrent_val, password = run_equation_p2(concurrent_val, val_to_add, password)
    return password

def run_equation_p2(concurrent_val, val_to_add, password):
    adding_list = []
    if val_to_add < 0:
        for i in range(0, val_to_add, -1):
            adding_list.append(-1)
    elif val_to_add > 0:
        for i in range(0, val_to_add):
            adding_list.append(1)
    for num in adding_list:
        concurrent_val += num
        if concurrent_val % 100 == 0:
            password += 1
    


    return concurrent_val, password
    


main()

