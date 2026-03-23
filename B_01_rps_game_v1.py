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


# Main Routine

# Intialise game variables
mode = "regular"
rounds_played = 0

rps_list = ["rock", "paper", "scissors", "xxx"]


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


    user_choice = string_checker("Choose: ", rps_list)
    print("you chose", user_choice)

    if user_choice == "xxx":
        break

    rounds_played += 1


    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
     rounds_wanted += 1


# Game loop ends here

# Game History / Statistics area







