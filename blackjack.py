import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
your_cards = []
computer_cards = []

def user_add_card():
    your_cards.append(random.choice(cards))
    if sum(your_cards) > 21 and 11 in your_cards:
        your_cards[your_cards.index(11)] = 1

def comp_add_card():
    computer_cards.append(random.choice(cards))
    if sum(computer_cards) > 21 and 11 in computer_cards:
        computer_cards[computer_cards.index(11)] = 1

def starting():
    your_cards.clear()
    computer_cards.clear()
    your_cards.extend([random.choice(cards), random.choice(cards)])
    computer_cards.append(random.choice(cards))

def show_score():
    print(f"    Your final hand: {your_cards}, current score: {sum(your_cards)}")
    print(f"    Computer's first card: {computer_cards[0]}")

def final_show_score(result):
    print(f"    Your cards: {your_cards}, final score: {sum(your_cards)}")
    print(f"    Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
    print(result)

def comparison():
    user_score = sum(your_cards)
    comp_score = sum(computer_cards)
    if user_score > 21:
        return "You went over. You lose 😭"
    elif comp_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > comp_score:
        return "You win 😃"
    elif user_score < comp_score:
        return "You lose 😭"
    else:
        return "It's a draw!"

def play_game():
    while True:
        game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if game == "n":
            break
        print("\n" * 20)
        print(logo)
        starting()
        show_score()

        while sum(your_cards) < 21 and input("Type 'y' to get another card, type 'n' to pass: ") == "y":
            user_add_card()
            show_score()

        while sum(computer_cards) < 17:
            comp_add_card()

        final_show_score(comparison())

play_game()
