from ast import Str
import os
import random
import numpy as np

os.system('cls' if os.name == 'nt' else 'clear')
player1 = input('enter player 1 name: ')
player2 = input('enter player 2 name: ')
rounds = int(input('enter number of rounds: '))

leader_board = {player1: 0, player2: 0}

def print_score():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'{"-" * 30}\nLeaderboard\n{"-" * 30}')
    print(f'{player1} {leader_board[player1]} - {leader_board[player2]} {player2}\n')
    print(f'{"-" * 30}\nLast round\n{"-" * 30}')
    for player in players:
        total = np.sum(scores[player])
        mean = int(np.mean(scores[player]))
        std = int(np.std(scores[player]))
        print(f'{player} = {total:,} {scores[player]} (avg: {mean:,} | std: {std:,})')
    score_delta = np.abs(np.sum(scores[player1]) - np.sum(scores[player2]))
    print(f'score delta: {score_delta:,}\n')

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    scores = {player1: [], player2: []}
    players = list(scores.keys())
    random.shuffle(players)
    
    for round in range(rounds):
        print(f'{"-" * 30}\nRound {round + 1} of {rounds}\n{"-" * 30}')
        for i, player in enumerate(players):
            s = ''
            while s.isnumeric() == False:
                s = input(f'{player}: ')
            scores[player].append(int(s))
            if i > 0:
                print_score()

    if np.sum(scores[player1]) == np.sum(scores[player2]):
        leader_board[player1] += 0.5
        leader_board[player2] += 0.5
        end_of_game_message = f'tie game\n'
    else:
        winner = player1 if np.sum(scores[player1]) < np.sum(scores[player2]) else player2
        leader_board[winner] += 1
        end_of_game_message = f'{"*" * 3}{winner} wins{"*" * 3}\n'
    print_score()
    print(end_of_game_message)

    
    rematch = input('play again? ')
    if rematch[0].lower() == 'n':
        break
