import csv

def try_games(data):
    possible_games_added = 0
    for row in data:
        green_cubes = 0
        red_cubes = 0
        blue_cubes = 0
        game_id, games = row[0].split(": ")
        game_id = int(game_id.replace("Game ", ""))
        attempts = games.split("; ")

        for attempt in attempts:
            colours = attempt.split(", ")
            for colour in colours:
                count_cubes, colour_name = colour.split()
                count_cubes = int(count_cubes)
                if colour_name == "green" and count_cubes > green_cubes:
                    green_cubes = count_cubes
                elif colour_name == "red" and count_cubes > red_cubes:
                    red_cubes = count_cubes
                elif colour_name == "blue" and count_cubes > blue_cubes:
                    blue_cubes = count_cubes
                else:
                    pass
        if green_cubes > 13 or red_cubes > 12 or blue_cubes > 14:
            #print(game_id, "game not possible")
            pass
        else:
            #print(game_id, "possible")
            possible_games_added = possible_games_added + game_id
    return possible_games_added

def main():
    with open('input.csv', 'r') as file:
        file = csv.reader(file)
        possible_games = try_games(file)
        print(possible_games)

if __name__ == "__main__":
    main()
