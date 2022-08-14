'''
Write a function named falling_distance that accepts an object’s
falling time (in seconds) as an argument. The function should
return the distance, in meters, that the object has fallen 
during that time interval. Write a program that calls the
function in a loop that passes the values 1 through 10 as
arguments and displays the return value.

'''

def falling_distance(t):
    distance_calcul = 0.5*9.8*t*t
    return distance_calcul

for i in range(1,11):
    distance=falling_distance(i)
    print("The distance the object falls in ",i,"sec is :", distance , "meters")
