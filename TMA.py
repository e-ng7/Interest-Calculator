#Ernest Ng Er Rui
#Student ID: B1580997
#TG01
import time
print('Welcome to Ernest\'s UOB One Account interest calculator!\nPlease enter the following information: ')

#I begin my interest calculator programs with a combination of while loops and try/except blocks for my user input validations.
#Because I would want my users to enter float data for the following inputs, I used while loops to ensure that any invalid inputs would force the users to re-enter the value and return to the initial question.
#With the exception of ValueError, any invalid data would result in a while loop. To overcome any ValueError that may stop the program, I also executed try/except blocks to prevent any invalid data that results in a ValueError.
#The same while loop and except combination, named invalid_entry, was repeated for account balances, salary credits, and total card spending inputs.
time.sleep(2)
reattempt = True #This while loop called 'reattempt' was to loop the entire calculator at the end if the user selects the choice to re-calculate his interest.
try_again = True #This while loop called 'try_again' was to loop the menu at the end of the calculator program. The menu will be known as the exit menu where the user can choose to exit, re-do or view bill summary.
while reattempt:
    #Input for Account Balance
    invalid_entry = True #This while loop called 'invalid_entry' was to loop the question for the account balance if a ValueError or invalid entry was given.
    while invalid_entry:
        try:
            account_balance = float(input('Enter account balance as at end of the month:\nS$')) #If an invalid input or ValueError occurs, this account balance input prompt will loop and execute again.
            invalid_entry = False #If a valid input was given, the loop will end with the invalid_entry variable becoming false.
        except ValueError:
            #As mentioned earlier above in line 8, this except function was used to invalidate any entries (e.g. Twenty dollars) that cannot be converted into a float data and results in a ValueError.
            #If an input cannot be converted into float data, the program would detect a ValueError and while loop back to the initial question. This prevents any ValueError from ending the program.
            print('\n\nSorry, you entered an invalid entry.\nPlease enter a numerical value.') #This is a prompt which will execute when a ValueError occurs or invalid data is given by the user to guide users to enter a valid data.

    #Input for Card Spending (Repeated same while loops and try/exception blocks for user input validation)
    invalid_entry = True #This while loop called 'invalid_entry' was to loop the question for UOB card spending if a ValueError or invalid entry was given. It will not loop back to the first question of account balance.
    while invalid_entry:
        try:
            card_spend = float(input('\nEnter total amount spent on UOB One Card this month:\nS$'))
            invalid_entry = False #If a valid input was given, the loop will end with the invalid_entry variable becoming false.
        except ValueError:
            print('\n\nSorry, you entered an invalid entry.\nPlease enter a numerical value.')

    #Input for Salary credited (Repeated same while loops and try/exception blocks for user input validation)
    invalid_entry = True #This while loop called 'invalid_entry' was to loop the question for salary credited if a ValueError or invalid entry was given.
    while invalid_entry:
        try:
            salary = float(input('\nEnter total salary amount credited this month: \nS$'))
            invalid_entry = False#If a valid input was given, the loop will end with the invalid_entry variable becoming false.
        except ValueError:
            print('\n\nSorry, you entered an invalid entry.\nPlease enter a numerical value.')

