# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from fastapi import FastAPI, Path
from typing import Optional
app = FastAPI()

toDoList = {
    1: {
        "Excersize name": "test",
        "Number of sets": 5,
        "number of reps": 5
    }

}

# http://127.0.0 .1:8000/docs dokumentacja
@app.get("/home")  # jsonowanie sobie automatycznie robi FastApi
def test():
    return {"test"}

@app.get("/get-excersize/{excercise_id}")
def get_excercize(excercise_id: int = Path(None, description="The id of the excersize:")):
    return toDoList[excercise_id]

@app.get("/get-by-name")
def get_excercize(name: Optional[str] = None):
    for excercize_id in toDoList:
        if toDoList[excercize_id]["name"] == name:
            return toDoList[excercize_id]
    return {"Data": "Not found"}