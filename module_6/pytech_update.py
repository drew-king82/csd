from pymongo import MongoClient

#Set url path for mongo
url = 'mongodb+srv://admin:admin@cluster0.czbkh.mongodb.net/<dbname>?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE'
#Connect to Mongo
client = MongoClient(url)
#Set database
db = client.pytech
#Set document
students_list = db.students

#Get student data from student document
all_students = students_list.find({})

#Following three lines not needed for this assignment
student_1007 = db.students.find_one({"student_id": "1007"})
student_1008 = db.students.find_one({"student_id": "1008"})
student_1009 = db.students.find_one({"student_id": "1009"})



#loop through students, and print data 
for student in all_students:
    #set variable student id
    student_id = student['student_id']
    #Set variable first_name
    first_name = student['first_name']   
    #set variable last_name
    last_name = student ['last_name']

    #Print Information
    print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
    print("Student ID: ", student_id)
    print("First Name: ", first_name)
    print("Last Name: ", last_name)


#update_one student_id

result = students_list.update_one({"student_id" : "1007"}, {"$set": {"last_name": "Samuels"}})

#Call find_one method, and output to terminal window
print("-- DISPLAYING STUDENTS DOCUMENTS 1007 --")
student_1007 = db.students.find_one({"student_id": "1007"})
student_1007_id = student_1007['student_id']
student_1007_first_name = student_1007['first_name']
student_1007_last_name = student_1007['last_name']


print("Student ID: ", student_1007_id)
print("First Name: ", student_1007_first_name)
print("Last Name: ", student_1007_last_name)
