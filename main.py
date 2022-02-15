import random

def play():
    user = input("Co wybierasz? 'K' to kamień, 'P' to papier, 'N' to nożyczki")
    computer = random.choice(['K', 'P', 'N'])

    if user == computer:
        return 'It\'s a tie'
    
    if is_win(user, computer):
        return 'Wygrałeś!'
    
    return 'Przegrałeś!'

def is_win(player, opponent):
    if (player == 'K' and opponent == 'N') or (player == 'N' and opponent == 'P') or (player == 'P' and opponent == 'R'):
        return True