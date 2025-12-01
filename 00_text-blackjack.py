import random

#define global variables
deck = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,
        "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A"]
used_card_pile = []
player_hand = []
dealer_hand = []
wallet = 1000


def bet():
    #ask bet amount
    ba_needed = True
    while ba_needed:
        print(f"Wallet: ${wallet}")
        bet_amount = input("Enter an amount to bet: ")
        if bet_amount.isdigit():
            if wallet >= int(bet_amount):
                ba_needed = False
        else:
            print("Invalid input. Enter a positive whole number.\n")

    return int(bet_amount)

    
def deal_card(recipient):
    #deal the cards to the arguement
    card = random.choice(deck)
    recipient.append(card)
    deck.remove(card)


def total(hand):
    #calculate hand total   
    total = 0
    face = ["J", "K", "Q"]
    
    for card in hand:
        if card in range(1,11):
            total += card
        elif card in face:
            total += 10
        else:
            if total > 10:
                total += 1
            else:
                total += 11

    if total > 21 and 'A' in hand:
        total -= 10
        
    return total


def reveal_dealer():
    #reveal dealer's first card... kinda useless function ngl
    return dealer_hand[0]


def game_loop():
    #loop player decisions until player chooses to stop or busts
    player_in = True
    game_on = True
    
    while player_in:
        print(f"Dealer has {reveal_dealer()} and an unknown")
        print(f"You have {total(player_hand)} {player_hand}")
        stay_or_hit = input("1: Stand\n2: Hit\n")

        if stay_or_hit == "1":
            player_in = False
        elif stay_or_hit == "2":
            deal_card(player_hand)
            if total(player_hand) >= 21:
                player_in = False
                game_on = False
        else:
            print("Invalid Input\n")
            continue
    else:
        if game_on:
            while total(dealer_hand) < 17:
                deal_card(dealer_hand)
            else:
                pass

    fpt, fdt = total(player_hand), total(dealer_hand)

    return fpt, fdt
        

def results(fpt, fdt, ba):
    global wallet
    print(f"You have {fpt} with {player_hand}.")
    print(f"The dealer has {fdt} with {dealer_hand}.\n")

    if fpt == 21 and fdt != 21:
        print("Blackjack! You win!")
        wallet += ba
    elif fdt == 21 and fpt !=21:
        print("Blackjack. Dealer wins.")
        wallet -= ba
    elif fpt > 21:
        print("You bust. Dealer wins.")
        wallet -= ba
    elif fdt > 21:
        print("Dealer busts! You win!")
        wallet += ba
    elif 21 - fdt < 21 - fpt:
        print("Dealer wins.")
        wallet -= ba
    elif 21 - fdt > 21 - fpt:
        print("You win!")
        wallet += ba
    else:
        print("Push.")
    

def clear_hands():
    #need to check if this will add blank spaces to the list
    used_card_pile.extend(player_hand)
    player_hand.clear()

    used_card_pile.extend(dealer_hand)
    dealer_hand.clear()

    if len(used_card_pile) == 52:
        deck.extend(used_card_pile)
        used_card_pile.clear()


def main():
    play_again = True
    
    while play_again:
        ba = bet()

        for _ in range(2):
            deal_card(dealer_hand)
            deal_card(player_hand)

        fpt, fdt = game_loop()

        results(fpt, fdt, ba)

        while True:
            print(f"New wallet total: ${wallet}")
            play_again = input("Again? (y/n): ").strip().lower()
            if play_again == 'y':
                break
            elif play_again == 'n':
                play_again = False
                break
            else:
                print("Invalid Input. Enter y or n.\n")

        clear_hands()

main()


