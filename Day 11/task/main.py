import art
import random

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
dealer_cards = []
card_deck = {"Ace" : 11, "1" : 1, "2" : 2, "3" : 3, "4" : 4,
             "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9,
             "10" : 10, "Jack" : 10, "Queen" : 10, "King" : 10
             }
special_cards10 = ["10", "Jack", "Queen", "King"]
user_score = 0
dealer_score = 0
# special
def deal_card():
    #We use random.choice if we want only one random element from the dictionary
    return random.choice(list(card_deck.keys()))

def calculate_score(cards):
   score_value = 0
   ace_card = False
   ace_card_index = 0
   for card in cards:
       #Check if there is an Ace card
       if card == "Ace":
           ace_card = True
           ace_card_index = cards.index(card)
           # Check for a Blackjack
           if len(cards) == 2:
                   if cards[ace_card_index - 1] in special_cards10:
                       return 0
       for key, value in card_deck.items():
           if card == key:
               score_value += value
       #If the total value is over 21 and there is an Ace card, then replace the Ace
       #card for and "1" card
       if ace_card and score_value > 21:
           cards[ace_card_index] = "1"
           score_value -= 10
   return score_value

def calculate_winner(score_user, score_dealer):
    if score_dealer == 0 and score_user == 0:
        return "Dealer - all zero"
    if score_dealer == 0 or score_dealer == 21:
        return "Dealer - zero or 21"
    if score_user == 0 or score_user == 21:
        if score_dealer != 0 and score_dealer != 21:
            return "User - User zero or 21 and dealer != zero or 21"
    if score_user < 21 > score_dealer:
        if score_user > score_dealer:
            return "User - (user and dealer < 21) and (user > dealer) "
        elif score_user == score_dealer:
            return "Draw - (user and dealer < 21) and (user == dealer) "
        else:
            return "Dealer - (user and dealer < 21) and (user < dealer)"
    if score_user > 21 < score_dealer:
        if score_dealer == score_user:
            return "Draw (score_dealer and score_user > 21) and (score_user == score_dealer)"
        else:
            return "Dealer - (score_dealer > 21) and (score_user > 21)"
    return None

#First two random cards assigment
#We use random.sample if we want multiple random elements from the dictionary
#Using the keyword list converts the key of a dictionary into a list
user_cards = ["10", "10", "1"]
dealer_cards = ["10", "9", "2"]

# user_cards = random.sample(list(card_deck.keys()), 2)
# dealer_cards = random.sample(list(card_deck.keys()), 2)

user_score = calculate_score(user_cards)
dealer_score = calculate_score(dealer_cards)

winner = calculate_winner(user_score, dealer_score)

print(user_cards)
print(dealer_cards[0])
print(dealer_cards)
print(user_score)
print(dealer_score)
print(winner)

