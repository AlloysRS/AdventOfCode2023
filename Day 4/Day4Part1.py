import csv

def get_winners(data):
    total_points = 0
    for row in data:
        points = 0
        game_id, games = row[0].split(": ")
        game_id = int(game_id.replace("Card ", ""))
        card_numbers, card_winners = games.split(" | ")
        card_number = card_numbers.strip().split(" ")
        card_winner = card_winners.strip().split(" ")
        #print("card:", game_id, "numbers:",card_number,"winners:", card_winner)
        
        for number in card_number:
            if number == "":
                continue
            if number in card_winner:
                if points == 0:
                    points += 1
                else:
                    points = points * 2
        
        total_points += points
        points = 0
    
    return total_points

def main():
    with open('input.csv', 'r') as file:
        file = csv.reader(file)
        points = get_winners(file)
        print(points)

if __name__ == "__main__":
    main()