from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    string_to_return = 'Working like a clockwork'
    return string_to_return
