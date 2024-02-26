import re
import sys

def replace_textual_numbers(text):
    number_mapping = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': 'f4r',
        'five': 'f5e',
        'six': 's6x',
        'seven': 's7n',
        'eight': 'e8t',
        'nine': 'n9e'
    }
    for word, number in number_mapping.items():
        text = text.replace(word, number)
    return text

while True:
    try:
        # Initilaise calibrations as an empty list and cumulative sum as int starting at 0
        calibrations = []
        cumulative_sum = 0
        # Open csv file with the string format data ie '4three2fivecnlzgone3'
        with open('calibration_values.csv') as file:
            # for each line within the file add the string to the calibrations list
            for line in file:
                line_revised = replace_textual_numbers(line)
                calibrations.append(line_revised)
                #print(calibrations)
            # for each calibration within the list use regex to find the first and last number value
            for calibration in calibrations:
                matches = re.findall(r"([0-9])", calibration)
                # combine the first and last number found into one number and add this to cumulative sum
                if matches:
                    combined_value = str(matches[0])+str(matches[-1])
                    cumulative_sum += int(combined_value)
            # final print of the ending cumulative sum value
            print(cumulative_sum)
            break
    except FileNotFoundError:
        sys.exit("no file")