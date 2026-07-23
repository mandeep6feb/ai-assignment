name=[]
roll_no=[]  
branch=[]
age=[]
n=5
 
for i in range(n):
  print(f"enter the sutudent details{i+1}")
  student_age=int(input("enter the age abovce 18:"))
  if student_age<18:
     print("only enter the 18 above or equal age!")
     continue
    
name.append(input("enter name:"))
roll_no.append(input("enter the roll_no"))
branch.append(input("enter the branch:" ))
age.append(student_age)

print("\n----------- student information--------")
print(format("name\troll_no\tbranch\tAge"))
print("\n-------------------")

for i in range(len(name)):
  print (name[i],
   roll_no[i],
   branch[i],
   age[i])
