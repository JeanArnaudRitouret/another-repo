from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    string_to_return = 'Working like a charm'
    return string_to_return
