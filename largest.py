#Niki
#Largest
#Write a function with 3 integer parameters (a,b,c) that returns the largest of the three numbers
#Functions
def largest(a,b,c):
    if a > b:
        print(a)
    elif c > b:
        print(c)
    elif b > a:
        print(b)
    elif c > a:
        print (c)
    elif a > c:
        print(a)
    elif b > c:
        print(b)
#Main
largest(5,7,9)
