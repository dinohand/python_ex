from fastapi import FastAPI
## pip install uvicorn


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}