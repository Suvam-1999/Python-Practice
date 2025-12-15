# 1. Student Grade Manager

# Create a Student class with name, marks attributes.

# Add a method to calculate grade (A, B, C, F) based on marks.

# Use a loop to input multiple students.

# Use if statements to assign grades.

# Print all students and their grades.


class Students:
    def __init__(self, name = "", marks = 0):
        self.name = name
        self.marks = marks

    def main(self):
        self.name = input("Enter name : \n")
        self.marks = int(input("Enter marks : "))
        if self.marks > 100 :
            print ("Invalid number")
        else :
            grade = self.calculate()
            print (f"Your total grade is {grade} , {self.name}")
            

    def calculate(self):
        if self.marks >= 90 :
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        else:
            return "F"


students = Students()
students.main()
