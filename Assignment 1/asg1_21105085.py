#Assignment-1
#Qusetion-1
print("   Program-1")
a=int(input("please enter 1st number: "))
b=int(input("please enter 2nd number: "))
c=int(input("please enter 3rd number: "))
print('The average of three numbers enter by you is ',(a+b+c)/3)

#Question-2
print("   Program-2")
gross_inc=float(input("Enter your Gross Income : "))
gross_inc=round(gross_inc,2)
dependents=int(input("Enter number of dependents: "))
standard_deduction=10000
dependent_deduction=3000
Tax_rate=0.2
Taxable_inc=gross_inc-standard_deduction-(dependent_deduction*dependents)
Tax=Taxable_inc*Tax_rate
print("Your Tax is ",Tax,"$")

#Question-3
print("   Program-3")
#Student=[SID,Name,Gender,Department Name,CGPA]
print("SID,Name,Gender,Departmant name,CGPA")
Student=[21105085,"Aditya","M","ECE",7.4]
print(Student)

#Qusetion-4
print("   Program-4")
Marks=[47,82,67,83,59]
print("Before Sorting ",Marks)
Marks.sort()
print("After Sorting ",Marks)

#Question-5(Part-a)
print("   Program-5(Part-a)")
color=['Red','Green','White','Black','Pink','Yellow']
color.pop(3)
print(color)

#Question-5(Part-b)
print("   Program-5(Part-b)")
color=['Red','Green','White','Black','Pink','Yellow']
color[3:5]=['Purple']
print(color)



