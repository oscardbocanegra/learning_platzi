from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from jwt_manager import create_token, validate_token
from config.database import Session, engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router    


app = FastAPI()
app.title = 'Learning FastAPI'

app.middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)



Base.metadata.create_all(bind=engine)



class User(BaseModel):
    email: str
    password: str

    
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Movie",
                "overview": "Movie description",
                "year": 2024,
                "raiting": 9.8,
                "category": "accion"
            }
        }
    
    
    
movies = [
        {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Accion"
	},
    {
		"id": 2,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Accion"
	}
]

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world!</h1>')




