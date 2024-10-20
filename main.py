from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
  user_data = {"data": {
    "full_name": "Raonar Vokshi",
  }}
  return user_data

@app.get("/about")
def about():
  about_user = {"user_data": {
    "age": 17,
    "from": "Kosovo",
    "Currently": "In Prishtina"
  }}
  return about_user