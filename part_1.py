import random


#შევქმნათ სია, რომელშიც შევინახავთ კარტის დასტას.

def create_deck():
    deck = []
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    for _ in range(4):
        for suit in suits:
            for value in values:
                deck.append(f"{value} of {suit}")
        random.shuffle(deck)
    return deck


# ფუნქცია მიიღებს მოთამაშეების სახელებს და სეინახავს ლისთში.
def get_playaers():
    players = []
    for i in range(3):
        name = input(f"Enter name for player {i + 1}: ")
        players.append(name)
    return players


# ფუნქცია დააგენერირებს ხუთ კარტს სამი მოთამაშისთვის და შეინახავს დიქტში. 
def generate_cards(players : list, deck : list): 
    cards_for_player = {}
    for i in players:
        cards = []
        for j in range(5):
            cards.append(deck.pop())
        cards_for_player[i] = cards
        
    return cards_for_player

# სათითაოდ კითხავს მოთამაშეებს თუ სურთ ერთი კარტის შეცვლა, თუ კი, შეცვლის ერთ სასურველ კარტს.
def change_cards(cards_for_players : dict, deck : list):
    for player, cards in cards_for_players.items():
        choice = input(f"{player}, do you want to change one card? (yes/no): ")
        if choice.lower() == 'yes':
            num = int(input("Enter the number of the card you want to change, from 1 to 5 : ")) - 1
            changed_card = deck.pop()
            cards[num] = changed_card
            cards_for_players[player] = cards
    return cards_for_players


# ფუნქცია, რომელიც ქულებს ანიჭებს კარტებს
def assigning_points(card):
    value = card.split()[0]
    if value == 'A':
        return 20
    elif value == 'K':
        return 13
    elif value == 'Q':
        return 12
    elif value == 'J':
        return 11
    else:
        return int(value)


# ფუნქცია, რომელიც ითვლის ქულებს
def calculate_points(cards):
    points = sum(assigning_points(card) for card in cards)
    return points


# ფუნქცია, რომელიც ითვლის ფერების რაოდენობას
def calculate_suits(cards):
    suits = {'Spades': 0, 'Hearts': 0, 'Diamonds': 0, 'Clubs': 0}
    for card in cards:
        suit = card.split()[-1]
        suits[suit] += 1
    return suits


# ფუნქცია, რომელიც ითვლის კარტის მნიშვნელობების რაოდენობას
def calculate_values(cards):
    values = {}
    for card in cards:
        value = card.split()[0]
        if value not in values:
            values[value] = 0
        values[value] += 1
    return values

def print_the_cards(cards_for_players):
    for player, cards in cards_for_players.items():
        print(f"{player}'s Cards:")
        for i in range(len(cards)):
            print(f"{i + 1}. {cards[i]}")
        print(f"Total Points: {calculate_points(cards)}")
        print(f"Suits: {calculate_suits(cards)}")
        print(f"Values: {calculate_values(cards)}")
        print()
def deal_cards(players):
    print("--" * 20) 
    print("Dealing cards...")
    print()
    deck = create_deck()
    cards_for_players = generate_cards(players, deck)
    print_the_cards(cards_for_players)
    cards_for_players = change_cards(cards_for_players, deck)
    return cards_for_players
