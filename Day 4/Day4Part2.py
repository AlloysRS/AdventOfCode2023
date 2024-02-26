import csv

def get_winners(data):
    max_winning_numbers = 200  # Could do to write code to get max rows from csv
    row_copies = [0] * (max_winning_numbers + 1)  # Initialize row_copies with zeros, probably poor approach
    row_count = -1
    total_scratchcards = 0
    for row in data:
        row_count += 1
        winning_numbers = 0
        game_id, games = row[0].split(": ")
        game_id = int(game_id.replace("Card ", ""))
        card_numbers, card_winners = games.split(" | ")
        card_number = card_numbers.strip().split(" ")
        card_winner = card_winners.strip().split(" ")
        #print("card:", game_id)
        total_scratchcards += 1
        
        # First process original version of scratchcard
        for number in card_number:
            if number == "":
                continue
            if number in card_winner:
                winning_numbers += 1
                row_copies[winning_numbers+row_count] += 1
        #print("copies array:",row_copies)
                
        # Then process any copies of scratchcard identified in row_copies array
        while row_copies[row_count] > 0:
            total_scratchcards += 1
            #print("card:", game_id)
            row_copies[row_count] -= 1
            row_num = 0
            for number in card_number:
                if number == "":
                    continue
                if number in card_winner:
                    row_num += 1
                    winning_numbers += 1
                    row_copies[row_count+row_num] += 1
            #print("copies array:",row_copies)
    return total_scratchcards

def main():
    with open('input.csv', 'r') as file:
        file = csv.reader(file)
        points = get_winners(file)
        print(points)

if __name__ == "__main__":
    main()