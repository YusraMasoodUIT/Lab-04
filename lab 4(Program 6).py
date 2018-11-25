print("Yusra Masood , 18B-093-CS, Section A")
print("lab 4")
print("Program 6")

print("Creating a multi dimensional list")
rnum = eval(input("Enter the number of rows: "))
cnum = eval(input("Enter the number of columns: "))
multilist = [[0 for col in range(cnum)] for row in range(rnum)]
for row in range(rnum):
    for col in range(cnum):
        multilist[row][col]= row*col
        
print(multilist)

input()
