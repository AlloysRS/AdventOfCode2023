import csv

# Function to assign values to each card, with Jokers the lowest value
def get_card_value(card):
    # Define values for face cards
    values = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, 'J': 1}
    # Return the numeric value of the card if it's a digit, otherwise return its value from the dictionary
    if card.isdigit():
        return int(card)
    else:
        return values.get(card, 0)

# Function to sort hands based on their card values
def sort_by_card_values(game):
    return [get_card_value(card) for card in game['hand']]

# Function to read hands and bets from a CSV file
def read_csv(filename):
    games = []

    # Open the CSV file
    with open(filename, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            # Split the line into hand and bet
            hand, bet = line.strip().split(' ')
            # Create a dictionary for the game and add it to the list of games
            game = {'hand': hand, 'bet': bet, 'result': "", 'rank': 0}
            games.append(game)
    
    # Sort the list of games based on the values of the cards in each hand
    games.sort(key=sort_by_card_values)

    # Iterate over each game
    for game in games:
        current_hand = game['hand']
        card_counts = {}

        # Count occurrences of each card in the hand
        for card in current_hand:
            card_counts[card] = card_counts.get(card, 0) + 1
            
        # Check for jokers
        joker_count = card_counts.get('J', 0)
        #print(joker_count)
            
        # Count pairs, three of a kind, four of a kind, five of a kind
        pairs = 0
        three_of_a_kind = 0
        four_of_a_kind = 0
        five_of_a_kind = 0
        full_house = 0
        for card, count in card_counts.items():
            if card != 'J':
                if count == 2:
                    pairs += 1
                elif count == 3:
                    three_of_a_kind += 1
                elif count == 4:
                    four_of_a_kind += 1
                elif count == 5:
                    five_of_a_kind += 1

        # Check for a full house and remove pair and three of a kind if found
        if pairs == 1 and three_of_a_kind == 1:
            full_house += 1
            pairs -= 1
            three_of_a_kind -= 1

        # Assign hand type to each hand in order of hand ranking
        if five_of_a_kind:
            game['result'] = "Five of a kind"
        elif four_of_a_kind:
            if joker_count == 1:
                game['result'] = "Five of a kind"
            else:
                game['result'] = "Four of a kind"
        elif full_house:
            game['result'] = "Full House"
        elif three_of_a_kind:
            if joker_count == 2:
                game['result'] = "Five of a kind"
            elif joker_count == 1:
                game['result'] = "Four of a kind"
            else:
                game['result'] = "Three of a kind"
        elif pairs == 2:
            if joker_count == 1:
                game['result'] = "Full House"
            else:
                game['result'] = "Two Pairs"
        elif pairs:
            if joker_count == 3:
                game['result'] = "Five of a kind"
            elif joker_count == 2:
                game['result'] = "Four of a kind"
            elif joker_count == 1:
                game['result'] = "Three of a kind"
            else:
                game['result'] = "One Pair"
        else:
            # Initially have to check if there are Five jokers, as all 5 cards could be a joker, but also four jokers and any other card is also Five of a kind, this one threw me for a while.
            if joker_count == 5:
                game['result'] = "Five of a kind"
            elif joker_count == 4:
                game['result'] = "Five of a kind"
            elif joker_count == 3:
                game['result'] = "Four of a kind"
            elif joker_count == 2:
                game['result'] = "Three of a kind"
            elif joker_count == 1:
                game['result'] = "One Pair"
            else:
                game['result'] = "High Card"

    # Rank hands based on their type using the sorted hands list with lower rank being a worse hand
    ranking_order = ["High Card", "One Pair", "Two Pairs", "Three of a kind", "Full House", "Four of a kind", "Five of a kind"]
    current_rank = 1
    winnings = 0
    for rank_type in ranking_order:
        for game in games:
            if game['result'] == rank_type:
                # Assign rank to the game and calculate winnings based on bet * rank, and add this to winnings
                game['rank'] = current_rank
                current_rank += 1
                winnings += int(game['bet']) * int(game['rank'])

    # Return accumulated winnings
    return winnings

def main():
    filename = 'input.csv'
    total_winnings = read_csv(filename)
    print(total_winnings)

if __name__ == "__main__":
    main()