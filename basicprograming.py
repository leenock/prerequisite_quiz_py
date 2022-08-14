#print("Hello world") #used to single line comment
'''print("ddHello world")
print("ddHello world")'''

#WAP TO ACCEPT VALUE IN PROGRAM AND DISPLAY IT

num = 100
print("your value for num: ",num)
print("Hello world.  \nwelcome to apu. \n\tThis is Pip class")

#WAP to accept value from the user and display it

no = int(input("Enter your value here:"))
print("your value is: ", no)
         
no2 = float(input("Enter your value here:"))
print("your decimal is: ", no2)

name1 = str(input("Enter your name here:"))
print("your name is: ", name1)

name2 = input("Enter your name here:")
print("your name is: ", name2)

##WAP to accept 2 numbers from user, do all arithmetic operation and
#display output at the end. (+,-,*,/,%,**,//)

num1 = int(input("Enter your first value here:"))
num2 = int(input("Enter your second value  here:"))

sum1 = num1 + num2
sub1 = num1 - num2
mult1 = num1 * num2
div1 = num1 / num2
modu1 = num1 & num2
divinter1 = num1 // num2
power1 = num1 ** num2


print("All arithmetic outputs are \nAddition is\t\t:",sum1,"\nsubstract is\t\t:",sub1,
      "\nmuiltiplication is\t:",mult1,
      "\ndivision is\t\t:",round(div1,2),"\nmodulus is\t\t:",modu1,
      "\npower is\t\t:",power1,"\ndivision with interger  is",divinter1,)


##WAP to Calculate the Area and the circumference for a circle.
# (Area of circle = π r2 circumference of circle = 2 π r)

print("**********calculate Area & Circumference of circle*****")
r = int(input("Enter r value:"))
pi = 22/7 # pi = 3.14
area = pi*r*r
cir=2*pi*r
print('curcle area is', round(area,2),'\ncircumference of circle is',round(cir,2))











