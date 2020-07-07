import random
all_pot = input("Your money: ")
x = input("Your bet is: ")
int(all_pot)
int( x )
y = all_pot - x
money = all_pot - y

#Write your game of chance functions herec
choice = input('Your game: ')
number_of_games = input('How many games you want to play?\n')

for game in range(0,4):
    for number in range(0, number_of_games):
        if game == choice and game == 0:
            def coin_flip(bet, guess, all_pot):
                if (bet > money):
                    return "You don't have enought money"
                num = random.randint(1, 2)

                if (num == 1 and guess == "Heads"):
                    all_pot += bet * 2
                    return ("You Win:{} \n Your money:{}".format(bet * 2,all_pot))
                elif (num == 2 and guess == "Tails"):
                    all_pot += bet * 2
                    return ("You Win:{} \n Your money:{}".format(bet * 2,all_pot))
                else:
                    all_pot = all_pot - bet
                    return ("You lost:{} \n YOur money:{}".format(-bet, all_pot))
            guess = "Heads"
            print(coin_flip(money, guess, all_pot))
            print("\n")
        #print(money)
        elif game == choice and game == 1:
                def cho_han(guess, bet, all_pot):
                    if (bet > money):
                        return "You don't have enought money"
                    dice1 = random.randint(1, 6)
                    dice2 = random.randint(1, 6)
                    sum = dice1 + dice2
                    print("The dice roll is " + str(sum))

                    if (sum % 2 == 0 and guess == "Even"):
                        all_pot += bet * 2
                        return ("You Win:{} \n Your money:{}".format(bet * 2,all_pot))
                    elif (sum % 2 != 0 and guess == "Odd"):
                        all_pot += bet * 2
                        return ("You Win:{} \n Your money:{}".format(bet * 2,all_pot))
                    else:
                        all_pot = all_pot - bet
                        return ("You lost:{} \n YOur money:{}".format(-bet, all_pot))
                print(cho_han("Even", money, all_pot))
                print("\n")
        #print(money)


        elif game == choice and game == 2:
            def high_low(bet, all_pot):
                if (bet > money):
                    return "You don't have enought money"

                card_number = list(range(1,14))*4
                card_type = ['diamonds', 'clubs', 'hearts', 'spades']*13
                card_deck = (zip(card_number, card_type))

                card1 = random.choice(card_deck)
                card_deck.remove(card1)
                print(card1)
                card2 = random.choice(card_deck)
                print(card2)
                card_deck.remove(card2)

                if card1[0] > card2[0]:
                    all_pot += bet * 2
                    return ("You Win:{} \n Your money:{}".format(bet * 2,all_pot))
                elif card1[0] == card2[0]:
                    return "It's a tie"
                else:
                    all_pot = all_pot - bet
                    return ("You lost:{} \n YOur money:{}".format(-bet, all_pot))

            print(high_low(money, all_pot))
            print("\n")
        #print(money)


        elif game == choice and game == 3:
            def roullete(bet, guess, all_pot):
                if (bet > money):
                    return "You don't have enought money"

                roullete1 = [(0, "green")]
                color = ["red", "black"] * 18
                numbers = list(range(1, 37))
                roullete2 = (zip(numbers, color))
                roullete = roullete1 + roullete2
                number_on_roullete = random.choice(roullete)

                print(roullete)
                print(number_on_roullete)


                if guess == "Even" and number_on_roullete[0] % 2 == 0:
                    all_pot += bet * 2
                    return ("You Win:{} \n Your money:{}".format(bet * 2,all_pot))
                elif guess == "Odd" and number_on_roullete[0] % 2 != 0:
                    all_pot += bet * 2
                    return ("You Win:{}".format(bet * 2))
                elif guess == 0 and number_on_roullete[0] == 0:
                    all_pot += bet * 2
                    return ("You Win:{}".format(bet * 35))
                elif guess == number_on_roullete[0]:
                    all_pot += bet * 2
                    return ("You Win:{}".format(bet * 35))
                else:
                    all_pot = all_pot - bet
                    return ("You lost:{}".format(-bet))



            print(roullete(money, 15,all_pot))
            print("\n")
        #print(money)

#Call your game of chance functions here
