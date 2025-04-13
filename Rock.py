import random 

class Game 
    def __init__(self):
        self.choices = {"Rock", "Paper", "Scissors", "Lizard", "Spock "}
        self.rules = { 
            "Rock" : ["Scissors", "Lizard"], 
            "Paper" : ["Rock", "Spock"], 
            "Scissors" : ["Paper", "Lizard"], 
            "Lizard" : ["Spock", "Paper"],
            "Spock" : ["Scissors", "Rock"]
        }

    def start_game(self):
        player_name = input("Enter your name: ")
        computer = Computer()
        while True: 
            player_choice = Player.choose_option()
            computer_choice = Computer.choose_option()
            self.determine_winner(player, computer, player_choice, computer_choice)
            self.display_result(player, computer)
            if not self.play_again():
                break

    def determine_winner(self, player, computer, player_choice, computer_choice):
        print(f"{player.name} chose {player_choice}")
        print(f"Computer chose {computer_choice}")
        if player_choice == computer_choice:
            print("it's a tie!")
        elif computer_choice in self.rules:
            print(f"{player.name} wins this round!")
        else: print("Computer wins this round")

    def display_result(self, player, computer, player_score, player_choice, computer_choice):
        print(f"{player.name}'s Score: {player_score} | Computer's Score: {computer.score}")
        if player_chioce == computer_choice:
            player.update_score()
        elif computer_choice > player_choice:
            computer.update_score()

   def play_again(self):
        again = input('Do you want to play again? (yes/no): ')
        return again.lower() == 'yes'

class Player: 
    def __init__(self, name):
        self.name = name 
        self.score = 0 
    
    def choose_option(slf):
        choice = input(f"{self.nam}, choose Rock, Paper, SCissors, Lizard, or Spock: ")
        return choice 
    
    def update_score(self):
        self.score += 1 

class Computer:
    def __init__(self):
        self.score = 0 
    
    def choose_option(self):
        return random.choice(["Rock", "Paper", "Scissors", "Lizard", "Spock"])
    
    def update_score(self):
        self.score += 1 

if __name__ == "__main__":
    game = Game()
    game.start_game()