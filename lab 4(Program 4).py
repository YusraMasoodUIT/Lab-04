print("Yusra Masood , 18B-093-CS, Section A")
print("lab 4")
print("Program 4")
print("\n")
print("Enter 2 values and I'll tell the prime numbers in b/w those numbers")
llimit = eval(input("Enter the lower limit  "))
ulimit = eval(input("Enter the upper limit  "))
print("Prime numbers between "+ str(llimit)+" and "+ str(ulimit) +" are:")
for number in range(llimit , ulimit + 1):

    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number)

input()
