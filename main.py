from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

names = ["Taha", "Ahmed"]

# ---------------------------------------------------------------GET
@app.get("/")
def get_data():
    return names


# ---------------------------------------------------------------POST
@app.post("/post")
def post_data(data: str):
    names.append(data)
    return names





# ---------------------------------------------------------------UPDATE
@app.put("/post/{index}")
def update_data(index: int, data: str):
    names[index] = data
    return names
    



# ---------------------------------------------------------------DELETE
@app.delete("/post/{index}")
def delete_data(index:int):
    names.pop(index)
    return names