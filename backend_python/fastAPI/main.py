from fastapi import FastAPI

app = FastAPI()
app.title = 'Learning FastAPI'

@app.get('/', tags=['home'])
def message():
    return 'Hello world'

