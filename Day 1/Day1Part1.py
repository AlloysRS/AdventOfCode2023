import re
import sys

while True:
    try:
        # Initilaise calibrations as an empty list and cumulative sum as int starting at 0
        calibrations = []
        cumulative_sum = 0
        # Open csv file with the string format data ie '4three2fivecnlzgone3'
        with open('calibration_values.csv') as file:
            # for each line within the file add the string to the calibrations list
            for line in file:
                calibrations.append(line)
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