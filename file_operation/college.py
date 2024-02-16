f1=open("C:\\Users\\DHANUJA\\Desktop\\python_works\\file_operation\\allstudent.txt")
f2=open("C:\\Users\\DHANUJA\\Desktop\\python_works\\file_operation\\failed.txt")

all_student={line.rstrip("\n") for line in f1}
failed_students={line.rstrip("\n") for line in f2}

passed_student=all_student.difference(failed_students)
print(passed_student)