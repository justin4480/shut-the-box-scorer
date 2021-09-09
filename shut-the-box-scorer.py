import os
import random
import numpy as np

os.system('cls' if os.name == 'nt' else 'clear')
player1 = input('enter player 1 name: ')
player2 = input('enter player 2 name: ')
rounds = int(input('enter number of rounds: '))

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    scores = {player1: [], player2: []}
    players = list(scores.keys())
    random.shuffle(players)
    
    for round in range(rounds):
        for i, player in enumerate(players):
            s = input(f'{player}: ')
            scores[player].append(int(s))
            if i > 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'{"-" * 30}\nround {round + 1} of {rounds}\n{"-" * 30}')
                for player in players:
                    print(f'{player} = {sum(scores[player])} {scores[player]}')
                score_delta = sum(scores[player1]) - sum(scores[player2])
                print(f'\nscore delta: {score_delta:,}\n')

    if sum(scores[player1]) == sum(scores[player2]):
        print(f'tie game')
    else:
        print(f'{player1 if sum(scores[player1]) < sum(scores[player2]) else player2} wins\n')
    
    rematch = input('play again? ')
    if rematch[0].lower() == 'n':
        break
