import random

class Game:
    def __init__(self):
        self.choices = {"Rock", "Paper", "Scissors", "Lizard", "Spock"}
        self.rules = {
            "Rock": ["Scissors", "Lizard"],
            "Paper": ["Rock", "Spock"],
            "Scissors": ["Paper", "Lizard"],
            "Lizard": ["Spock", "Paper"],
            "Spock": ["Scissors", "Rock"]
        }

    def show_intro(self):
        print('\nWelcome to Rock, Paper, Scissors, Lizard, Spock!\n ') 
        while True:
            print("----------------------------")
            print("What would you like to do?")
            print("1: See the Rules")
            print("2: Start Game")
            print("3: Exit")
            print("----------------------------")

            choice = input("\nEnter 1, 2, or 3: ").strip()
            if choice == '1':
                self.show_rules()
            elif choice == '2':
                self.start_game()
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please enter 1, 2, or 3.")

    def show_rules(self):
        print("\nGame Rules:")
        print("- Rock crushes Scissors and crushes Lizard")
        print("- Paper covers Rock and disproves Spock")
        print("- Scissors cuts Paper and decapitates Lizard")
        print("- Lizard eats Paper and poisons Spock")
        print("- Spock smashes Scissors and vaporizes Rock\n")

    def start_game(self):
        player_name = input("Enter your name: ").strip().capitalize()
        player = Player(player_name)
        computer = Computer()

        while True:
            player_choice = player.choose_option()
            if player_choice in ["stop", "exit"]:
                print(f"\n{player.name}, You chose to stop the game. Returning to the main menu...\n")
                break


            computer_choice = computer.choose_option()
            self.determine_winner(player, computer, player_choice, computer_choice)
            self.display_result(player, computer)

    def determine_winner(self, player, computer, player_choice, computer_choice):
        print(f"\n{player.name} chose {player_choice}")
        print(f"Computer chose {computer_choice}")

        if player_choice == computer_choice:
            print("\n🤝 It's a tie! 🤝")
        elif computer_choice in self.rules.get(player_choice, []):
            print(f"\n🎉 {player.name} wins this round! 🎉")
            player.update_score()
        else:
            print("\n💻 Computer wins this round! 💻")
            computer.update_score()

    def display_result(self, player, computer):
        print(f"\nScoreboard:\n- {player.name}: {player.score}\n- Computer: {computer.score}\n")

 

class Player:
    def __init__(self, name: str):
        self.name = name
        self.score = 0

    def choose_option(self):
        while True:
            print(f"\n{self.name}, ")
            print("Choose one of: Rock, Paper, Scissors, Lizard, Spock")
            print("OR type 'Stop' or 'Exit' to end the game.")
            choice = input("Your choice: ").strip().capitalize()


            if choice.lower() in ["stop", "exit"]:
                return choice.lower()
            if choice in ["Rock", "Paper", "Scissors", "Lizard", "Spock"]:
                return choice
            else:
                print("\n Invalid choice. Please try again.")

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
    game.show_intro()