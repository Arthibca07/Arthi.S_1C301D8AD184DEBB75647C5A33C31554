#sort_students that takes a list of student objects as input and sorts the list based on their CGPA 


class Student:

  def __init__(self,name,roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  #sort he list of student in descending order of cgpa
  sorted_students = sorted(student_list,
      key = lambda student:student.cgpa,
      reverse = True)
  return sorted_students


students = [Student("Deepika","bca09",8.9),
            Student("Keerthana","bca08",8.2),
            Student("Arthi","bca07",9.4),
            Student("Serina","bca10",8.6)]

sorted_students = sort_students(students)
#print the sorted list of students
for student in sorted_students:
  print("Name : {} , Roll Number :  {} , CGPA : {}".format(student.name,
                                                student.roll_number,
                                                student.cgpa))