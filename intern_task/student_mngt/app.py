import json
import os

class Student:

    @staticmethod
    def load():
        with open("intern_task\\student_mngt\\stu.json", "r") as f:
            data = json.load(f)

            if not isinstance(data, list):
                return []
        return data

    @staticmethod
    def save_data(data):
        with open("intern_task\\student_mngt\\stu.json", "w") as f:
            json.dump(data, f, indent=4)

    def add_student(self):
        print('---------------for new student-----------------')
        data = Student.load()

        name = input("Enter the name: ")
        email = input("Enter the email id: ")
        course = input("Enter the enroll course: ")

        stu = {
            "name": name,
            "email": email,
            "course": course
        }

        data.append(stu)
        Student.save_data(data)

        print("Student Added Successfully!")


    def show_details(self):
        count=0
        data=Student.load()
        for i in data:
            count+=1
            print(count,'.',i)

    def update_student(self):
        print('-----------------------for update student-------------------')
        data=Student.load()
        name=input('enter the your old name 1st:')
        mail=input('enter the new mail:')
        for stu in data:
            if stu['name']==name:
                stu['email']=mail
                Student.save_data(data)
                print("Email Updated Successfully!")
        else:
            print('student does not exit')
    
    def delet_stu(self):
        print('-------------------------this is for delet student-------------------')
        data=Student.load()
        name=input('enter the name for delet:')
        for stu in data:
            if stu['name'] == name:
                data.remove(stu)
                Student.save_data(data)
                print("Deleted!")
                return
        print("User not found")


class Course:
    @staticmethod
    def load():
        with open("intern_task\\student_mngt\\course.json","r") as file:
            data=json.load(file)
            
            if not isinstance(data, list):
                return []
            return data
    @staticmethod
    def save_data(data):
        with open("intern_task\\student_mngt\\course.json","w") as file:
            json.dump(data,file,indent=4)
    
    def add_course(self):
        print('-----------------------this is for add course ----------------------')
        data=Course.load()
        title=input('enter the course title:')
        for stu in data:
            if stu['ctitle']==title:
                print('course already exist!')
                return
            
        id=input('enter the course id:')
        credit=input('enter the course credit:')
        
        cou={
            'ctitle':title,
            'cid':id,
            'credit':credit
            
            }
        data.append(cou)
        Course.save_data(data)
        print('course add done!')
        
      
    def update_course(self):
        print('------------this is for update course------------------')
        data=Course.load()
        title=input('enter the old title for update course:')
        for i in data:
            if i['ctitle']==title:
                ti=input('enter the new title:')
                id=input('enter the new id:')
                cre=input('enter the new credit:') 
                i['ctitle']=ti
                i['cid']=id 
                i['credit']=cre      
                print('title update succesfully')
                Course.save_data(data)
            else:
                print('course not found!')
    def delet_course(self):
        print('-------------------this is for delet coure------------------')
        data=Course.load()
        title=input('enter the title for remove course:')
        for i in data:
            if i['ctitle']==title:
                data.remove(i)
                Course.save_data(data)
                print('course delet done!')
        
        else:
            print('course not found ')
        
    def show_course(self):
        print('-----------show all course-----------------')
        data=Course.load()
        for i in data:
            print(i)
        
class Enrollment:

    @staticmethod
    def load():
        with open("intern_task\\student_mngt\\enroll.json", "r") as f:
            return json.load(f)

    @staticmethod
    def save_data(data):
        with open("intern_task\\student_mngt\\enroll.json", "w") as f:
            json.dump(data, f, indent=4)

    def enroll_student(self):
        data = Enrollment.load()

        name = input("Enter student name: ")
        course = input("Enter course title: ")

        enroll = {
            "student": name,
            "course": course
        }

        data.append(enroll)
        Enrollment.save_data(data)

        print("Enrollment Done!")

    def show_enroll(self):
        data = Enrollment.load()

        for i in data:
            print(i)

        

s = Student()
#s.add_student()
s.delet_stu()
#s.show_details()
#s.update_student()


c=Course()
#c.add_course()
#c.update_course()
c.delet_course()
c.show_course()

e=Enrollment()
e.enroll_student()