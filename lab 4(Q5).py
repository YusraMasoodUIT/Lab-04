print("Yusra Masood , 18B-093-CS , Section A ")
print("lab 4,  9th-November-2018")
print("Question 5")
print("Give me 2 numbers and I'll generate a table from first to last value")
fnum = eval(input("Enter your first nnumber "))
lnum = eval(input("Enter your last nnumber "))
a= fnum
while a != lnum+1 :
    for i in range(fnum , lnum+1):
        x = i * a
        print(x , end= "\t")
    print("\n")
    a = a +1
    if a == (lnum+1):
        break

print("\n")
input()
