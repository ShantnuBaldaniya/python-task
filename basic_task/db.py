# # import sqlite3 as d

# # conn=d.connect("shantnu.db")
# # cur=conn.cursor()
# # for i in range(3):
# #     name=input('enter the name:')
# #     id=input('ente the id of stu:')
# # #cur.execute("create TABLE student(id integer,name text)")
# #     cur.execute("INSERT INTO student (id , name) VALUES(? ,?) ",(id,name))
# # cur.execute("SELECT * FROM student")
# # print(cur.fetchall())
# # conn.commit()
# # conn.close()

# # print('db succ!')

# import sqlite3 as f
# conn=f.connect('data.db')
# cur=conn.cursor()
# #cur.execute('create table shantnu(name text,roll_number integer)')
# # for i in range(3):
# #     name=input('enter the student name:')
# #     roll=input('enter the student roll number:')
    
# #     cur.execute('insert into shantnu (name , roll_number) values (?,?)',(name,roll))
# #cur.execute("SELECT * FROM shantnu")
# cur.execute("DELETE FROM shantnu WHERE  name= ? ",("shantnu",))
# print(cur.fetchall())
# conn.commit()
# conn.close()


