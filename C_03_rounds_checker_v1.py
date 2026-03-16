def int_check(question, exit_code=None):



    while True:
        error = "Please enter an integer that is 0 or more."

        # ask the question
        response = input(question)

        if response == exit_code:
           return response


        try:
            response = int(response)

            # checks that the number is more than / equal to 13
            if response < 0:
                print(error)

            else:
                return response

        except ValueError:
            print(error)



# main routine
how_many = int_check("How many questions, <enter> for "
                     "infinite? ", "")

print(f"you chose {how_many}")
