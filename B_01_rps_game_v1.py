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





# Main Routine

# Intialise game variables
mode = "regular"
rounds_played = 0


print ("💎📄✂️ Rock / Paper / Scissors Game 💎📄✂️")
print()

# Instructions

# Ask user for number of rounds / infinite mode

rounds_wanted = int_check( "How many rounds? <enter for infinite>: ","" )

if rounds_wanted == "":
    # change mode to infinite if users press <enter>
    mode = "infinite"
    print ("you chose infinite")

    # set rounds_wanted to a number for comparison later.
    rounds_wanted = 5

# Game loop starts here
while rounds_played <= rounds_wanted:
    user_choice = input("Choose: ")

    if user_choice == "xx":
        break
        
    rounds_played += 1
    print("rounds played: ", rounds_played)

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
     rounds_wanted += 1

    print("rounds wanted: ", rounds_wanted)
# Game loop ends here

# Game History / Statistics area







