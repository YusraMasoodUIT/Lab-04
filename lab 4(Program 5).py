print("Yusra Masood , 18B-093-CS, Section A")
print("lab 4")
print("Program 5")

print("\n")
print("Enter 2 numbers and I'll tell the sum of all the numbers in between")
ivalue = eval(input("Enter the first value "))
fvalue = eval(input("Enter the last value "))
num = range(ivalue , fvalue)
print(num)
sum = 0
for value in num:
    sum = sum + value
    
print("The total sum is", sum)

input()
