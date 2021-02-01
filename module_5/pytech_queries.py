from pymongo import MongoClient

url = 'mongodb+srv://admin:admin@cluster0.czbkh.mongodb.net/<dbname>?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE'
client = MongoClient(url)
db = client.pytech

all_students = db.students.find({})
student_1007 = db.students.find_one({"student_id": "1007"})
student_1008 = db.students.find_one({"student_id": "1008"})
student_1009 = db.students.find_one({"student_id": "1009"})

print("-- DISPLAYING STUDENT DOCUMENT FROM find() QUERY--")
print(all_students)
print("--DISPLAYING STUDENT DOCUMENTS FROM find_one() QUERY")
print(student_1007)
print(student_1008)
print(student_1009)
