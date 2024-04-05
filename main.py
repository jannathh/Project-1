from game import TicTacToe, Hangman, RockPaperScissors
from player import Player
from scoreboard import Scoreboard 

def choose_game():
    while True:
        print("""\nWHAT WOULD YOU LIKE TO PLAY TODAY?
        1. Tic Tac Toe
        2. Hangman 
        3. Rock Paper Scissors""")

        try:
            choice = int(input("Enter the number of your choice: "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Error! Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Error! Please enter a numeric choice.")


def get_num_players():
    return int(input("\nEnter number of players: "))

def get_player_names(num_players):
    return [input(f"\nEnter the name of Player {i + 1}: ") for i in range(num_players)]

def get_hangman_topics():
    print("\nCHOOSE A TOPIC:")
    print("1. Fruits")
    print("2. Animals")
    print("3. Countries")
    print("4. Movies")

    choice = int(input("Enter the number of your choice: "))
    topics_dict = {
        1: ["apple", "banana", "orange"],
        2: ["cat", "dog", "elephant"],
        3: ["bahrain", "canada", "india"],
        4: ["inception", "avatar", "starwars"]
    }
    
    if choice in topics_dict:
        return topics_dict[choice]
    else:
        print("Invalid choice. Exiting program.")
        exit()

def prompt_to_start():
    input("\nPress enter key to start the game...")

#......
selected_game_choice = choose_game()

if selected_game_choice == 1:
    num_players = 2  
    selected_game = TicTacToe(num_players)
elif selected_game_choice == 2:
    selected_game = Hangman()
else:
    selected_game = RockPaperScissors()

selected_game_class = choose_game()
num_players = get_num_players()
player_names = get_player_names(num_players)

players = [Player(name) for name in player_names]
scoreboard = Scoreboard()

if selected_game_class == Hangman:
    hangman_topics = get_hangman_topics()
    selected_game = selected_game_class(players, hangman_topics)
else:
    selected_game = selected_game_class(players)  

# Prompt to start the game
prompt_to_start()

# Start and end the game
selected_game.start_game()
selected_game.end_game()     

# Update scores in the scoreboard
for player in players:
    scoreboard.update_score(player, 10)

# Display current scores
scoreboard.display_scores()