import random


#შევქმნათ სია, რომელშიც შევინახავთ კარტის დასტას.
def create_deck():
    deck = []
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
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
        print()
        
    #კითხავს მოთამაშეებს სათითაოდ, თუ უნდათ კარტის შეცვლა, თუ კი, შეცვლის ერთ კარტს ამ მოთამაშისთვის და დავბეჭდავთ.
    new_cards_for_players = change_cards(cards_for_players, deck)
    for player, cards in new_cards_for_players.items():
        print(f"{player}'s Cards:")
        for i in range(len(cards)):
            print(f"{i + 1}. {cards[i]}")
        print()
    
if __name__ == "__main__" :
    main()
    