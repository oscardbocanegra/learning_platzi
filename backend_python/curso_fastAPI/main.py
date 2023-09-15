# We will import the module of fastAPI
from fastapi import FastAPI

#Now we will create an instance of FastAPI
app = FastAPI()
#On the following code we will change the name on the /docs
app.title = "Mi aplicacion con FastAPI"

@app.get('/', tags=['Home'])
def message():
    return 'Hello world'

