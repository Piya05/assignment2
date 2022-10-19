namlist=[]
markslist=[]
studentdict={}
studentno=int(input("Enter the number of student :"))
for i in range(studentno):
  nam=input(f"Enter the name of student {i+1} :")
  marks=int(input(f"Enter the marks of student {i+1} :"))
  namlist.append(nam)
  markslist.append(marks)
  studentdict[nam]=marks
print(f"Name of the student :{namlist}")
print(f"Mark of the student :{markslist}")
print(f"Detail of the student :{studentdict}")

  
