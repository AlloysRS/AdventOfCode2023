import re
import csv

def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        return [row[0] for row in reader]

def check_adjacency(engine_rows, row, col):
    symbol_pattern = re.compile(r'[^.\d]')
    max_row = len(engine_rows)
    max_col = len(engine_rows[0])


    directions = [(0, -1), (0, 1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]

    #print("Checking adjacency for numeric value at:", row, col)

    for direction in directions:
        new_row = row + direction[0]
        new_col = col + direction[1]
        #print("checking: ", row, col, new_row, new_col)

        if is_valid_position(new_row, new_col, max_row, max_col) and symbol_pattern.match(engine_rows[new_row][new_col]):
            #print(new_row, new_col)
            #print("Found symbol:", symbol_pattern.match(engine_rows[new_row][new_col]).group())
            return True

    return False

def is_valid_position(row, col, max_row, max_col):
    return 0 <= row < max_row and 0 <= col < max_col

def find_engine_part_numbers(engine_rows):
    part_numbers = []
    for row in range(len(engine_rows)):
        number_valid = ''
        number_str = ''
        for col in range(len(engine_rows[row])):
            if engine_rows[row][col].isdigit():
                number_str += engine_rows[row][col]
                #print("checking:", engine_rows[row][col])
                if check_adjacency(engine_rows, row, col):
                    number_valid = 'valid'
            elif number_str:
                #print("number: ", number_str, number_valid)
                if number_valid == 'valid':
                    part_numbers.append(int(number_str))
                number_str = ''
                number_valid = ''
        if number_valid == 'valid':
            part_numbers.append(int(number_str))
            number_str = ''
            number_valid = ''
        #print("row: ", row, part_numbers)
        #part_numbers = []
    return part_numbers

# Example usage
csv_file_path = "input.csv"
engine_rows = read_csv(csv_file_path)

# Test the function
part_numbers = find_engine_part_numbers(engine_rows)

#print("Part numbers:", part_numbers)
print("Sum of part numbers:", sum(part_numbers))