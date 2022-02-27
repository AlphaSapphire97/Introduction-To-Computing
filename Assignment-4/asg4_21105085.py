#QUESTION-1
print("   QUESTION-1")
def hanoi(n,source,to,aux):
    if n==0:
     return
    if n>0:
       hanoi(n-1,source,aux,to)
       print("Shift the disc",n,"from",source,"to "+to+".")
       hanoi(n-1,aux,to,source)
hanoi(3,"A","B","C")

#QUESTION-2
print("   QUESTION-2")
n=int(input("Enter no. of rows you want to print:"))
print("Using iteration ")
b=n
for i in range(1,n+1):
    for j in range(0,n+1-i):
        print(' ', end='')
    Co=1                   # first element is 1
    for j in range(1,i+1):
        print(' ',Co,sep='',end='')   # first value in a line is 1
        Co=Co*(i-j)//j                # using Binomial Coefficient to print reqired elements in each row
    print()
print("Using recursion")
def pascaltri(n):                     #creating a function to use recurction with
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        next_row = [1]
        result = pascaltri(n-1)
        last_row = result[-1]
        for i in range(len(last_row)-1):                               #making such that next list(row) have elements from sum of the required elements last list(row)
            next_row.append(last_row[i] + last_row[i+1])
        next_row += [1]
        result.append(next_row)
    return result
space=" "
c=n
for a in pascaltri(n):                #printing the required pascal triangle
    print(space*c,a)
    c-=1

#QUESTION-3
print("   QUESTION-3")
no1=int(input("ENTER DIVIDEND:"))
no2=int(input("ENTER DIVISOR:"))
list0=list(divmod(no1,no2))
print("\nPart-a")
check=callable(divmod(no1,no2))
if check==True:
    print("Function is callable.")
else:
    print("Function is not callable.")
print("\nPart-b")
if list0[0]==0 and list0[1]==0:
    print("Both quotient and remainder is zero.")
if list0[0]==0 and list0[1]!=0:
    print("Quotient is zero but remainder is non zero")
if list0[0]!=0 and list0[1]==0:
    print("Remainder is zero but quotient is non zero")
if list0[0]!=0 and list0[1]!=0:
    print("Both quotient and remainder are non zero")
print("\nPart-c")
list1=[]       #new list to store result after filtering
for i in range(4,7):
    list0.append(i)
for d in list0:
    if d<4:
        list1.append(d)
print(list1)   #printing list obtained after filtering
print("\nPart-d")
result0=set(list1)          #converting to set data type
print(result0)
print("\nPart-e")
result0=frozenset(result0)   #making set immutable
print(result0)
print("\nPart-f")
maxno=max(result0)
print("Max number from set is",maxno)
hashval=hash(maxno)
print("Hash value of",maxno,"is",hashval)

#QUESTION-4
print("   QUESTION-4")
class Student:  # creating a class Student
    def __init__(self,name,sid):  # using init function
        Student.name=name  #defining attribute name
        Student.sid=sid    #defining attribute sid
        print("object created and information stored")
    def printer(self):  # defining function to print information
        print(f"Student's name is {self.name} and SID is {self.sid}")
    def __del__(self):  #  defing destructor to delete required data
        print("Object deleted")
student1 = Student("Aditya Kansal",21105085)  # creating object
student1.printer()  # using defined function to print required data
del student1    #using this finction to delete object student1 and now we can't print it

#QUESTION-5
print("   QUESTION-5")
class Employee:       #making a class Employee
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def __del__(self):
        print(f"The record of the employee {self.name} the is deleted")
    def printname(self):
        print(f"The name of the employee is {self.name}")
    def printoldsalary(self):
        print(f"the old salary of the employee name {self.name} is {self.salary}")
employee1 = Employee("Mehak",40000)   #Creating objects
employee2 = Employee("Ashok",50000)
employee3 = Employee("Viren",60000)
employee1.printname()      #Printing names of each employee
employee2.printname()
employee3.printname()
employee1.printoldsalary()          #Printing the salary which has to be updated
employee1.salary=700000
print(f"the new salary of Mehak is {employee1.salary}")
del employee3                    #Deleting object of the required employee now we won't be able to print it

#QUESTION-6
print("   QUESTION-6")
george=input("George enter your word:")
barbie=input("Barbie enter your word:")
def anagrams(s):
 if s == "":
  return [s]
 else:
  ans = []
  for w in anagrams(s[1:]):
   for pos in range(len(w)+1):
     ans.append(w[:pos]+s[0]+w[pos:])
  return ans
anagrams(george)
if barbie in anagrams(george):
 print("Your friendship is true")
else:
  print("Your friendship is fake")
