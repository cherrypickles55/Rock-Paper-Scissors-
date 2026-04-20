import random

# Check that users have entered a valid
# option based on a list

def string_checker(question, valid_ans=("yes", "no")):

    """ Check that users enter a valid word / first
    letter of the word based on a list of options. Defaults to yes / no."""

    error = f"Please enter a valid option from the following list: {valid_ans}"


    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()



        for var_item in valid_ans:
            # check if the user response is a word in the list
            if var_item == user_response:
                return var_item



            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == var_item [0]:
                return var_item


        # print error if user does not enter something that is valid
        print(error)
        print()



def int_check(question, exit_code=None):
    """ checks for an integer more than 0 (allows <enter>)"""


    while True:
        error = "Please enter an integer that is 1 or more."

        response = input(question)


        # check for infinite mode / exit code
        if response == exit_code:
            return exit_code


        try:
            # tries to make the response into an integer
            response = int(response)


            # checks that the number is more than / equal to 1
            if response < 1:
                print(error)

            else:
                return response


        except ValueError:
            # if the response is not an integer, displays an error
            print(error)




    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()



        for var_item in valid_ans:
            # check if the user response is a word in the list
            if var_item == user_response:
                return var_item



            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == var_item [0]:
                return var_item

# Displays Instructions

def instructions():
    print("""
*** Instructions ***

To begin, choose the number (or press <enter> for infinite mode).



Then play against the computer. You need to choose R (rock), P (paper) or S(scissors).



The rules are as follows:
O Paper beats rock
O Rock beats scissors 
O Scissors beats paper 

Press <xxx> to end the game at anytime. 

Good Luck ! 
     """)


# compare user / computer choice and returns
# result (win / lose / tie)
def rps_compare(user, comp):

    if user == comp:
        round_result = "tie"

    # There are three ways to win
    elif user == "paper" and comp == "rock":
        round_result = "win"
    elif user == "scissors" and comp == "paper":
        round_result = "win"
    elif user == "rock" and comp == "scissors":
        round_result = "win"


     # if it's not a win / tie, then it's a loss
    else:
        round_result = "lose"



    return round_result



# Main Routine

# Intialise game variables
mode = "regular"
rounds_played = 0
rounds_tied = 0
rounds_lost = 0

rps_list = ["rock", "paper", "scissors", "xxx"]
game_history = []


print ("💎📄✂️ Rock / Paper / Scissors Game 💎📄✂️")
print()



# Ask user for number of rounds / infinite mode

rounds_wanted = int_check( "How many rounds? <enter for infinite>: ","" )

if rounds_wanted == "":
    # change mode to infinite if users press <enter>
    mode = "infinite"

    # set rounds_wanted to a number for comparison later.
    rounds_wanted = 5

# Game loop starts here
while rounds_played < rounds_wanted:

     # Rounds headings
    if mode == "infinite":
        rounds_heading = f"\n🎀🎀🎀 Round {rounds_played + 1} (Infinite Mode) 🎀🎀🎀"
    else:
        rounds_heading = f"\n🦑🦑🦑 Round {rounds_played + 1} of {rounds_wanted} 🦑🦑🦑"


    print(rounds_heading)
    print()

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(rps_list[: -1])
    print("Computer choice", comp_choice)

    user_choice = string_checker("Choose: ", rps_list)
    print("you chose", user_choice)

    if user_choice == "xxx":
        break

    result = rps_compare(user_choice, comp_choice)

    # Adjust game lost / game tied counters and add results to game history
    if result == "tie":
        rounds_tied += 1
        feedback = "😬😬 It's a tie!😬😬"
    elif result == "lose":
        rounds_lost += 1
        feedback = "🤣🤣 You lose. 🤣🤣"
    else:
        feedback = "😄😄 You won. 😄😄"


    # Set up round feedback and output it user
    # Add it to the game history list (include the round number)
    rounds_feedback = (f"{user_choice} vs {comp_choice}, {feedback}")
    history_item = f"Round: {rounds_played} - {rounds_feedback}"

    print(rounds_feedback)
    game_history.append(history_item)

    rounds_played += 1


    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
     rounds_wanted += 1


# Game loop ends here

# Game History / Statistics area


    # Calculate Statistics
    rounds_won = rounds_played - rounds_tied - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    percent_tied = 100 - percent_won - percent_lost

    # Output Game Statistics
    print("📊📊📊 Game Statistics📊📊📊")
    print(f"👍 Won: {percent_won:.2f} \t"
          f"😢 Lost: {percent_lost:.2f} \t "
          f"👔 Tied {percent_tied:.2f}")

    # ask user if they want to see their game history and output it if requested.
    see_history = string_checker("\nDo you want to see your game history? ")
    if see_history == "yes":
        for item in game_history:
            print(item)

    print()
    print("Thanks for playing.")

else:
    print("🐣🐣🐣 Oops - You chickened out! 🐣🐣🐣")





