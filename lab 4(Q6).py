print("Yusra Masood , 18B-093-CS , Section A ")
print("lab 4,  9th-November-2018")
print("Question 6")

print("\n")
print("Program to perforrm matrix addition" )
print("\n")
rownum = int(input("Input number of rows: "))
colnum = int(input("Input number of columns: "))
multi_list=[]
while rownum != colnum:
    print("Sorry need a square matrix")
    rownum = int(input("Please Enter again the number of rows: "))
    colnum = int(input("Please enter again the number of columns: "))
    if rownum == colnum:
        break
    
print("\n") 
print("For first matrix please enter the following")
multi_list = [[0 for col in range(colnum)] for row in range(rownum)]
for row in range(rownum):
    for col in range(colnum):
        print("Enter a value for " +str(row)+ " row and "+str(col)+ " column")
        num = eval(input())
        multi_list[row][col]=num

print("\n")
multi_list1=[]
print("For second matrix please enter the following")
multi_list1 = [[0 for col in range(colnum)] for row in range(rownum)]
for row in range(rownum):
    for col in range(colnum):
        print("Enter a value for " +str(row)+ " row and "+str(col)+ " column")
        num = eval(input())
        multi_list1[row][col]=num
print("\n\n")

print("First matrix")
for x in multi_list:
    print(x)
    
print("Second matrix")
for x in multi_list1:
        print(x)

print("\n\n")
result=[] # assigning the result matrix
result = [[0 for col in range(colnum)] for row in range(rownum)]
for row in range(rownum):
    for col in range(colnum):
        result[row][col]=0

   

for i in range(len(multi_list)):
    for j in range(len(multi_list[0])):
        result[i][j] = multi_list[i][j] + multi_list1[i][j]
print("The result of matrix addition is ")
for r in result:
    print(r)

input()











