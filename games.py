import random
all_pot = input("Your money: ")
x = input("Your bet is: ")
int(all_pot)
int( x )
y = all_pot - x
money = all_pot - y

print("Games you can play. \n 0.Coin Flip \n 1.Dice Roll \n 2.High/Low card game \n 3. Roullete")

#Write your game of chance functions herec
choice = input('Your game: ')
number_of_games = input('How many games you want to play?\n')


for game in range(0,4):
    money_left = all_pot
    for number in range(0, number_of_games):
        if game == choice and game == 0:
            def coin_flip(bet, guess):
                if (bet > money):
                    return "You don't have enought money"
                num = random.randint(1, 2)

                if (num == 1 and guess == "Heads"):
                    return bet * 2
                elif (num == 2 and guess == "Tails"):
                    return bet * 2
                else:
                    return -bet
            guess = "Heads"
            how_mutch = coin_flip(money, guess)
            money_left += how_mutch
            if money < how_mutch:
                money_left = money_left - money
                print("You Win:{} \nYour money:{}".format(how_mutch - money, money_left))
            elif money > how_mutch:
                print("You Lose:{} \nYour money:{}".format(how_mutch, money_left))
            print("\n")

        elif game == choice and game == 1:
                def cho_han(guess, bet):
                    if (bet > money):
                        return "You don't have enought money"
                    dice1 = random.randint(1, 6)
                    dice2 = random.randint(1, 6)
                    sum = dice1 + dice2
                    print("The dice roll is " + str(sum))

                    if (sum % 2 == 0 and guess == "Even"):
                        return bet * 2
                    elif (sum % 2 != 0 and guess == "Odd"):
                        return bet * 2
                    else:
                        return -bet
                guess = "Even"
                how_mutch = cho_han(guess, money)
                money_left += how_mutch
                if money < how_mutch:
                    money_left = money_left - money
                    print("You Win:{} \nYour money:{}".format(how_mutch - money, money_left))
                elif money > how_mutch:
                    print("You Lose:{} \nYour money:{}".format(how_mutch, money_left))
                print("\n")


        elif game == choice and game == 2:
            def high_low(bet):
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
                    return bet * 2
                elif card1[0] == card2[0]:
                    return bet
                else:
                    return -bet

            how_mutch = high_low(money)
            money_left += how_mutch
            if money < how_mutch:
                money_left = money_left - money
                print("You Win:{} \nYour money:{}".format(how_mutch - money, money_left))
            elif money > how_mutch:
                print("You Lose:{} \nYour money:{}".format(how_mutch, money_left))
            elif money == how_mutch:
                print("It's a tie")
            print("\n")
        #print(money)


        elif game == choice and game == 3:
            def roullete(bet, guess):
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
                    return bet * 2
                elif guess == "Odd" and number_on_roullete[0] % 2 != 0:
                    return bet * 2
                elif guess == 0 and number_on_roullete[0] == 0:
                    return bet * 35
                elif guess == number_on_roullete[0]:
                    return bet * 35
                else:
                    return -bet


            how_mutch = roullete(money, 15)
            money_left += how_mutch
            if money < how_mutch:
                money_left = money_left - money
                print("You Win:{} \nYour money:{}".format(how_mutch - money, money_left))
            elif money > how_mutch:
                print("You Lose:{} \nYour money:{}".format(how_mutch, money_left))
            elif money == how_mutch:
                print("It's a tie")
            print("\n")
        #print(money)

#Call your game of chance functions here
