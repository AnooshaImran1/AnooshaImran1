#Anoosha Imran, Mariam Raheem

# Create a rock-paper-scissors game!
# - Play once and report the result
# - Play in a loop and record how many wins and losses happen?
# - Allow choosing how many human players there are, from 0-2?
# - Organize everything into functions?
# - Organize everything into classes??

from numpy import random

choices = ['rock', 'paper', 'scissors']

p1 = input('Pick one of rock, paper or scissors: ')
p2 = random.choice(choices)

# StackOverflow for setting a Rock-Paper-Scissors game in Python: https://stackoverflow.com/questions/46939745/rock-paper-scissors-python
# StackOverflow for defining game with multiple rounds: https://stackoverflow.com/questions/40621578/making-a-rock-paper-scissors-game-in-python-just-curious-on-how-to-make-multi
    

winning_pairs = {'paper':'rock',
                 'rock':'scissors',
                 'scissors':'paper'}

def my_game(p1, p2):
    print(f"\nPlayer 1 chose {p1}.\nPlayer 2 chose {p2}.")
    
    if p1 == p2:
        print(f"Both players selected {p1}.")
        return 'It is a tie!'
    
    elif winning_pairs[p1] == p2:
        print(f'{p1} defeats {p2}.')
        return 'Player 1 won!'
    
    else:
        print(f'{p2} defeats {p1}.')
        return 'Player 1 lost!'

my_game(p1, p2)

# 2) Play in a loop and record how many wins and losses happen?

def my_games_multiple(no_of_games):
    wins = 0
    losses = 0
    ties = 0
    remaining_games = no_of_games
    
    while remaining_games > 0:
        p1 = input('Pick one of rock, paper or scissors: ')
        p2 = random.choice(choices)
        result = my_game(p1, p2)
        
        if result == 'Player 1 won!':
            wins += 1
        elif result == 'Player 1 lost!':
            losses += 1
        else:
            ties += 1
        
        remaining_games -= 1
    
    print(f"\nPlayer 1's Results:\nWins: {wins}\nLosses: {losses}\nTies: {ties}")

my_games_multiple(3)

# 3) Allow choosing how many human players there are, from 0-2?
def my_games_multiple(no_of_games, no_of_players):
    wins = 0
    losses = 0
    ties = 0
    remaining_games = no_of_games
    
    while remaining_games > 0:
        if no_of_players == 2:
            p1 = input('Player 1, pick one of rock, paper, or scissors: ')
            p2 = input('Player 2, pick one of rock, paper, or scissors: ')
        elif no_of_players == 1:
            p1 = input('Player 1, pick one of rock, paper, or scissors: ')
            p2 = random.choice(choices)
        else:
            p1 = random.choice(choices)
            p2 = random.choice(choices)
        
        result = my_game(p1, p2)
        
        if result == 'Player 1 won!':
            wins += 1
        elif result == 'Player 1 lost!':
            losses += 1
        else:
            ties += 1
        
        remaining_games -= 1
    
    print(f"\nPlayer 1's Results:\nWins: {wins}\nLosses: {losses}\nTies: {ties}")

# Fix number of games, allow user to input number of players
no_of_players = int(input('How many human players are there, from 0-2?'))

my_games_multiple(3, no_of_players)

# Allow user to input number of rounds to play and number of players
no_of_games = int(input('How many rounds would you like to play? '))
no_of_players = int(input('How many human players are there, from 0-2? '))

my_games_multiple(no_of_games, no_of_players)

# 4) Organize everything into functions?

choices = ['rock', 'paper', 'scissors']

winning_pairs = {'paper': 'rock',
                 'rock': 'scissors',
                 'scissors': 'paper'}

def player_choice(player):
    return input(f'Player {player}, input your choice: ')

def computer_choice():
    return random.choice(choices)

def play_game(p1, p2):
    print(f"\nPlayer 1 chose {p1}.\nPlayer 2 chose {p2}.")
    
    if p1 == p2:
        print(f"Both players selected {p1}.")
        return 'It is a tie!'
    
    elif winning_pairs[p1] == p2:
        print(f'{p1} defeats {p2}.')
        return 'Player 1 won!'
    
    else:
        print(f'{p2} defeats {p1}.')
        return 'Player 1 lost!'

def my_games_multiple(no_of_games, num_human_players):
    wins = 0
    losses = 0
    ties = 0
    
    for _ in range(no_of_games):
        if num_human_players == 2:
            p1 = player_choice(1)
            p2 = player_choice(2)
        elif num_human_players == 1:
            p1 = player_choice(1)
            p2 = computer_choice()
        else:
            p1 = computer_choice()
            p2 = computer_choice()
        
        result = play_game(p1, p2)
        
        if result == 'Player 1 won!':
            wins += 1
        elif result == 'Player 1 lost!':
            losses += 1
        else:
            ties += 1
    
    print(f"\nPlayer 1's Results:\nWins: {wins}\nLosses: {losses}\nTies: {ties}")

no_of_games = int(input('How many rounds would you like to play? '))
no_of_players = int(input('How many human players are there, from 0-2? '))

my_games_multiple(no_of_games, no_of_players)

# 5) Organize everything into classes??

class PlayRockPaperScissors:
    def __init__(self, no_of_players):
        self.choices = ['rock', 'paper', 'scissors']
        self.winning_pairs = {'paper':'rock', 'rock':'scissors', 'scissors':'paper'}
        self.no_of_players = no_of_players
        self.wins = 0
        self.losses = 0
        self.ties = 0

    def player_choice(self, player):
        return input(f'Player {player}, input your choice: ')

    def computer_choice(self):
        return random.choice(self.choices)

    def play_game(self, p1, p2):
        print(f"\nPlayer 1 chose {p1}.\nPlayer 2 chose {p2}.")
        
        if p1 == p2:
            print(f"Both players selected {p1}.")
            return 'It is a tie!'
        
        elif self.winning_pairs[p1] == p2:
            print(f'{p1} defeats {p2}.')
            return 'Player 1 won!'
        
        else:
            print(f'{p2} defeats {p1}.')
            return 'Player 1 lost!'

    def play_multiple_games(self, no_of_games):
        self.wins = 0
        self.losses = 0
        self.ties = 0
        
        for _ in range(no_of_games):
            if self.no_of_players == 2:
                p1 = self.player_choice(1)
                p2 = self.player_choice(2)
            elif self.no_of_players == 1:
                p1 = self.player_choice(1)
                p2 = self.computer_choice()
            else:
                p1 = self.computer_choice()
                p2 = self.computer_choice()
            
            result = self.play_game(p1, p2)
            
            if result == 'Player 1 won!':
                self.wins += 1
            elif result == 'Player 1 lost!':
                self.losses += 1
            else:
                self.ties += 1
        
        print(f"\nPlayer 1's Results:\nWins: {self.wins}\nLosses: {self.losses}\nTies: {self.ties}")

no_of_players = int(input('How many human players are there, from 0-2? '))
no_of_games = int(input('How many rounds would you like to play? '))

game = PlayRockPaperScissors(no_of_players)
game.play_multiple_games(no_of_games)
