def main():
    lines = parse_file()
    total_output_voltage = 0
    # print(lines)
    for line in lines:
        total_output_voltage += int(find_highest_voltage(line))
    print(f"Overall output: {total_output_voltage}")


    total_output_voltage_p2 = 0
    for line in lines:
        total_output_voltage_p2 += int(find_highest_voltage_p2(line))
    print(f"Overall output: {total_output_voltage_p2}")




def find_highest_voltage(line):
    first_digit = line[0]
    second_digit = line[1]
    # print(f"First digit is {first_digit}. Second digit is {second_digit}.")
    for i in range(1, len(line)):
        if first_digit < line[i] and i != len(line)-1:
            first_digit, second_digit = line[i], line[i+1]
            # print(f"First digit and second digit swapped. Now {first_digit}{second_digit}")
        elif second_digit < line[i]:
            second_digit = line[i]
            # print(f"Second digit swapped. Now {first_digit}{second_digit}")
    highest_voltage = first_digit + second_digit
    # print(f"Highest voltage: {highest_voltage} from {line}.")
    return highest_voltage



def parse_file():
    filename = r"C:\Users\dashe\Local Documents\Personal Projects\advent_code\adventcode_d3.txt"
    file = open(filename, "r")
    content = file.read().split("\n")
    if content[-1] == '':
        content.pop(-1)
    return content




#in principle, this is meant to work by scanning from the last possible index the first digit of the number
#can come from (if we start at the 11th last index, we only get 11 digit number).
#once we find the largest possible digit for the first digit, we then 'scan' up the index just before
#that digit for the next digit's search. This maximises the digit in the highest place value position,
#which in theory guarantees we get the largest possible number.

def find_highest_voltage_p2(line): #something has gone wrong here will investigate l8r
    starting_point_index = len(line) - 12
    up_to_index = 0 #rename?
    number_to_return = ""
    for i in range(starting_point_index, len(line)):
        current_digit = line[i]
        # print(f"Digit we're starting with: {current_digit}")
        for j in range(i-1, up_to_index-1, -1):
            # print(f"Is {current_digit} < {line[j]}?")
            if current_digit <= line[j]:
                # print(f"Yes. Setting {up_to_index} to {j+1}.")
                current_digit, up_to_index = line[j], j+1
        # print(f"Appending {current_digit} to {number_to_return}")
        number_to_return += current_digit
    print(number_to_return)
    return number_to_return

            



main()