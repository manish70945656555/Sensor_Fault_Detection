import os


AWS_S3_BUCKET_NAME = "wafer-fault"
MONGO_DATABASE_NAME = "WaferFault"
MONGO_COLLECTION_NAME = "WaferFaultDetection"

TARGET_COLUMN = "quality"
MONGO_DB_URL = "mongodb+srv://manishkumawat0803:manishkumawat08034@cluster0.necirxl.mongodb.net/?retryWrites=true&w=majority"

MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder =  "artifacts"