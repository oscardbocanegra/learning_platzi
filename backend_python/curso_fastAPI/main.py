# We will import the module of fastAPI
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

#Now i'll create a varible that will contain a list of a movies in where each 
#dictionary is going to have their own description 
movie = [
    {
        "id": 1,
        "title": "Avatar",
        "overview":'Avatar derives from a Sanskrit word meaning "descent," and when it first appeared in English in the late 18th century, it referred to the descent of a deity to the earth—typically, the incarnation in earthly form of Vishnu or another Hindu deity.',
        "year": "2009",
        "rating": 7.4,
        "category": "Action"
    
    },
    {
        "id": 2,
        "title": "Avatar",
        "overview":'Avatar derives from a Sanskrit word meaning "descent," and when it first appeared in English in the late 18th century, it referred to the descent of a deity to the earth—typically, the incarnation in earthly form of Vishnu or another Hindu deity.',
        "year": "2009",
        "rating": 7.4,
        "category": "Action"
    
    }
]


#Now we will create an instance of FastAPI
app = FastAPI()
#On the following code we will change the name on the /docs
app.title = "Mi aplicacion con FastAPI"

@app.get('/', tags=['Home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')

@app.get('/movies', tags=['movies'])
def movies():
    return movie

#So now I'll create another path but this time we are going to specificate 
#that this will have a parameter, and i can do this with the "{}"
@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int):
    for item in movie:
        if item ["id"] == id:
            return item
    return []

@app.get('/prueba')
def prueba():
    return 'prueba'