# We will import the module of fastAPI
from fastapi import FastAPI, Body
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

@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str, year: int):
    return [item for item in movies if item ['category'] == category ]

#now I'll create the same structure but this time with the post
@app.post('/movies', tags=['movies'])
def create_movie(id: int = Body(), title: str= Body(), overview: str= Body(), year: int= Body(), rating: float= Body(), category: str= Body()):
    movie.append({
        "id":id,
        "title":title,
        "overview":overview,
        "year":year,
        "rating": rating,
        "category":category
    })
    return movie

#With 'put' method we can do modifications in my API
@app.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, title: str = Body(), overview:str = Body(), year:int = Body(), rating: float = Body(), category: str = Body()):
	for item in movie:
		if item["id"] == id:
			item['title'] = title,
			item['overview'] = overview,
			item['year'] = year,
			item['rating'] = rating,
			item['category'] = category
			return movie

@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    for item in movie:
        if item["id"] == id:
            movie.remove(item)
            return movie