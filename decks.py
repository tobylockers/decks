# DECKS, version 1 - programmed by Toby Loughlin
import os
import time
import random
import json

print('Welcome to DECKS, version 1', '\n')

fileError = 'Account file does not exist!'
accountError = 'Invalid account details.'

def clear():
    os.system('cls') # Clears shell history

def details_check(user, pswd): # Look up against something
    if user == '':
        print(accountError)
        signin()
    else:
        return details[user]["password"] == pswd

def signin():
    global details
    try:
        with open('details.json') as file:
            details = json.load(file)
    except:
        print(fileError)
        exit()
    
    p1_signedin = False
    p2_signedin = False
    
    print('Account sign-in')
    
    if not p1_signedin:
        p1_username = input('PLAYER 1, Enter your username: ')
        p1_password = input('PLAYER 1, Enter your password: ')
        if details_check(p1_username, p1_password):# Authentication
            print('\n', 'PLAYER 1 -', p1_username, 'signed in.', '\n')
            p1_signedin = True # Authorisation
            time.sleep(1)
            clear()
        else:
            print(accountError)
    if not p2_signedin:
        p2_username = input('PLAYER 2, Enter your username: ')
        p2_password = input('PLAYER 2, Enter your password: ')
        if details_check(p2_username, p2_password):
            if p2_username == p1_username:
                print('\n', 'PLAYER 1 is already using that account!')
                time.sleep(2)
                print('Restarting sign-in...')
                time.sleep(3)
                clear()
                signin()
            else:    
                print('PLAYER 2 -', p2_username, 'signed in.', '\n')
                p2_signedin = True
                time.sleep(1)
                clear()
        else:
            print(accountError)
    
    return p1_username, p2_username
     
def game():
    colours = ['Black', 'Red', 'Yellow']
    colours_winning = { 'Red' : 'Black',
                        'Yellow' : 'Red',
                        'Black' : 'Yellow'}
    numbers = list(range(1, 11))
    deck = [[n, c] for n in numbers for c in colours] # Generate a deck of cards
    random.shuffle(deck) # Shuffle the cards

    p1 = []
    p2 = []
    
    p1_username, p2_username = signin() # Starts the login

    while len(deck) != 0: # Loop players taking cards from the deck
        print(f'''{len(deck)} cards left in deck''')
        time.sleep(3)
        clear()
        input('{}, take from deck: '.format(p1_username)) # Use string formatting to include player names in prompts
        p1.append(deck.pop())
        clear()
        print(f'''{p1_username} drew {p1[-1][0]} {p1[-1][1]}''') # Formatting for the exact card most recently appended to a player's deck
        input('{}, take from deck: '.format(p2_username))
        clear()
        p2.append(deck.pop())
        print(f'''{p2_username} drew {p2[-1][0]} {p2[-1][1]}''')
        if p1[-1][1] == p2[-1][1]: 
            if p1[0] < p2[0]: # For each draw of cards, compare against logic in brief
                print(p1_username,'wins, and gains', p2_username + "'s card!")
                p1.append(p2.pop()) # Winner of draw takes the card from the other player
            else:
                print(p2_username,'wins, and gains', p1_username + "'s card!")
                p2.append(p1.pop())
        elif colours_winning[p1[-1][1]] == p2[-1][1]: # Compare colour matrix
            print(p1_username,'wins, and gains', p2_username + "'s card!")
            p1.append(p2.pop())
        else:
            print(p2_username,'wins, and gains', p1_username + "'s card!")
            p2.append(p1.pop())
        time.sleep(2)
    
    return p1, p2, p1_username, p2_username
            
p1, p2, p1_username, p2_username = game()
if len(p1) > len(p2): # Winner is the one with the most cards
    print(p1_username, 'won this game with a total of', len(p1), 'cards!')
    details[p1_username]["wins"] += 1
else:
    print(p2_username, 'won this game with a total of', len(p2), 'cards!')
    details[p2_username]["wins"] += 1
    
input('Press RETURN to load the leaderboard: ')
clear()

place = 0

try:
    with open('details.json', 'w') as file: # Write to file
        json.dump(details, file, indent = 4)
except:
    print(fileError)
    exit()
    
scores_list = {key: value["wins"] for key, value in details.items()} # Creates a new dictionary with the player and wins
sorted_scores_list = sorted([(value, key) for (key, value) in scores_list.items()], reverse = True) # Creates a list of lists, ordered by winner, desc.
print('TOP 5 - WINS:')
for k in sorted_scores_list:
    print(k[0], '-', k[1]) # Loops and prints it out
    
print('Reload the program and login again to start a new game!')