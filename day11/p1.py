import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card    
user_cards = []
computer_cards = []
is_game_over=False
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
def calculate_score(cards):
    if sum(cards) > 21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards) >21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(sum_computer,sum_user):
    if sum_computer==sum_user:
        return "draw"
    elif sum_computer == 0:
        return "Lose, opponent have blackjack"
    elif sum_user==0:
        return " win with blackjack"
    elif sum_user >21:
        return "you went over you lose"
    elif sum_computer >21 :
        return "computer went over you win"
    elif sum_user > sum_computer:
        return "you win"
    else:
        return "you lose" 
while not is_game_over:
    sum_of_computer = calculate_score(computer_cards)
    sum_of_user = calculate_score(user_cards)
    print(f"your socre is {user_cards} and computer socre {computer_cards[0]}")
    if sum_of_user == 0 or sum_of_computer ==0 or sum_of_user >21:
        is_game_over = True
    else:
        user_shoud_deal=input("enter  'y' to get another card: ")
        if user_shoud_deal =="y":  
            user_cards.append(deal_card())
        else:
            is_game_over=True
while sum_of_computer !=0 and sum_of_computer <17:
    computer_cards.append(deal_card())
    sum_of_computer = calculate_score(computer_cards)
print(f"user card {user_cards} sum {sum_of_user} and computer {computer_cards} sum {sum_of_computer}")
print(compare(sum_of_computer,sum_of_user))    


