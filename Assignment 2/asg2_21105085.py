#Question 1
print("   QUESTION 1")
g="Python is a case sensitive language"   #Assigning variabe to given string
           #Part a
print("   Part a")
print(len(g))                  #gives length of string g
           #Part b
print("   Part b")
print(g[::-1])                 #prints string in reverse
           #Part c
print("   Part c")
new_str=g[10:26]               #storing "a case sensitive" in a new variable
print(new_str)                 #printing the new string
           #Part d
print("   Part d")
g_1=g.replace("a case sensitive","object oriented")    #Replacing “a case sensitive” with “object oriented” and storing it in a new variable
print(g_1)
           #Part e
print("   Part e")
print(g.find("a"))             #finding and printing index of substring "a" in given string
           #Part f
print("   Part f")
print(g.replace(" ",""))       #printing the string remaining after removing the white spaces from the given input string.

#Question 2
print("\n\n   QUESTION 2")
SID=21105085
Name="Aditya Kansal"
Department_name="ECE"
CGPA=8.2
print("Hey, %s here!"%Name)
print("My SID is %s"%str(SID))
print("I am from %s department and my CGPA is %s ."%(Department_name,str(CGPA)))

#Question 3
print("\n\n   QUESTION 3")
a,b,=56,10
print("a =",a,"\nb =",b)
print("The result of a&b =",(a&b))
print("The result of a|b =",(a|b))
print("The result of a^b =",(a^b))
print("The result after left shift of a with 2 bits =",(a<<2))
print("The result after left shift of b with 2 bits =",(b<<2))
print("The result after right shift of a with 2 bits =",(a>>2))
print("The result after right shift of b with 4 bits =",(b>>4))

#Question 4
print("\n\n   QUESTION 4")
num_1=int(input("Enter first number : "))
num_2=int(input("Enter second number : "))
num_3=int(input("Enter third number : "))
if num_1>num_2 and num_1>num_3:
 print("First number whose value is",num_1,"is the greatest number.")
elif num_2>num_1 and num_2>num_3:
 print("Second number whose value is",num_2,"is the greatest number.")
else:
 print("Third number whose value is",num_3,"is the greatest number.")

#Question 5
print("\n\n   QUESTION 5")
input_0=input("Enter the string : ")
if "name" in input_0:
 print("Yes")
else:
 print("No")

#Question 6
print("\n\n   Question 6")
side_1=int(input("Enter length of first side : " ))
side_2=int(input("Enter length of second side : "))
side_3=int(input("Enter length of third side : "))
if side_1+side_2>side_3 and side_2+side_3>side_1:
 if side_1+side_3>side_2:
  print("Yes")
else:
 print("No") 
