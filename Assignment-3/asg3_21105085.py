#QUESTION-1 
print("   QUESTION-1")
str0=input("Enter a string:")
str1 = str0.lower()    #CONVERTING INPUT STRING TO LOWERCASE AS PYTHON IS A CASE SENSITIVE LANGUAGE 
if " " in str0:        #CHECKING IF OUR INPUT STRING HAS MULTIPLE WORDS OR A SINGLE WORD
 str_0 = str1.split()  #THIS FUNCTION CREATES A LIST OF ALL WORDS IN OUR INPUT STRING
 dict_0= dict()
 for word in str_0:    #COUNTING DIFFERENT WORDS IN INPUT STRING
    if word not in dict_0:
     dict_0[word]=1     
    else : 
     dict_0[word]+=1 
 for key in dict_0.keys():
     print("The word",key,"has come",dict_0[key],"time(s).")
else :                 #IF OUR STRING HAS ONLY ONE WORD THEN THIS PART OF THE CODE WILL RUN
 str_1=list(str1)      #THIS FUNCTION CREATES A LIST OF ALL CHARACTERS IN OUR INPUT STRING 
 dict_1=dict()                                
 for ch in str_1:      #COUNTING DIFFERENT CHARACTERS IN INPUT STRING 
    if ch not in dict_1:  
        dict_1[ch]=1             
    else: 
        dict_1[ch]+=1 
 for key in dict_1.keys():
     print("The character",key,"has come",dict_1[key],"time(s).")

#QUESTION-2
print("   QUESTION-2")
year=int(input("Enter year:"))                         #Taking input
month=int(input("Enter month:"))
date=int(input("Enter date:"))
month_1=month
cond0=True
if 1800<=year<=2025 and 1<=month<=12 and 1<=date<=31:
   print("Entered date is: "+str(date)+'/'+str(month)+'/'+str(year))
   if year%4==0 and year%100!=0:                       #Checking if entered year is leap year
    leap=True
   elif year%400==0:
    leap=True
   else:
    leap=False
   if month==2 and 0<date<29 and leap==True:           #Finding next date if entered month is 2(Feb)
    date_1=date + 1
   if month==2 and 0<date<28 and leap==False:
    date_1 =date + 1
   if month==2:
       if date==28 and leap==False or date==29 and leap==True:
        date_1=1
        month_1=3
   if month==2:
       if date>28 and leap==False or date>29 and leap==True :
         print("Enter a valid value.")
         cond0=False
   mon_31=[1,3,5,7,8,10,12]                         #List of all months with 31 days
   mon_30=[4,6,9,11]                                #List of all months with 30 days
   if month in mon_31:                              #Finding next date if entered month has 31 days
    if 0<date<31:
      date_1=date+1
    elif date==31 and month==12:
       date_1=1
       month_1=1
       year+=1
    elif date==31 and month!=12:
        date_1=1
        month_1=month+1
   if month in mon_30:                              #Finding next date if entered month has 30 days
    if 0<date<30:
        date_1 = date + 1
    elif date==30:
        date_1=1
        month_1=month+1
    elif date>30:
        cond0=False
        print("Enter valid values.")
else:                                              #If input is not lying in required range then this condition activates
    cond0=False
    print("Enter valid values.")
if cond0==True:
      print("Next Date is: "+str(date_1)+'/'+str(month_1)+'/'+str(year))     #Printing next date if all parameters are satisfied

#QUESTION-3
print("   QUESTION-3")                                            
list0=[]                                          #LIST WHICH STORES INPUT FROM USER
list=[]                                           #LIST WHICH STORES THE NUMBERS WITH THEIR SQUARES
a=int(input("Enter a number:"))                   #TAKING FIRST INPUT
list.append((a,a*a))
list0.append(a)
choice=True
while choice==True:                               #LOOP TO TAKE INPUT REPEATEDLY UNTIL USER IS SATISFIED
    ask=input("Do you want to enter another number?(Enter Y for Yes) ")
    if ask=="Y":
        a = int(input("Enter another number:"))
        list.append((a,a*a))
        list0.append(a)
    else:
        break
print("List(numbers without their square):",list0)          #PRINTING LISTS
print("List(numbers with their square) :",list)



#QUESTION-4
print("   QUESTION-4")
grade=int(input("Enter your grade : "))
i=grade                     #replacing grade with i so i don't have to write grade again and again
if i==4:
    l_grade="D"            #l_grade represents Letter Grade
    perf="Poor"            #perf represents performance
elif i==5:
    l_grade="C"
    perf="Below Average"
elif i==6:
    l_grade="C+"
    perf="Average"
elif i==7:
    l_grade="B"
    perf="Good"
