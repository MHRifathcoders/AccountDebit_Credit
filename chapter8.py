# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.
# class Student:
#     def __init__(self, name, marks_of_sub1, marks_of_sub2, marks_of_sub3):
#         self.name= name
#         self.marks1= marks_of_sub1
#         self.marks2= marks_of_sub2
#         self.marks3= marks_of_sub3

#         # def get_name(self):
#         #     self.name
# student_name_input= input("Enter your name: ")
# student_rec= Student(student_name_input, 80, 90, 70)
# # print(student_rec.name)
# # print(student_rec.marks1)
# # print(student_rec.marks2)
# # print(student_rec.marks3)
# print(f"Student Name: {student_rec.name}, Subject 1 marks: {student_rec.marks1}, Subject 2 marks: {student_rec.marks2} and Subject 3 marks: {student_rec.marks3}")

class Student:
    def __init__(self, name, marks):
        self.name= name
        self.marks= marks

    def get_avg(self):
        total= sum(self.marks)
        avg= total/len(self.marks)
        return avg
        # print(f"Student name is {self.name} and Average scores are {avg} which is based on 3 Subjects mark and they are {self.marks}")
student_name= input("Enter Your Name: ")
student_marks_input= input("Enter marks separated by spaces (e.g., 80 90 70): ")
marks= list(map(int, student_marks_input.split()))
student_rec= Student(student_name, marks)
# student_rec.get_avg()
print(f"Student name is {student_rec.name} and Average scores are {student_rec.get_avg()} which is based on {len(student_rec.marks)} Subjects and marks are {student_rec.marks}")