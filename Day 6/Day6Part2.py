import csv

def read_csv(filename):
    margin_of_error = 0
    timestr = ""
    distancestr = ""

    with open(filename, 'r') as file:
        for line in file:
            # Create array of times and distances
            if line.startswith('Time:'):
                times = line.split(':')[1].split()
            elif line.startswith('Distance:'):
                distances = line.split(':')[1].split()

        # Concatenate times/distances as strings then set totals
        for time in times:
            timestr = timestr + time
        total_time = int(timestr)

        for distance in distances:
            distancestr = distancestr + distance
        total_distance = int(distancestr)

        # For loop to iterate over races, initialise ways_to_win as 0
        ways_to_win = 0
        # For loop to calculate every attempt waiting 1 second longer each time
        for i in range(total_time):
            attempt = i * (total_time - i)
            # If statement that increases ways_to_win if the attempt is better than distance
            if attempt > total_distance:
                ways_to_win += 1

        # After each race, margin_of_error calculated as product of each race ways_to_win
        if margin_of_error == 0:
            margin_of_error = ways_to_win
        else:
            margin_of_error = margin_of_error * ways_to_win

    # return margin_of_error
    return margin_of_error

filename = 'input.csv'
margin_of_error = read_csv(filename)
print(margin_of_error)
