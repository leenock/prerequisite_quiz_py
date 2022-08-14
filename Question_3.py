'''
Design and write a program that lets the user enter
the total rainfall for each of 12 months into a list.
The program should calculate and display the total rainfall for the year,
the average monthly rainfall, and the months with the highest and lowest amounts.

'''
def RainFall():


#i am going to define the year months using a list.

#Variable months_years is going to store name of the months of the year
    months_year=["january","february","March","April","May","June","July","August","September","Octomber","November","December"]
#variable months is going to store total rain per month
    months = [0] * 12
    sum = 0

#loop to take input from user
    for i in range(12):
        months[i]=float(input("Enter Total Rain in "+months_year[i]+" "))

#adding rain to sum
        sum+=months[i]

#printing result
    print("""\n\nTotal Rainfall: """+str(sum)+"""\nAverage Monthly Rainfall: """+str(sum/12)+"""

     \nLowest Rainfall: """+str(min(months))+""" In month of """+str(months_year[months.index(min(months))])+"""

     \nHighest Rainfall: """+str(max(months))+""" In month of """+str(months_year[months.index(max(months))]))


#calling function RainFall
RainFall() 
