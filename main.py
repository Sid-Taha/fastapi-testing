from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

names = ["Taha", "Ahmed"]

# ---------------------------------------------------------------Request Validation
# Create a Pydantic model for request body
class NameRequest(BaseModel):
    data: str

# ---------------------------------------------------------------GET
@app.get("/")
def get_data():
    return names


# ---------------------------------------------------------------POST
@app.post("/post")
def post_data(request: NameRequest):
    names.append(request.data)
    return names





# ---------------------------------------------------------------UPDATE
@app.put("/post/{index}")
def update_data(index: int, item: NameRequest):
    names[index] = item.data
    return names
    



# ---------------------------------------------------------------DELETE
@app.delete("/post/{index}")
def delete_data(index:int):
    names.pop(index)
    return names
