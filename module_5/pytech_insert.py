from pymongo import MongoClient

url = 'mongodb+srv://admin:admin@cluster0.czbkh.mongodb.net/<dbname>?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE'
client = MongoClient(url)
db = client.pytech

Bob = {
    "student_id":"1007",
    "first_name":"Bob",
    "last_name":"Smith"
}

bob_student_id = db.students.insert_one(Bob).inserted_id
print("Inserted Student Record", bob_student_id)

Joe = {
    "student_id":"1008",
    "first_name":"Joe",
    "last_name":"Jones"
}

joe_student_id = db.students.insert_one(Joe).inserted_id
print("Inserted Student Record", joe_student_id)

Sam = {
    "student_id":"1009",
    "first_name":"Sam",
    "last_name":"Jackson"
}

sam_student_id = db.students.insert_one(Sam).inserted_id
print("Inserted Student Record", sam_student_id)
