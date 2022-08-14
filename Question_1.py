
'''
#declared variable name - number_of_cookies:
The While True: try and except tells the program if the user enters something which isn't in positive value,
or null input it should trigger the except, print the error and head back to try.

#There is a built-in function input() to ask the user to enter the number of cookies they want,
the int command function is used to  convert the given input from string to integer data type

'''
while True:
    try:
        number_of_cookies = int(input('\nKindly would you enter the number of cookies you would you like to bake:'))
    except ValueError:
        print("Sorry, You have not entered anything.")
        continue
    
    if number_of_cookies < 0:
        print("Sorry, your response must not be negative number.")
        continue
    else:
        break
    '''
validation to check whether the number of cups is a positive value and proceed with the program
'''
if number_of_cookies >= 0:
    
    cups_of_sugar = 1.5
    cups_of_butter = 1
    cups_of_flour = 2.75
    produced_cookies = 48

    '''
I am now going to calculate to find out the number of cookies needed using the
above ingredient variables.
I am going to declare new variables assigned to this calculations that is:

cups_sugar_needed,
cups_of_butter_needed,
cups_of_flour_needed

'''

    cups_sugar_needed = (cups_of_sugar * number_of_cookies)/produced_cookies
    cups_of_butter_needed = (cups_of_butter * number_of_cookies) /produced_cookies
    cups_of_flour_needed = (cups_of_flour * number_of_cookies) /produced_cookies



    print('\nNumber of cookies the user wants to bake =', number_of_cookies, end='\n\n')
    print('The number of cups of sugar needed for',number_of_cookies,'cookies is:',round(cups_sugar_needed,2),
      '\n The number of cups of butter needed ',number_of_cookies,'cookies is:',round(cups_of_butter_needed,2),
      '\n The number of cups of flour needed ',number_of_cookies,'cookies is:',round(cups_of_flour_needed,2))

'''
I am now going to print or display the calculation that we have made above this code
The answers are displayed with two digits after the decimal point. Because
our calculation can give a number with 10 digits after the decimal depending with the
number of cookies. With two digits a person is able to estimate exactly the measurement of the
ingredients that are needed.Using the function round() to two decimal points to achieve this.

'''