#The next part of the calculation, users will be prompted for details of the bills paid through their UOB One account. The inputs would be added into the dictionary named 'bill_summary'.
    bill_summary = {} #This is the dictionary where all bills input by users will be listed. At the end of the calculation, users could retrieve the details of bills recorded for the calculation.

    Bill_Entry = True #Another while loop named 'Bill_Entry' was used here to loop the bill entry process when a ValueError occurs or when an invalid entry is given by the users.
    #Multiple while loops are used because I did not want a invalid entry or ValueError to loop to the beginning of the program or restart the whole calculator to the beginning.
    while Bill_Entry:
        try:
            check = input("\nAre there any bills paid this month? \n Yes/No\n>")
            if(check == 'Yes'):
                category = input("\nBill Category: ") #Users are prompted to input the name of their bill here
                amount = float(input("\nBill Amount: S$")) #A follow-up prompt for the bill's amount will be executed
                bill_summary[category] = amount #Both the bill category and bill amount will be added to the dictionary named bill_summary
                Bill_Entry = False #The while loop will end here if both inputs are valid inputs or not ValueError
            elif(check == 'No'):
                print('No bills were recorded.') #If user inputs 'No' to indicate that there are no bills paid this month at all, the loop will end immediately and proceed to calculate the interest earned.
                Bill_Entry = False
            else:
                print("Hmm, it seems that you have entered an invalid entry.\nPlease enter 'Yes' or 'No'.")
                #If the user enters an input that is invalid (e.g. non-float data for amount "Twenty-one"), this prompt will be executed.
                #The program will loop back to the bill entry questions.
                time.sleep(2)
        except ValueError:
            print("Hmm, it seems that you have entered an invalid amount.\nPlease enter a valid amount.")
            #If the user enters an input that causes a ValueError, this same prompt will also be executed.
            time.sleep(2)

    if(check == 'Yes'):
        Bill_Entry = True
        while Bill_Entry:
            try:
                check2 = input("\nAny other bills? Yes/No\n\n")
                #This follow-up question will be executed so that the user could input more bills paid during the month.
                #The user could input any many bills as they like by entering 'Yes' value and filling in the bill name and amount, as the input prompt for any more bills will keep repeating/looping.
                if(check2 == 'Yes'):
                    category = input("\nBill Category: ")
                    amount = float(input("\nBill Amount: S$"))
                    bill_summary[category] = amount
                    # Both bill category and amount will be added to the dictionary accordingly.
                elif(check2 == 'No'):
                    Bill_Entry = False
                    #However if the user enters input 'No', the while loop ends and the input prompt for more bills will stop repeating.
                else:
                    print("Hmm, it seems that you have entered an invalid entry. \nPlease enter 'Yes' or 'No'.")
                    #If the user does not enter 'Yes' or 'No' data values for the question "Any other bills?", this prompt will execute for the user to do so and loop the question back again.
                    time.sleep(2)
            except ValueError:
                print("Hmm, it seems that you have entered an invalid amount.\nPlease enter a valid amount.")
                #If the user enters an input that results in a ValueError, I created an except function like the previous try/except blocks to execute the while loop whenever a ValueError occurs.
    time.sleep(3)
    bills_paid = len(bill_summary) #This variable was created to count the number of bills paid in the dictionary.
    #As the bonus interest is only applicable to One Account holders to pay at least three bills a month or credit $2000 salary minimum to the account,
    #I had to count the numbers of bills in the dictionary.


    #Here we check the rates that user is qualified for based on the inputs given. We follow the logic flow chart given in part (c) of the TMA.

    base_interest = float(0.0005/12)
    #This variable is the base interest rate per month. Account holders who do not meet the required $500 min card spending will only earn base interest rates.

    interest_rates_A = [0.01, 0.015, 0.02]
    interest_rates_B = [0.015, 0.02, 0.0333]
    #The two lists interest rates A and B are the bonus rates for the user if the One account meets the required card spending, salary credits or monthly bills count.
    #The first items in both lists are the interest rates for the first S$10,000 in the account balance.
    #The second items in both lists are the interest rates for the next S$20,000 in the account balance.
    #And the third items in both lists are the interest rates for the next S$20,000 in the account balance.
    #interest_rates_A list will be referenced if card spend is at least $500 (card_spend >= 500) but no salary credits or monthly bills paid.
    #interest_rates_B list will be referenced to if card spend is at least $500 and either min salary credited is $2,000 or at least three bills are paid through UOB One account.
    #In other words, salary >= 2000 and bills_paid >= 3
    if card_spend >= 500:
        #The first criteria was to check if card spend was >= $500 because if the account holder does not meet this criteria, they do not qualify for any bonus interest and only base interest.
        #If the variable of card_spend < 500, the calculator skips all arguments below and proceeds to else argument at the end.
        if salary >= 2000:
            print("\nInterest Summary")
            print("-" * 25)
            #This if function tests if the salary variable meets the criteria of at least S$2000 and proceeds to calculate the interest if the argument of salary >= 2000 is true.
            #At this point, the program runs a few arguments to calculate the interest earned depending on the account_balance variable.
            #The following arguments and formulas are known as the Interest Earned Calculation block, which will be repeated later.
            if account_balance <= 10000:
                #If the argument account_balance <= 10000 is true, the interest earned will be calculcated with the formula below.
                annual_interest_rate = interest_rates_B[0]
                monthly_interest_rate = annual_interest_rate / 12
                interest_earned = (round(monthly_interest_rate * account_balance, 4))
                #Since the account balance is <= S$10,000, the formula for interest earned would only be the first bonus interest rate in the dictionary * the account balance.
                print(f'Total interest earned on S${account_balance}:\nS${interest_earned}')
                #After the interest is calculated, an exit menu would appear.
                reattempt = False
                try_again = True
                while try_again:#The exit menu would be on a while loop and prompt the user to input an integer 1, 2, or 3.
                    reattempt = True
                    try:
                        option = int(input('\n\nWhat would you like to do now? \n1. Re-calculate interest earned. \n2. See bill summary \n3. Quit interest calculator. \n>'))
                        if option == 1:
                            #If the user inputs 1, the while loop would go back to the beginning of the calculator and re-calculate from the beginning.
                            print("\n\nLet's try again!")
                            try_again = False
                            time.sleep(2)
                        elif option == 2:
                            #If the user inputs 2, a bill summary made from items on the dictionary {bill_summary} will be printed.
                            #This is so that the user could see the bill details for the month
                            print(f"\n\nBill Summary \nTotal number of bills paid: {bills_paid}\n\nBill Details:")
                            for bill, amt in list(bill_summary.items()):
                                print(f'{bill} : S${amt}') #this function will print all items in the dictionary 'bill_summary'

                        elif option == 3:
                            print("\nThank you for using Ernest's interest calculator!\nGoodbye!")
                            #If user enters input 3, all remaining while loops will end and a goodbye message will be printed. This effectively ends the entire program.
                            try_again = False
                            reattempt = False
                    except ValueError:
                        print("Hmm, it seems that you have entered an invalid option.\nPlease enter 1, 2 or 3.")
                        #If the user enters an input that cannot be converted into an integer, there would be a ValueError.
                        #Similar to the try/except blocks before, the except function here would ignore the ValueError and proceed to while loop to the exit menu again.
            elif account_balance <= 30000:
                #If the first argument under if account_balance <= 10,000 is false, the program will proceed to the next argument at elif account_balance <= 30,000
                #because if there is more than 10,000 in the account, the next 20,000 would be earning a higher interest rate (the 2nd item in the interest rate list)
                #Therefore, the formula would be different and be as follows
                interest1 = (interest_rates_B[0] / 12) * 10000 #interest1 variable represents the interest earned in the first S$10,000 in the account.
                print(f"Interest earned on first S$10,000: S${interest1}")
                interest2 = (interest_rates_B[1] / 12) * (account_balance - 10000) #interest2 variable represents the interest earned in the next S$20,000 in the account.
                #The program would print out a breakdown of the interest earned on the first S$10,000 and next S$20,000 in the account balance.
                print(f"Interest earned on remaining S${float(account_balance - 10000)}: S${interest2}")
                interest_earned = round(interest1 + interest2, 4) #Both variable interest1 and interest2 are added up into the total interest earned and rounded to the nearest 4 significant numbers.
                print(f"Total interest earned:\nS${interest_earned}")
                reattempt = False
                try_again = True
                while try_again:
                    reattempt = True
                    #Once again, the exit menu will appear with a prompt for the user to input an integer 1, 2 or 3.
                    try:
                        option = int(input('\n\nWhat would you like to do now? \n1. Re-calculate interest earned. \n2. See bill summary \n3. Quit interest calculator. \n>'))
                        #This input prompts the user to enter input 1, 2 or 3.
                        if option == 1:
                            #If 1 in entered by the user, the while loop try_again will be stopped and the other while loop 'reattempt' will loop to the beginning of the program again to recalculate the interest earned.
                            print("\n\nLet's try again!")
                            try_again = False #This stops the while loop try_again and effectively ends the repeat of exit menu.
                            time.sleep(2)
                        elif option == 2:
                            #When the user inputs 2, all items in the dictionary 'bill_summary' will be printed as a summary to show the user the bills paid for the month
                            print(f"\n\nBill Summary \nTotal number of bills paid: {bills_paid}\n\nBill Details:")
                            for bill, amt in list(bill_summary.items()):
                                print(f'{bill} : S${amt}') #this function will print all items in the dictionary 'bill_summary' and display a summary of the bill input entries for the user

                        elif option == 3:
                            #When the user inputs 3, the program will end all while loops and print a goodbye message.
                            print("\nThank you for using Ernest's interest calculator!\nGoodbye!")
                            try_again = False
                            reattempt = False
                    except ValueError: #An except function was used to overlook any ValueError arising from user's input and lead to a while loop to the exit menu again.
                        print("Hmm, it seems that you have entered an invalid option.\nPlease enter 1, 2 or 3.") #A ValueError would lead to the exit menu and this prompt would be printed to prompt the user to enter 1,2 or 3.
            elif account_balance <= 50000: #This argument represents any account balance above S$50,000 will use the following formulas
                interest1 = (interest_rates_B[0] / 12) * 10000
                print(f"Interest earned on first S$10,000: S${interest1}")
                interest2 = (interest_rates_B[1] / 12) * 20000
                print(f"Interest earned on next S$20,000: S${interest2}")
                interest3 = (interest_rates_B[2] / 12) * (account_balance - 30000)
                print(f"Interest earned on remaining S${float(account_balance - 30000)}: S${interest3}")
                interest_earned = round(interest1 + interest2 +interest3, 4)
                print(f"Total interest earned:\nS${interest_earned}")
                reattempt = False
                try_again = True
                while try_again:
                    reattempt = True
                    try:
                        option = int(input('\n\nWhat would you like to do now? \n1. Re-calculate interest earned. \n2. See bill summary \n3. Quit interest calculator. \n>'))
                        if option == 1:
                            #When the user inputs 1, the while loops brings the user back to the beginning and re-calculate the interest earned from scratch.
                            print("\n\nLet's try again!")
                            try_again = False
                            time.sleep(2)
                        elif option == 2:
                            #When the user inputs 2 at the exit menu, a bill summary would be printed from the items of the dictionary "bill_summary"
                            print(f"\n\nBill Summary \nTotal number of bills paid: {bills_paid}\n\nBill Details:")
                            for bill, amt in list(bill_summary.items()):
                                print(f'{bill} : S${amt}') #this function will print all items in the dictionary 'bill_summary'

                        elif option == 3:
                            print("\nThank you for using Ernest's interest calculator!\nGoodbye!")
                            try_again = False
                            reattempt = False
                    except ValueError:
                        print("Hmm, it seems that you have entered an invalid option.\nPlease enter 1, 2 or 3.")
            else:
                #If all three arguments under ifs and elifs above were False, that means the account balance should be more then S$50,000 and will follow the following formulas
                interest1 = (interest_rates_A[0] / 12) * 10000
                #This variable would represent the interest earned on the first S$10,000 in the account
                print(f"Interest earned on first S$10,000: S${interest1}")
                interest2 = (interest_rates_A[1] / 12) * 20000
                #interest2 variable is the interest earned on the next S$20,000 in the account at the 2nd item in the interest rate list
                print(f"Interest earned on next S$20,000: S${interest2}")
                interest3 = (interest_rates_B[2] / 12) * 20000
                #interest3 variable represents the interest earned on the last S$20,000 of the first S$50,000 in the account balance
                print(f"Interest earned on next S$20,000: S${interest3}")
                interest4 = (base_interest) * (float(account_balance - 50000))
                #interest4 is the base interest earned on the remaining amount in excess of S$50,000
                print(f"Interest earned on remaining S${float(account_balance - 50000)}: S${interest4}")
                interest_earned = round((interest1 + interest2 + interest3 + interest4), 4) #interest_earned variable is the total of all four different interest tiers
                print(f"Total interest earned: \nS${interest_earned}")
                reattempt = False
                try_again = True
                while try_again:
                    #The try_again while loops executes the exit menu and gives the users choices to re-calculate, see bill summary or quit the program.
                    reattempt = True
                    try:
                        option = int(input('\n\nWhat would you like to do now? \n1. Re-calculate interest earned. \n2. See bill summary \n3. Quit interest calculator. \n>'))
                        if option == 1:
                            print("\n\nLet's try again!")
                            try_again = False
                            time.sleep(2)
                        elif option == 2:
                            print(f"\n\nBill Summary \nTotal number of bills paid: {bills_paid}\n\nBill Details:")
                            for bill, amt in list(bill_summary.items()):
                                print(f'{bill} : S${amt}') #this function will print all items in the dictionary 'bill_summary'

                        elif option == 3:
                            print("\nThank you for using Ernest's interest calculator!\nGoodbye!")
                            try_again = False
                            reattempt = False
                    except ValueError:
                        print("Hmm, it seems that you have entered an invalid option.\nPlease enter 1, 2 or 3.")
                        #The exact Interest Earned Calculation block is used for the next argument if bills_paid >= 3 because the account holder is entitled to earn the bonus interest rates if there is a min S$2,000 salary credit or at least 3 bills are paid via GIRO
        else:
            if bills_paid >= 3:
                #If the argument salary >= 2000 is false, the program will skip all the elif functions and proceed to the above argument bills_paid >= 3 to check if the account holders has paid 3 bills this month.
                #If the argument bills_paid >= 3 concludes to be true, the program would proceed to calculate the interest earned with interest rates under list interest_rates_B.
                #The following formulas and arguments are the Interest Earned Calculation block and are identical to line 119 to 176.
                if account_balance <= 10000:
                    annual_interest_rate = interest_rates_B[0]
                    monthly_interest_rate = annual_interest_rate / 12
                    interest_earned = (round(monthly_interest_rate * account_balance, 4))
                    print(f'Total interest earned on S${account_balance}:\nS${interest_earned}')
                    reattempt = False
                    try_again = True
                    while try_again:
                        reattempt = True
                        try:
                            option = int(input('\n\nWhat would you like to do now? \n1. Re-calculate interest earned. \n2. See bill summary \n3. Quit interest calculator. \n>'))
                            if option == 1:
                                print("\n\nLet's try again!")
                                try_again = False
                                time.sleep(2)
                            elif option == 2:
                                print(f"\n\nBill Summary \nTotal number of bills paid: {bills_paid}\n\nBill Details:")
                                for bill, amt in list(bill_summary.items()):
                                    print(f'{bill} : S${amt}') #this function will print all items in the dictionary 'bill_summary'

                            elif option == 3:
                                print("\nThank you for using Ernest's interest calculator!\nGoodbye!")
                                try_again = False
                                reattempt = False
                        except ValueError:
                            print("Hmm, it seems that you have entered an invalid option.\nPlease enter 1, 2 or 3.")
                elif account_balance <= 30000:
                    interest1 = (interest_rates_B[0] / 12) * 10000
                    print(f"Interest earned on first S$10,000: S${interest1}")
                    interest2 = (interest_rates_B[1] / 12) * (account_balance - 10000)
                    print(f"Interest earned on remaining S${float(account_balance - 10000)}: S${interest2}")
                    interest_earned = round(interest1 + interest2, 4)
                    print(f"Total interest earned:\nS${interest_earned}")
                    reattempt = False
                    try_again = True
                    while try_again:
                        reattempt = True
                        try:
                            option = int(input('\n\nWhat would you like to do now? \n1. Re-calculate interest earned. \n2. See bill summary \n3. Quit interest calculator. \n>'))
                            if option == 1:
                                print("\n\nLet's try again!")
                                try_again = False
                                time.sleep(2)
                            elif option == 2:
                                print(f"\n\nBill Summary \nTotal number of bills paid: {bills_paid}\n\nBill Details:")
                                for bill, amt in list(bill_summary.items()):
                                    print(f'{bill} : S${amt}') #this function will print all items in the dictionary 'bill_summary'

                            elif option == 3:
                                print("\nThank you for using Ernest's interest calculator!\nGoodbye!")
                                try_again = False
                                reattempt = False
                        except ValueError:
                            print("Hmm, it seems that you have entered an invalid option.\nPlease enter 1, 2 or 3.")
                elif account_balance <= 50000:
                    interest1 = (interest_rates_B[0] / 12) * 10000
                    print(f"Interest earned on first S$10,000: S${interest1}")
                    interest2 = (interest_rates_B[1] / 12) * 20000
                    print(f"Interest earned on next S$20,000: S${interest2}")
                    interest3 = (interest_rates_B[2] / 12) * (account_balance - 30000)
                    print(f"Interest earned on remaining S${float(account_balance - 30000)}: S${interest3}")
                    interest_earned = round(interest1 + interest2 +interest3, 4)
                    print(f"Total interest earned:\nS${interest_earned}")
                    reattempt = False
                    try_again = True
                    while try_again:
                        reattempt = True
                        try:
                            option = int(input('\n\nWhat would you like to do now? \n1. Re-calculate interest earned. \n2. See bill summary \n3. Quit interest calculator. \n>'))
                            if option == 1:
                                print("\n\nLet's try again!")
                                try_again = False
                                time.sleep(2)
                            elif option == 2:
                                print(f"\n\nBill Summary \nTotal number of bills paid: {bills_paid}\n\nBill Details:")
                                for bill, amt in list(bill_summary.items()):
                                    print(f'{bill} : S${amt}') #this function will print all items in the dictionary 'bill_summary'

                            elif option == 3:
                                print("\nThank you for using Ernest's interest calculator!\nGoodbye!")
                                try_again = False
                                reattempt = False
                        except ValueError:
                            print("Hmm, it seems that you have entered an invalid option.\nPlease enter 1, 2 or 3.")
                else:
                    interest1 = (interest_rates_A[0] / 12) * 10000
                    print(f"Interest earned on first S$10,000: S${interest1}")
                    interest2 = (interest_rates_A[1] / 12) * 20000
                    print(f"Interest earned on next S$20,000: S${interest2}")
                    interest3 = (interest_rates_B[2] / 12) * 20000
                    print(f"Interest earned on next S$20,000: S${interest3}")
                    interest4 = (base_interest) * (float(account_balance - 50000))
                    print(f"Interest earned on remaining S${float(account_balance - 50000)}: S${interest4}")
                    interest_earned = round(interest1 + interest2 + interest3 + interest4, 4)
                    print(f"Total interest earned: \nS${interest_earned}")
                    reattempt = False
                    try_again = True
                    while try_again:
                        reattempt = True
                        try:
                            option = int(input('\n\nWhat would you like to do now? \n1. Re-calculate interest earned. \n2. See bill summary \n3. Quit interest calculator. \n>'))
                            if option == 1:
                                print("\n\nLet's try again!")
                                try_again = False
                                time.sleep(2)
                            elif option == 2:
                                print(f"\n\nBill Summary \nTotal number of bills paid: {bills_paid}\n\nBill Details:")
                                for bill, amt in list(bill_summary.items()):
                                    print(f'{bill} : S${amt}') #this function will print all items in the dictionary 'bill_summary'

                            elif option == 3:
                                print("\nThank you for using Ernest's interest calculator!\nGoodbye!")
                                try_again = False
                                reattempt = False
                        except ValueError:
                            print("Hmm, it seems that you have entered an invalid option.\nPlease enter 1, 2 or 3.")
            else:
                #This is the same Interest Earned Calculation block as line 119 to 176. The arguments and formulas are identical and was elaborated and explained earlier.
                #The only change is the reference of list interest_rates_A instead of interest_rates_B because the first two arguments of salary >= 2000 and bills_paid >= 3 were false
                if account_balance <= 10000:
                    annual_interest_rate = interest_rates_A[0]
                    monthly_interest_rate = annual_interest_rate / 12
                    interest_earned = (round(monthly_interest_rate * account_balance, 4))
                    print(f'Total interest earned on S${account_balance}:\nS${interest_earned}')
                    try_again = True
                    reattempt = False
                    while try_again:
                        reattempt = True
                        try:
                            option = int(input('\n\nWhat would you like to do now? \n1. Re-calculate interest earned. \n2. See bill summary \n3. Quit interest calculator. \n>'))
                            if option == 1:
                                print("\n\nLet's try again!")
                                try_again = False
                                time.sleep(2)
                            elif option == 2:
                                print(f"\n\nBill Summary \nTotal number of bills paid: {bills_paid}\n\nBill Details:")
                                for bill, amt in list(bill_summary.items()):
                                    print(f'{bill} : S${amt}') #this function will print all items in the dictionary 'bill_summary'

                            elif option == 3:
                                print('Thank you for using Ernest\'s interest calculator!')
                                try_again = False
                                reattempt = False
                        except ValueError:
                            print("Hmm, it seems that you have entered an invalid option.\nPlease enter 1, 2 or 3.")
                elif account_balance <= 30000:
                    interest1 = (interest_rates_A[0] / 12) * 10000
                    print(f"Interest earned on first S$10,000: S${interest1}")
                    interest2 = (interest_rates_A[1] / 12) * (account_balance - 10000)
                    print(f"Interest earned on remaining S${float(account_balance - 10000)}: S${interest2}")
                    interest_earned = round(interest1 + interest2, 4)
                    print(f"Total interest earned:\nS${interest_earned}")
                    reattempt = False
                    try_again = True
                    while try_again:
                        reattempt = True
                        try:
                            option = int(input('\n\nWhat would you like to do now? \n1. Re-calculate interest earned. \n2. See bill summary \n3. Quit interest calculator. \n>'))
                            if option == 1:
                                print("\n\nLet's try again!")
                                try_again = False
                                time.sleep(2)
                            elif option == 2:
                                print(f"\n\nBill Summary \nTotal number of bills paid: {bills_paid}\n\nBill Details:")
                                for bill, amt in list(bill_summary.items()):
                                    print(f'{bill} : S${amt}') #this function will print all items in the dictionary 'bill_summary'

                            elif option == 3:
                                print("\nThank you for using Ernest's interest calculator!\nGoodbye!")
                                try_again = False
                                reattempt = False
                        except ValueError:
                            print("Hmm, it seems that you have entered an invalid option.\nPlease enter 1, 2 or 3.")
                elif account_balance <= 50000:
                    interest1 = (interest_rates_A[0] / 12) * 10000
                    print(f"Interest earned on first S$10,000: S${interest1}")
                    interest2 = (interest_rates_A[1] / 12) * 20000
                    print(f"Interest earned on next S$20,000: S${interest2}")
                    interest3 = (interest_rates_A[2] / 12) * (account_balance - 30000)
                    print(f"Interest earned on remaining S${float(account_balance - 30000)}: S${interest3}")
                    interest_earned = round(interest1 + interest2 +interest3, 4)
                    print(f"Total interest earned:\nS${interest_earned}")
                    reattempt = False
                    try_again = True
                    while try_again:
                        reattempt = True
                        try:
                            option = int(input('\n\nWhat would you like to do now? \n1. Re-calculate interest earned. \n2. See bill summary \n3. Quit interest calculator. \n>'))
                            if option == 1:
                                print("\n\nLet's try again!")
                                try_again = False
                                time.sleep(2)
                            elif option == 2:
                                print(f"\n\nBill Summary \nTotal number of bills paid: {bills_paid}\n\nBill Details:")
                                for bill, amt in list(bill_summary.items()):
                                    print(f'{bill} : S${amt}') #this function will print all items in the dictionary 'bill_summary'

                            elif option == 3:
                                print("\nThank you for using Ernest's interest calculator!\nGoodbye!")
                                try_again = False
                                reattempt = False
                        except ValueError:
                            print("Hmm, it seems that you have entered an invalid option.\nPlease enter 1, 2 or 3.")
                else:
                    interest1 = (interest_rates_A[0] / 12) * 10000
                    print(f"Interest earned on first S$10,000: S${interest1}")
                    interest2 = (interest_rates_A[1] / 12) * 20000
                    print(f"Interest earned on next S$20,000: S${interest2}")
                    interest3 = (interest_rates_B[2] / 12) * 20000
                    print(f"Interest earned on next S$20,000: S${interest3}")
                    interest4 = (base_interest) * (float(account_balance - 50000))
                    print(f"Interest earned on remaining S${float(account_balance - 50000)}: S${interest4}")
                    interest_earned = round(interest1 + interest2 + interest3 + interest4, 4)
                    print(f"Total interest earned: \nS${interest_earned}")
                    try_again = True
                    reattempt = False
                    while try_again:
                        reattempt = True
                        try:
                            option = int(input('What would you like to do now? \n1. Re-calculate interest earned. \n2. See bill summary \n3. Quit interest calculator. \n'))
                            if option == 1:
                                print("Let's try again!")
                                try_again = False
                                time.sleep(2)
                            elif option == 2:
                                print(f"\n\nBill Summary \nTotal number of bills paid: {bills_paid}\n\nBill Details:")
                                for bill, amt in list(bill_summary.items()):
                                    print(f'{bill} : S${amt}')

                                # print(bills)
                            elif option == 3:
                                print('\nThank you for using Ernest\'s interest calculator!\nGoodbye!')
                                try_again = False
                                reattempt = False
                        except ValueError:
                            print("Hmm, it seems that you have entered an invalid option.\nPlease enter 1, 2 or 3.")
    else:
        interest_earned = round(base_interest * account_balance, 4) #This is the formula used for interest earned if the card_spend <= 500.
        print(f'\nSorry but you only qualify for the base interest of 0.05% per annum due to low card spending.\nTotal interest earned: S${interest_earned}')
        #If the user account inputs do not meet the first criteria where card_spend is >= $500, the program will skip all elif and move to this else.
        #The calculator would inform the account holder that they only qualify for base interest and no bonus interest was earned.
        #The total interest earned will be printed out.
        try_again = True
        while try_again:
            try:
                #At this part of the calculator, the user is given the choice to recalculate interest, see bill summary or end the program.
                #This part is also known as the exit menu.
                option = int(input('\n\nWhat would you like to do now? \n1. Re-calculate interest earned. \n2. See bill summary \n3. Quit interest calculator. \n>'))
                if option == 1:
                    #If the user inputs 1, the while loop 'reattempt' will execute and the first question of how much is in the account balance will be executed.
                    print("\n\nLet's try again!")
                    try_again = False #This is to end the while loop try_again which repeats the exit menu.
                    time.sleep(2)
                elif option == 2:
                    #If the user inputs 2, the calculator would print the bill summary which includes all the items in the bill summary dictionary.
                    print(f"\n\nBill Summary \nTotal number of bills paid: {bills_paid}\n\nBill Details:")
                    for bill, amt in list(bill_summary.items()):
                        print(f'{bill} : S${amt}')
                        #This function would print all the items in the bill summary dictionary.
                        #The try_again while loop will execute again and repeat the exit menu.

                elif option == 3:
                    #If the user inputs 3 at the exit menu, the calculator would print a thank you message and end all while loops.
                    print('\nThank you for using Ernest\'s interest calculator!\nGoodbye!')
                    try_again = False
                    reattempt = False
            except ValueError:
                print("Hmm, it seems that you have entered an invalid option.\nPlease enter 1, 2 or 3.")
                #If the user does not input a value that is convertible to an integer, it will result in a ValueError. The except function will be executed and it will print the above prompt before looping back to the exit menu.
