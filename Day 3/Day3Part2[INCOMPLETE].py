import re
import csv

def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        return [row[0] for row in reader]

def check_adjacency(engine_rows, row, col):
    symbol_pattern = re.compile(r'[0-9]')
    max_row = len(engine_rows)
    max_col = len(engine_rows[0])

    directions_up = [(-1, -1), (-1, 0), (-1, 1)]
    directions_down = [(1, -1), (1, 0), (1, 1)]
    directions_left = [(0, -1)]
    directions_right = [(0, 1)]

    number_str = ''
    numbers_array = []

    #print("Checking adjacency for numeric value at:", row, col)

    for direction in directions_up:
        new_row = row + direction[0]
        new_col = col + direction[1]
        #print("checking up")
        if is_valid_position(new_row, new_col, max_row, max_col) and symbol_pattern.match(engine_rows[new_row][new_col]):
            #print(new_row, new_col)
            #print("Found symbol:", symbol_pattern.match(engine_rows[new_row][new_col]).group())
            while True:
                new_col -= 1
                #print("col is", new_col)
                if is_valid_position(new_row, new_col, max_row, max_col) and symbol_pattern.match(engine_rows[new_row][new_col]):
                    ...
                else:
                    break
            while True:
                new_col += 1
                if is_valid_position(new_row, new_col, max_row, max_col) and symbol_pattern.match(engine_rows[new_row][new_col]):
                    #print("Found symbol:", symbol_pattern.match(engine_rows[new_row][new_col]).group())
                    number_str += symbol_pattern.match(engine_rows[new_row][new_col]).group()
                else:
                    #print("num is:", number_str)
                    break
        if number_str != '':
            #print("not blank")
            numbers_array.append(int(number_str))
            number_str = ''
            break

    for direction in directions_left:
        new_row = row + direction[0]
        new_col = col + direction[1]
        #print("checking left")
        if is_valid_position(new_row, new_col, max_row, max_col) and symbol_pattern.match(engine_rows[new_row][new_col]):
            #print(new_row, new_col)
            #print("Found symbol:", symbol_pattern.match(engine_rows[new_row][new_col]).group())
            while True:
                new_col -= 1
                #print("col is", new_col)
                if is_valid_position(new_row, new_col, max_row, max_col) and symbol_pattern.match(engine_rows[new_row][new_col]):
                    #print("Found symbol:", symbol_pattern.match(engine_rows[new_row][new_col]).group())
                    ...
                else:
                    break
            while True:
                new_col += 1
                if is_valid_position(new_row, new_col, max_row, max_col) and symbol_pattern.match(engine_rows[new_row][new_col]):
                    #print("Found symbol:", symbol_pattern.match(engine_rows[new_row][new_col]).group())
                    number_str += symbol_pattern.match(engine_rows[new_row][new_col]).group()
                    ...
                else:
                    #print("num is:", number_str)
                    break
        if number_str != '':
            #print("not blank")
            numbers_array.append(int(number_str))
            number_str = ''
            break

    for direction in directions_right:
        new_row = row + direction[0]
        new_col = col + direction[1]
        #print("checking right")
        if is_valid_position(new_row, new_col, max_row, max_col) and symbol_pattern.match(engine_rows[new_row][new_col]):
            #print(new_row, new_col)
            #print("Found symbol:", symbol_pattern.match(engine_rows[new_row][new_col]).group())
            while True:
                new_col -= 1
                #print("col is", new_col)
                if is_valid_position(new_row, new_col, max_row, max_col) and symbol_pattern.match(engine_rows[new_row][new_col]):
                    #print("Found symbol:", symbol_pattern.match(engine_rows[new_row][new_col]).group())
                    ...
                else:
                    break
            while True:
                new_col += 1
                if is_valid_position(new_row, new_col, max_row, max_col) and symbol_pattern.match(engine_rows[new_row][new_col]):
                    #print("Found symbol:", symbol_pattern.match(engine_rows[new_row][new_col]).group())
                    number_str += symbol_pattern.match(engine_rows[new_row][new_col]).group()
                    ...
                else:
                    #print("num is:", number_str)
                    break
        if number_str != '':
            #print("not blank")
            numbers_array.append(int(number_str))
            number_str = ''
            break

    for direction in directions_down:
        new_row = row + direction[0]
        new_col = col + direction[1]
        #print("checking down")
        if is_valid_position(new_row, new_col, max_row, max_col) and symbol_pattern.match(engine_rows[new_row][new_col]):
            #print(new_row, new_col)
            #print("Found symbol:", symbol_pattern.match(engine_rows[new_row][new_col]).group())
            while True:
                new_col -= 1
                #print("col is", new_col)
                if is_valid_position(new_row, new_col, max_row, max_col) and symbol_pattern.match(engine_rows[new_row][new_col]):
                    #print("Found symbol:", symbol_pattern.match(engine_rows[new_row][new_col]).group())
                    ...
                else:
                    break
            while True:
                new_col += 1
                if is_valid_position(new_row, new_col, max_row, max_col) and symbol_pattern.match(engine_rows[new_row][new_col]):
                    #print("Found symbol:", symbol_pattern.match(engine_rows[new_row][new_col]).group())
                    number_str += symbol_pattern.match(engine_rows[new_row][new_col]).group()
                else:
                    #print("num is:", number_str)
                    break
        if number_str != '':
            #print("not blank")
            numbers_array.append(int(number_str))
            number_str = ''
            break

    #print("row number cnt:",len(numbers_array))
    print("numbers array:", numbers_array)

    if len(numbers_array) == 2:
        return numbers_array[0] * numbers_array[1]
    else:
        return 0

def is_valid_position(row, col, max_row, max_col):
    return 0 <= row < max_row and 0 <= col < max_col

def find_engine_gearing(engine_rows):
    gear_ratio = 0
    for row in range(len(engine_rows)): 
        print("row is", row)
        for col in range(len(engine_rows[row])):
            if engine_rows[row][col] == '*':
                #print("star found")
                #print("checking:", engine_rows[row][col])
                gear_ratio += check_adjacency(engine_rows, row, col)
    return gear_ratio

def main():
    csv_file_path = "input.csv"
    engine_rows = read_csv(csv_file_path)
    total_gear_ratio = find_engine_gearing(engine_rows)
    print("Total Gear Ratio:", total_gear_ratio)

if __name__ == '__main__':
    main()