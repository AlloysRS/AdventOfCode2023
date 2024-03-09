import csv

def read_csv(filename):
    races = []
    margin_of_error = 0

    with open(filename, 'r') as file:
        for line in file:
            # Create array of times and distances
            if line.startswith('Time:'):
                times = line.split(':')[1].split()
            elif line.startswith('Distance:'):
                distances = line.split(':')[1].split()

        # Zip times and distances and append to races array
        for time, distance in zip(times, distances):
            races.append({'time': int(time), 'distance': int(distance)})

        # For loop to iterate over races, initialise ways_to_win as 0
        for race in races:
            ways_to_win = 0
            # For loop to calculate every attempt waiting 1 second longer each time
            for i in range(race['time']):
                attempt = i * (race['time'] - i)
                # If statement that increases ways_to_win if the attempt is better than distance
                if attempt > race['distance']:
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
