#code for Palindrome number
num=int(input("Enter any number: "))
temp=num
reverse=0
while(num>0):
  digit=num%10
  reverse=reverse*10+digit
  num=num//10
if(temp==reverse):
  print("The entered number is Palindrome")
else:
  print("Entered number is not Palindrome")

#Code to print Multiplication table
n= int(input("enter a number"))
for i in range(1,11):
  print(n,"x",i,"=",n*i)


