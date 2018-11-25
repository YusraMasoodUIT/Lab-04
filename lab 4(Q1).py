print("Yusra Masood , 18B-093-CS , Section A ")
print("lab 4,  9th-November-2018")
print("Home assignmnt")
print("Question 1")

print("Program to sove quadratic equation")
a = eval(input("Enter the value of a "))
b = eval(input("Enter the value of b "))
c = eval(input("Enter the value of c "))
deno = 2*a
if deno != 0 :
    root = ((b**2) - (4*a*c))**0.5
    x = ((-b+root)/deno)
    y = ((-b-root)/deno)
    print("The first root is  " + str(x))
    print("The second root is  " + str(y))
else:
    print("in-valid value , Please try again")
print("\n\n\n")
    
    
input()
