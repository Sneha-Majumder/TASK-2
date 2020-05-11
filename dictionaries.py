Student = {"Name": "Sneha", "Age": 22, "Year of study": 4, "Branch":"Biotechnology"}
print(type(Student))
print("printing Student data")
print(Student)
print("Deleting some of the student's data")
del Student["Name"]
del Student["Branch"]
print("printing the modified information")
print(Student)
print("Deleting the dictionary:Student");
del Student
print("Lets try to print it again");
print(Student)
