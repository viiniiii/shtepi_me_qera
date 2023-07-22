import copy
class Student:
    all = []
    def __init__(self, emri:str, mbiemri:str, dega:str, viti_i_diplomimit:int, mesatarja:float):
        self.emri = emri
        self.mbiemri = mbiemri
        self.dega = dega
        self.viti_i_diplomimit = viti_i_diplomimit
        self.mesatarja = mesatarja
        Student.all.append(self)
    
    @staticmethod
    def master(studentet):
        for student in studentet:
             if student.mesatarja > 8.5:
                 yield student
    @staticmethod
    def sort_by_name(studentet):
        while len(studentet) > 0:
            for i in range(0,len(studentet)):
                min = studentet[0].emri
                index = 0
                if (studentet[i].emri < min):
                    min = studentet[i].emri
                    index = i
            yield studentet[index]
            studentet.remove(studentet[index])


student1 = Student("Edvin","Perfundi","Informatike_ekonomike",2025,8.8)
student2 = Student("Rexhina","Mokreri","Fizioterapi",2025,6.1)
student3 = Student("Kjara","Hysko","Informatike_ekonomike",2025,8.1) 
student4 = Student("Kostika","Tome","Informatike_ekonomike",2025,9.1)
student5 = Student("Erda","Gjura","Informatike_ekonomike",2025,8.7)
for student in Student.all:
    print(student.emri,student.mbiemri,student.dega,student.viti_i_diplomimit,student.mesatarja)
Student.all = list(Student.sort_by_name(Student.all))
print("----------------------------------------------")
for student in Student.all:
    print(student.emri,student.mbiemri,student.dega,student.viti_i_diplomimit,student.mesatarja)
print("----------------------------------------------")
studentet_master = copy.deepcopy(Student.all)
studentet_master = list(Student.master(studentet_master))
for student in studentet_master:
    print(student.emri,student.mbiemri,student.dega,student.viti_i_diplomimit,student.mesatarja)

print(len(studentet_master))
print("----------------------------------------------")
studentet_master = list(Student.sort_by_name(studentet_master))
print(len(studentet_master))
for student in studentet_master:
    print(student.emri,student.mbiemri,student.dega,student.viti_i_diplomimit,student.mesatarja)