elif i==8 :
    l_grade = "B+"
    perf = "Very Good"
elif i==9:
    l_grade="A"
    perf="Excellent"
else:
    l_grade="A+"
    perf="Outstanding"
if i<4:
    print("Improve your performance.")
elif i>10:
    print("Enter valid value.")
else:
    print("Your Grade is ‘%s’ and %s Performance." %(l_grade,perf))     #printing the required output


#QUESTION-5
print("   QUESTION-5")
a="ABCDEFGHIJK"               
i=0
b=" "
j=0
while True:                 #LOOP WHICH PRINTS REQUIRED OUTPUT
 print( b*j + a[0:11-i] )   #ADDING SPACING AND SLICING STRING a TO GET REQUIRED OUTPUT IN EACH LINE
 i=i+2
 j+=1
 if i>10:
     break

#QUESTION-6
print("   QUESTION-6")
Record=dict()              #MAKING THE DICTIONARY NAMED Record TO STORE SIDs AND NAMEs
choice="Y"
while choice=="Y":         #LOOP WHICH TAKES INPUT UNTIL USER IS SATISFIED
 SID=int(input("Enter SID(should be unique):"))
 Name=input("Enter name:")
 Record[SID]=Name
 choice=input("Enter Y if you want to enter more data else neter N:")

print("Part-a")
for key in Record.keys():         
 print("SID:",key," Name:",Record[key])

print("Part-b")
print("After sorting based on student names")
def get_key(val):                               #DEFINING A FUNCTION TO GET KEY FROM VALUE IN DICTIONARY Record
    for key, value in Record.items():
         if val == value:
             return key
for value in sorted(Record.values()):
    print("Name:",value," SID:",get_key(value)) #PRINTING AFTER SORTING BASED ON NAMES 

print("Part-c")
print("After sorting based on SID")
for key in sorted(Record):
    print("SID:",key," Name:",Record[key])      #PRINTING AFTER SORTING BASED ON SIDS

print("Part-d")
req_SID=int(input("Enter the SID of student whose name you want:"))
for k in Record.keys():                         #FINDING THE NAME OF STUDENT CONNECTED WITH REQUIRED SID
    if k==req_SID:
     print("The name of student with SID",k,"is",Record[k])

#QUESTION-7
print("   QUESTION-7")
n=int(input("Enter n: "))
if n>2:                   #FOR THE CASES IF n>2
 i=0                      #ASSIGNING INITIAL TERM
 j=1                      #ASSIGNING SECOND TERM
 k=i+j                    #ASSIGNING THIRD TERM
 a=2
 sum_1=1                  #ASSIGNING SUM UNTIL SECOND TERM
 print('Term 1 is:',i)
 print('Term 2 is:',j)
 while a<n :              #THE LOOP WHICH EVALUATES TERMS AFTER THIRD TERM
    sum_1+=k
    i=j                   
    j=k
    print('Term',int(a+1),'is:',k)
    k=i+j
    a+=1
if n==1:                #FOR THE CASE n=1       
  i=0
  sum_1=0
  print('Term 1 is:',i)
if n==2:                #FOR THE CASE n=2
  i=0
  j=1
  sum_1=1
  print('Term 1 is:',i)
  print('Term 2 is:',j)
average=sum_1/n
print("Average =",average)        #PRINTING AVERAGE

#QUESTION-8
print("   QUESTION-8")
Set1= {1, 2, 3, 4, 5}         #INPUTING THE SETS GIVEN IN QUESTION
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}
print("Set1=",Set1)
print("Set2=",Set2)
print("Set3=",Set3)

print("Part a")
print("Set of all elements that are in Set1 and Set2 but not both:",Set1^Set2)

print("Part b")
print("Set of all elements that are in only one of the three sets Set1, Set2 and Set3:",Set1^Set2^Set3)

print("Part c")
Set12=(Set1&Set2-Set3)    #Set with elements that are exactly in Set1,Set2 and not in Set3
Set23=(Set2&Set3-Set1)    #Set with elements that are exactly in Set2,Set3 and not in Set1
Set13=(Set1&Set3-Set2)    #Set with elements that are exactly in Set1,Set3 and not in Set2
print("Set of elements that are exactly two of the sets Set1, Set2 and Set3:",Set12|Set23|Set13)   #PRINTING THE SET WHICH IS UNION OF Set12,Set23 and Set13

print("Part d")
Set10={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}     #Set with all integers in range 1 to 10
print("Set of all integers in the range 1 to 10 that are not in Set1:",Set10-Set1)

print("Part e")
print("Set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3:",Set10-(Set1|Set2|Set3))
    
