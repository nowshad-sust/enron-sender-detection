from pymongo import MongoClient
import pprint

client = MongoClient('localhost', 27017)
db = client.enron_mail
collection = db.messages

# getting the data of all mails in the _sent_mail subfolder of each user 
mails = collection.find({"subFolder": {"$regex": "_sent_mail"}})

for mail in mails:
    sender_mail = mail["headers"]["From"]
    messsage_body = mail["body"]
    