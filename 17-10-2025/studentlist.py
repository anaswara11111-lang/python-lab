student={"Name":"Anaswara","Roll no":9,"Register no":10007,"Department":"MCA","Semester":1}
print(student)
total_mark=int(input("Enter the mark:"))
student.update({"total_mark":total_mark})
mark=student["total_mark"]
if mark>=90:
    Grade='A'
elif mark>=82:
    Grade='B'
elif mark>=75:
    Grade='C'
elif mark>=60:
    Grade='D'
elif mark>=50:
    Grade='P'
else:
    Grade='F'
student.update({"grade":Grade})
print(student)
del student["Roll no"]
print(student)

