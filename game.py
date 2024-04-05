from player import Player
from random import randrange


# GAME CLASS

class Game:
    def __init__(self, name, players):
        self.name = name
        self.players = players

    def start_game(self):
        pass

    def end_game(self, name):
        print(f"\n{name} game ended.")
        winner = self.get_winner()
        if winner:
            print(f"\n{winner} wins!")
        else:
            print("\nIt's a tie!")


# TIC TAC TOE 

class TicTacToe(Game):
    def __init__(self, num_players, players):
        super().__init__("Tic Tac Toe", num_players)
        if num_players != 2:
            raise ValueError("Tic Tac Toe requires 2 players.")
        self.game_name = "Tic Tac Toe"
        self.board = [" "] * 9
        self.players = players
        self.current_player = self.players[0]

    def display_board(self):
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("-----------")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("-----------")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")

    def make_move(self):
        valid_move = False
        while not valid_move:
            try:
                move = int(input(f"{self.current_player}, enter your move (1-9): ")) - 1
                if 0 <= move < 9 and self.board[move] == " ":
                    self.board[move] = "X" if self.current_player == self.players[0] else "O"
                    valid_move = True
                else:
                    print("\nInvalid move. Try again.")
            except ValueError:
                print("\nInvalid input. Please enter a number between 1 and 9.")

    def switch_player(self):
        if self.current_player == self.players[1]:
            self.current_player = self.players[0]
        else:
            self.current_player = self.players[1]

    def is_game_over(self):
        # Check for a win and tie
        for i in range(3):
            if (
                self.board[i] == self.board[i + 3] == self.board[i + 6] != " " or
                self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2] != " "
            ):
                return True

        # Check for a diagonal win
        if (
            self.board[0] == self.board[4] == self.board[8] != " " or
            self.board[2] == self.board[4] == self.board[6] != " "
        ):
            return True
        # Check for a tie
        if " " not in self.board:
            return True
        return False

    def get_winner(self):
        # Check for a win
        for i in range(3):
            if (
                self.board[i] == self.board[i + 3] == self.board[i + 6] != " " or
                self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2] != " "
            ):
                return self.current_player
        # Check for a diagonal win
        if (
            self.board[0] == self.board[4] == self.board[8] != " " or
            self.board[2] == self.board[4] == self.board[6] != " "
        ):
            return self.current_player
        return None

    def start_game(self):
        print("\nTic Tac Toe game started!")
        self.display_board()

        while not self.is_game_over():
            self.switch_player()
            self.make_move()
            self.display_board()

        self.end_game(self.game_name)


# HANGMAN

class Hangman(Game):
    def __init__(self, players, topics):
        super().__init__("Hangman", players)
        self.current_player = players[0]
        self.topic = self.select_topic(topics)
        self.secret_word = self.select_word()
        self.guesses = set()

    def select_topic(self, topics):
        return topics

    def select_word(self):
        random_word = randrange(len(self.topic))
        return self.topic[random_word]

    def display_word(self):
        display_word = "".join(letter if letter in self.guesses else "_" for letter in self.secret_word)
        print(f"Word: {display_word}")

    def make_guess(self):
        guess = input(f"{self.current_player}, enter a letter: ").lower()
        if guess.isalpha() and len(guess) == 1:
            self.guesses.add(guess)
            if guess not in self.secret_word:
                print("\nIncorrect guess!")
        else:
            print("\nInvalid input. Please enter a single letter.")

    def is_game_over(self):
        if set(self.secret_word) <= self.guesses or len(set(self.secret_word) - self.guesses) == 0:
            return True  # All letters guessed
        return False

    def end_game(self):
        print(f"\nHangman game ended! The word was: {self.secret_word}")
        if set(self.secret_word) <= self.guesses:
            print(f"{self.current_player} wins!")
        else:
            print("\nIt's a tough word! Nobody wins.")

    def get_winner(self):
        if set(self.secret_word) <= self.guesses:
            return self.current_player
        return None

    def start_game(self):
        print("\nHangman game started!")
        self.display_word()

        while not self.is_game_over():
            self.make_guess()
            self.display_word()

        self.end_game()


# ROCK PAPER SCISSORS

class RockPaperScissors(Game):
    def __init__(self, players):
        super().__init__("Rock Paper Scissors", players)
        self.current_player = players[0]
        self.choices = ["Rock", "Paper", "Scissors"]

    def start_game(self):
        print("\nRock Paper Scissors game started!")
        while True:
            player_choice = self.get_player_choice()
            opponent_choice = self.get_opponent_choice()

            result = self.determine_winner(player_choice, opponent_choice)
            print(result)

            # Check if players want to play again
            play_again = input("\nDo you want to play again? (y/n): ").lower()
            if play_again != 'y':
                break

    def get_opponent_choice(self):
        import random
        return random.randint(0, 2)

    def get_player_choice(self):
        while True:
            print("1. Rock\n2. Paper\n3. Scissors")
            try:
                choice = int(input("\nEnter the number of your choice: "))
                if choice in [1, 2, 3]:
                    return choice - 1
                else:
                    print("\nInvalid input. Please enter a number between 1 and 3.")
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")

    def determine_winner(self, player_choice, opponent_choice):
        player_choice_name = self.choices[player_choice]
        opponent_choice_name = self.choices[opponent_choice]

        print(f"{self.current_player} chose {player_choice_name}")
        print(f"Computer chose {opponent_choice_name}")

        if player_choice == opponent_choice:
            return "\nIt's a tie!"
        elif (
            (player_choice == 0 and opponent_choice == 2) or
            (player_choice == 1 and opponent_choice == 0) or
            (player_choice == 2 and opponent_choice == 1)
        ):
            return f"{self.current_player} wins!"
        else:
            return f"Computer wins!"