def calculate_winners(new_cards_for_players):
    if len(new_cards_for_players.keys()) == 3:
        min_points = float('inf')
        losers = []
        for player, cards in new_cards_for_players.items():
            points = calculate_points(cards)
            if points < min_points:
                losers = [player]
                min_points = points
            elif points == min_points:
                losers.append(player)
        
        if len(losers) == 1:
            del new_cards_for_players[losers[0]]
            players = new_cards_for_players.keys()
            deal_cards(players)
            return calculate_winners(new_cards_for_players)
        elif len(losers) > 1:
            
            max_color_loser_1 = max(new_cards_for_players[losers[0]], key=lambda card: card[1][0])
            max_color_loser_2 = max(new_cards_for_players[losers[1]], key=lambda card: card[1][0])
            if max_color_loser_1[1][0] > max_color_loser_2[1][0]:
                del new_cards_for_players[losers[1]]
                players = new_cards_for_players.keys()
                deal_cards(players)
                return calculate_winners(new_cards_for_players)
            elif max_color_loser_1[1][0] < max_color_loser_2[1][0]:
                del new_cards_for_players[losers[0]]
                players = new_cards_for_players.keys()
                deal_cards(players)
                return calculate_winners(new_cards_for_players) 
            else:
                
                max_value_loser_1 = max(new_cards_for_players[losers[0]], key=lambda card: card[0])
                max_value_loser_2 = max(new_cards_for_players[losers[1]], key=lambda card: card[0])
                if max_value_loser_1[0] > max_value_loser_2[0]:
                    del new_cards_for_players[losers[1]]
                    players = new_cards_for_players.keys()
                    deal_cards(players)
                    return calculate_winners(new_cards_for_players)
                elif max_value_loser_1[0] < max_value_loser_2[0]:
                    del new_cards_for_players[losers[0]]
                    players = new_cards_for_players.keys()
                    deal_cards(players)
                    return calculate_winners(new_cards_for_players)
                else:
                    players = new_cards_for_players.keys()
                    deal_cards(players)
                    return calculate_winners(new_cards_for_players)    
    elif len(new_cards_for_players.keys()) == 2:
        players = list(new_cards_for_players.keys())
        if calculate_points(new_cards_for_players[players[0]]) > calculate_points(new_cards_for_players[players[1]]):
            del new_cards_for_players[players[1]]
            return new_cards_for_players
        elif calculate_points(new_cards_for_players[players[0]]) < calculate_points(new_cards_for_players[players[1]]):
            del new_cards_for_players[players[0]]
            return new_cards_for_players
        else:
            max_color_loser_1 = max(new_cards_for_players[players[0]], key=lambda card: card[1][0])
            max_color_loser_2 = max(new_cards_for_players[players[1]], key=lambda card: card[1][0])
            if max_color_loser_1[1][0] > max_color_loser_2[1][0]:
                del new_cards_for_players[players[1]]
                return new_cards_for_players
            elif max_color_loser_1[1][0] < max_color_loser_2[1][0]:
                del new_cards_for_players[players[0]]
                return new_cards_for_players
            else:
                max_value_loser_1 = max(new_cards_for_players[players[0]], key=lambda card: card[0])
                max_value_loser_2 = max(new_cards_for_players[players[1]], key=lambda card: card[0])
                if max_value_loser_1[0] > max_value_loser_2[0]:
                    del new_cards_for_players[players[1]]
                    return new_cards_for_players
                elif max_value_loser_1[0] < max_value_loser_2[0]:
                    del new_cards_for_players[players[0]]
                    return new_cards_for_players
                else:
                    players = new_cards_for_players.keys()
                    deal_cards(players)
                    return calculate_winners(new_cards_for_players)    
    
def main():
    #შეიქმნება კარტების დასტის სია
    deck = create_deck()
    
    #მომხმარებელს მოსთხოვს მოთამაშეების სახელებს
    players = get_playaers()
    
    #დავაგენერირებთ კარტს თითოეული მოთამაშისთვის და დავბეჭდავთ
    cards_for_players = generate_cards(players, deck)
    for player, cards in cards_for_players.items():
        print(f"{player}'s Cards:")
        for i in range(len(cards)):
            print(f"{i + 1}. {cards[i]}")
        print(f"Total Points: {calculate_points(cards)}")  # მაგალითისთვის ჩავსვი, რომ მენახა, სწორად ითვლიდა თუ არა
        print(f"Suits: {calculate_suits(cards)}")
        print(f"Values: {calculate_values(cards)}")
        print()
        
    #კითხავს მოთამაშეებს სათითაოდ, თუ უნდათ კარტის შეცვლა, თუ კი, შეცვლის ერთ კარტს ამ მოთამაშისთვის და დავბეჭდავთ.
    new_cards_for_players = change_cards(cards_for_players, deck)
    for player, cards in new_cards_for_players.items():
        print(f"{player}'s Cards:")
        for i in range(len(cards)):
            print(f"{i + 1}. {cards[i]}")
        print(f"Total Points: {calculate_points(cards)}")  # მაგალითისთვის ჩავსვი, რომ მენახა, სწორად ითვლიდა თუ არა
        print(f"Suits: {calculate_suits(cards)}")
        print(f"Values: {calculate_values(cards)}")
    winner = calculate_winners(new_cards_for_players)
    print("--" * 20)
    for player, cards in winner.items():
        print(f"{player} won with {cards}!")
        print(f"{player}'s total points: {calculate_points(cards)}")
        print(f"{player}'s suits: {calculate_suits(cards)}")
        print(f"{player}'s values: {calculate_values(cards)}")

    
    print("Thanks for playing!")
        
    
    
if __name__ == "__main__" :
    main()
    