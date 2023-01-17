# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from fastapi import FastAPI

app = FastAPI()
#http://127.0.0.1:8000/docs dokumentacja
@app.get("/home")
def trojkacik():
    return {"dupa"}