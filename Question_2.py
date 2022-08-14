'''
A program  that predicts the approximate size of a population of organisms.
The application should allow the user to enter the starting number of organisms, the average daily population increase (as a percentage), and
the number of days the organisms will be left to multiply

'''
'''
Float datatype is Used for numbers that contain decimal points, or for fractions.
In our case a percentage can be of float type , so i am going to convert the input string type of percentage
to float data type so as to achieve our calculations.

'''

'''
I are going to use For loops to iterate over a sequence of given number of
days for the organism to multiply and a  range() function to return the
a new list with the number of days  of that specified range
'''

#Ask the user to enter the starting number of organisms and it stores the user input into a variable StartNumber_of_Organism
StartNumber_of_Organism = int(input("Kindly Enter the Starting number of organisms:"))

#Ask user to enter the average daily increase, and store that user input in Average_Percentage_Increase variable 
Average_Percentage_Increase = float(input("Kindly enter the Average daily increase as:"))

#Ask user to enter the number for  organisim Multiplication, and store that user input in Number_of_days_to_multiply variable
Number_of_days_to_multiply = int(input("Kindly enter the Number days for organisim Multiplication:"))

#first i am going to create a heading for our program for a good preview
# \t is a tab/indent if used in a string and will create a space between Day Approximate and population
print("Day\tPopulation of the organisms")

#Here i am going to store the decimal value of percentage of the average percentage increase into the variable Average_Percentage_Increase 
Average_Percentage_Increase =Average_Percentage_Increase/100

# I am going to store the start number of organism into a new variable called pop_Organisms
# basically it will store the value the user on the input value.
pop_Organisms = StartNumber_of_Organism

#Using the c variable,i am going to iterate iterate over each value from 1 to Number_of_days_to_multiply+1
for c in range(1, Number_of_days_to_multiply + 1):

#i ma going to print the number of days againist the equivalent number or population of the organisms which is rounded off to 5 decimal    
    print(c,"\t",str(round(pop_Organisms,5)))

#print function comes first so that the value of the starting number of organisms is calculated first.
#if print function comes last the calculation or final results will eliminate the first value /number
#and calculate from the second digit or value. 
   
#calculations of the organisms population plus the average percentage increase which divided by the starting number of the organisms the user did input    
    pop_Organisms = pop_Organisms + (Average_Percentage_Increase * pop_Organisms)
