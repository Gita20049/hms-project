from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hospital Management System Running"}

@app.get("/patients")
def patients():
    return {"patients": ["Ram", "Shyam", "Gita"]}