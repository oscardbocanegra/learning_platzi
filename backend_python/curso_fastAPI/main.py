# We will import the module of fastAPI
from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional

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
app.version = "0.0.1"

class Movie(BaseModel):
    id: Optional[int] = None
    title: str
    overview: str
    year: int
    rating: float
    category: str
    

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

@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str, year: int):
    return [item for item in movies if item ['category'] == category ]

#now I'll create the same structure but this time with the post
@app.post('/movies', tags=['movies'])
def create_movie(movie:Movie):
    movie.append(movie)
    return movie

#With 'put' method we can do modifications in my API
@app.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, movie: Movie):
	for item in movie:
		if item["id"] == id:
			item['title'] = movie.title
			item['overview'] = movie.overview
			item['year'] = movie.year
			item['rating'] = movie.rating
			item['category'] = movie.category
			return movie

@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    for item in movie:
        if item["id"] == id:
            movie.remove(item)
            return movie