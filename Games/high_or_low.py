import random

def main():
    CASH = 1000
    CARDS = [
        { 'face': 'Ace', 'value': 1},
        { 'face': '2', 'value': 2},
        { 'face': '3', 'value': 3},
        { 'face': '4', 'value': 4},
        { 'face': '5', 'value': 5},
        { 'face': '6', 'value': 6},
        { 'face': '7', 'value': 7},
        { 'face': '8', 'value': 8},
        { 'face': '9', 'value': 9},
        { 'face': '10', 'value': 10},
        { 'face': 'Jack', 'value': 11},
        { 'face': 'Queen', 'value': 12},
        { 'face': 'King', 'value': 13},
    ]

    print('''High or Low
        In High or Low, you play against the house
        Before the hand, bets are placed
         
        After the draw, you will guess whether your card is higher or lower than you opponent's
         
        Guess right, you win. Guess wrong, you lose. If cards are equal, the house wins.
         
        The house always wins.
         
        Aces are low. 
        
        You get a grand. Turn it into ten, you win. Turn it into nothing... well.

        Ready to play? 
        
        ''')
    
    if input('It\'s a yes or no question > ').startswith('y'):
        while True:
            if CASH >= 10000:
                print('Looks like you won it all kid. I didn\'t think you had it in you.')
                break
            if CASH <= 0:
                print('Gone bust kid. Looks like you\'re ours now. Sorry.')
                break
            print('Your cash: {}'.format(CASH))
            bet = int(input('Place your bet > '))
            if bet <= 0 or bet > CASH:
                print('Think you\'re funny?')
                continue
            else:
                CASH -= bet

                house_card = CARDS[random.randint(0,12)]
                player_card = CARDS[random.randint(0,12)]

                guess = input('You\'ve got a {}. You think the house is higher or lower?'.format(player_card['face']))

                if guess.startswith('h'):
                    if house_card['value'] > player_card['value']:
                        print('Congrats. House had a {} you had a {}. Looks like you win this round'.format(house_card['face'], player_card['face']))
                        CASH += bet * 2
                        continue
                    else:
                        print('Sorry. House had a {} you had a {}. Better luck next time.'.format(house_card['face'], player_card['face']))
                elif guess.startswith('l'):
                    if house_card['value'] < player_card['value']:
                        print('Congrats. House had a {} you had a {}. Looks like you win this round'.format(house_card['face'], player_card['face']))
                        CASH += bet * 2
                        continue
                    else:
                        print('Sorry. House had a {} you had a {}. Better luck next time.'.format(house_card['face'], player_card['face']))
                else:
                    print('You don\'t have to play right. It\'s your call, but I\'m keeping that {} bucks'.format(bet))

    else:
        print('Then why are you here?')

if __name__ == '__main__':
    main()