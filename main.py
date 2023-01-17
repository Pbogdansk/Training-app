# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from fastapi import FastAPI

app = FastAPI()

toDoList = {
    1: {
        "Excersize name": "Bent over row",
        "Number of sets": 5,
        "number of reps": 5
    }

}

# http://127.0.0 .1:8000/docs dokumentacja
@app.get("/home")  # jsonowanie sobie automatycznie robi FastApi
def trojkacik():
    return {"test"}

@app.get("/get-excersize/{excercise_id}")
def get_excersize(excercise_id: int):
    return toDoList[excercise_id]