import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_player_choice():
    while True:
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Please enter rock, paper, or scissors")

def who_wins(player, computer):
    if player == computer:
        return "tie"
    
    if (player == "rock" and computer == "scissors") or \
       (player == "paper" and computer == "rock") or \
       (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"

def show_choices(player, computer):
    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}")

def show_result(winner):
    if winner == "tie":
        print("It's a tie!")
    elif winner == "player":
        print("You win!")
    else:
        print("Computer wins!")

def show_score(player_score, computer_score):
    print(f"\nScore - You: {player_score} | Computer: {computer_score}")

def play_again():
    while True:
        again = input("\nWant to play again? (y/n): ").lower()
        if again in ['y', 'yes']:
            return True
        elif again in ['n', 'no']:
            return False
        print("Please enter y or n")

def main_game():
    print("Welcome to Rock Paper Scissors!")
    print("=" * 30)
    
    player_score = 0
    computer_score = 0
    
    while True:
        print("\nNew round!")
        
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        
        show_choices(player_choice, computer_choice)
        
        winner = who_wins(player_choice, computer_choice)
        show_result(winner)
        
        if winner == "player":
            player_score += 1
        elif winner == "computer":
            computer_score += 1
        
        show_score(player_score, computer_score)
        
        if not play_again():
            break
    
    print("\nFinal Score:")
    show_score(player_score, computer_score)
    
    if player_score > computer_score:
        print("You won overall! Great job!")
    elif computer_score > player_score:
        print("Computer won overall! Better luck next time!")
    else:
        print("Overall it's a tie! Good game!")
    
    print("Thanks for playing!")

if __name__ == "__main__":
    main_game()