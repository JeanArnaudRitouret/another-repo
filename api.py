from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    string_to_return = 'Working'
    return string_to_return
