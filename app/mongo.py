from pymongo import MongoClient

client = MongoClient("mongodb+srv://vpvnspranay:vpvnspranay@cluster0.pietx.mongodb.net/?appName=Cluster0")

db = client["event_platform"]
event_logs = db["event_logs"]
user_activity = db["user_activity"]
feedback = db["feedback"]