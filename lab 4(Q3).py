print("Yusra Masood , 18B-093-CS , Section A ")
print("lab 4,  9th-November-2018")
print("Question 3")

print("Program to  check if the word is palindrome or not")
word= input("Enter a word  ")
casf = word.casefold()
print(casf)
wlist=list(casf)
print(wlist)
revlist = list(reversed(casf))
if wlist == revlist :
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")

input()
