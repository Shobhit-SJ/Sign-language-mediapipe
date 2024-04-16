from pymongo import MongoClient

# Replace with your cloud database connection details (same as Raspberry Pi script)
DATABASE_URL = "ongodb+srv://SLRS-login:<SLRS@MSRIT@123>@cluster2.yjeqc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster2"
DATABASE_NAME = "SLRS1"
COLLECTION_NAME = "sensor_data"

# Connect to MongoDB
# Function to connect to MongoDB
def connect_to_db():
    client =MongoClient(DATABASE_URL)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    return collection

# Function to insert sensor data
def insert_sensor_data(timestamp, flex1, flex2, flex3, flex4, flex5, acc_x, acc_y, acc_z, gyro_x, gyro_y, gyro_z):
    collection = connect_to_db()
    data = {
        "timestamp": timestamp,
        "flex": {
            "flex1": flex1,
            "flex2": flex2,
            "flex3": flex3,
            "flex4": flex4,
            "flex5": flex5
        },
        "acceleration": {
            "x": acc_x,
            "y": acc_y,
            "z": acc_z
        },
        "gyroscope": {
            "x": gyro_x,
            "y": gyro_y,
            "z": gyro_z
        }
    }
    collection.insert_One(data)
    print("Data inserted successfully!")