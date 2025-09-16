from fastapi import FastAPI

app = FastAPI()

@app.get("/message/")
def get_messege():
    return {"messege":"Hello world"}

@app.post("/create_product")
def create():
    return {"message":"продукт создан"}
