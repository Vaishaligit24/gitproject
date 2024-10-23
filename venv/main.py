from fastapi import FastAPI # type: ignore
from pydantic import BaseModel # type: ignore
from typing import List
 
app = FastAPI()
 
@app.get("/")
def read_root():
    return {"Hello": "World"}
 
@app.get("/reverse/{item}")
def reverse_string(item: str):
    return item[::-1]
