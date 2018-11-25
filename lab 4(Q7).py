print("Yusra Masood , 18B-093-CS , Section A ")
print("lab 4,  9th-November-2018")
print("Question 7")

x = [[3,7], [2 ,5]] #first matrix
y = [[9,4], [6,3]] #second matrix

result = [[0,0], [0,0]] 

  #multiplication of matrix
for i in range(len(x)):
   for j in range(len(y[0])):
       for k in range(len(y)):
           result[i][j] = x[i][k] * y[k][j]
print("The result of matrix multiplication is ")
for r in result: 
	print(r) # print the result

input()








































