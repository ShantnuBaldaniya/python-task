import json
import os

def show_data():
    
    with open('E:\\code\\python-task\\intern_task\\json\\stu.json','r') as file:
        data=json.load(file)
    
        if not isinstance(data,list):
            return []
        return data

def save_data(data):
    with open('stu.json','w') as file:
        json.dump(data, file, indent=4)

def add_student():
    data = show_data()

    n = input("Enter name: ")
    rl = int(input("Enter roll number: "))
    m = int(input("Enter marks: "))
    g = input("Enter grade: ")
    
    stu = {
        "name": n,
        "roll-number": rl,
        "marks": m,
        "grade": g
    }
    

    data.append(stu)
    save_data(data)
    print("Student added successfully")
   
 
def search_student():
    data = show_data()
    rl = int(input('Enter the roll-number: '))

    for stu in data:
        if stu["roll-number"] == rl:
            print('Student found:', stu)
            return

    print('Not found')


def update_marks():
    data=show_data()
    m=int(input('enter the new marks: '))
    rl=int(input('enter the roll umber for c'))
    for stu in data:
        if stu["roll-number"]==rl:
            stu["marks"]==m
            print('marks update successfully')
            save_data(data)
            return
    print('student not found!')    
    

def delet_student():
    data=show_data()
    name=input('ente the student name u want  to delet :')
    for stu in data:
        if stu["name"]==name:
            data.remove(stu)
            save_data(data)
            print('delet successfully!')
            return 
    print('student not found')
    
def display_all():
    data=show_data()
    print(data)

def calculate_average():
    data=show_data()
    total=0
    n=0
    for i in data:
        total+=i["marks"]
        n+=1
        
    print('avarege of ',total/n)
#add_student()
#earch_student()
#update_marks()
#delet_student()
display_all()
calculate_average()
