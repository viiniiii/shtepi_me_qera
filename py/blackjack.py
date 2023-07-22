import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return cards[random.randint(0,12)]
user_cards = []
user_cards.append(deal_card())
user_cards.append(deal_card())
computer_cards = []
computer_cards.append(deal_card())
computer_cards.append(deal_card())

def calculate_score(array):
    piket = sum(array)
    if piket == 21:
        return 0
    if piket > 21:
        if array[0] == 11:
            array.remove(11)
            array.append(1)
        elif array[1] == 11:
            array.remove(11)
            array.append(1)
    return piket
komp = calculate_score(computer_cards)
player = calculate_score(user_cards)
print(komp)
print(player)
game_over = False
print(f"Player's cards: {user_cards}")
print(f"Computer's cards: [{computer_cards[0]}, ?]")
def precheck():
    if komp == 0 and player == 0:
        print("Draw")
        return True
    elif komp == 0:
        print("Computer wins")
        return True
    elif player == 0:
        print("Player wins")
        return True
    return False 
game_over = precheck()
if not game_over:        
    draw_another = input("Do you want to draw another card type 'y' or 'n': ")
    while draw_another == 'y':
        user_cards.append(deal_card())
        player = calculate_score(user_cards)
        print(f"Player's cards: {user_cards}")
        print(f"Computer's cards: [{computer_cards[0]}, ?]")
        draw_another = input("Do you want to draw another card type 'y' or 'n': ")
    while komp < 17:
        print("-------Computer draws a card!-------")
        computer_cards.append(deal_card())
        komp = calculate_score(computer_cards)
        print(f"Player's cards: {user_cards}")
        print(f"Computer's cards: {computer_cards}")
    if player > 21:
        print("-------Final result-------")
        print(f"Player's cards: {user_cards}")
        print(f"Computer's cards: {computer_cards}")
        print("Computer wins")
    elif komp > player:
        print("-------Final result-------")
        print(f"Player's cards: {user_cards}")
        print(f"Computer's cards: {computer_cards}")
        print("Computer wins")
    elif player > komp:
        print("-------Final result-------")
        print(f"Player's cards: {user_cards}")
        print(f"Computer's cards: {computer_cards}")
        print("Player wins") 
    elif player == komp:
        print("-------Final result-------")
        print(f"Player's cards: {user_cards}")
        print(f"Computer's cards: {computer_cards}")
        print("Draw")
        

           






