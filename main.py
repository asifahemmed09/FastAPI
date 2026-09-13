from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

posts = [
    {
        "id": 1,
        "title": "Introduction to Python",
        "content": "Python is a beginner-friendly programming language.",
        "author": "Asif",
        "published": True
    },
    {
        "id": 2,
        "title": "Learning FastAPI",
        "content": "FastAPI is a modern and fast web framework for Python.",
        "author": "Rahim",
        "published": True
    },
    {
        "id": 3,
        "title": "Understanding Dictionaries",
        "content": "Dictionaries store data in key-value pairs.",
        "author": "Karim",
        "published": False
    },
    {
        "id": 4,
        "title": "Python Lists Explained",
        "content": "Lists are ordered and mutable collections in Python.",
        "author": "Nadia",
        "published": True
    },
    {
        "id": 5,
        "title": "Building REST APIs",
        "content": "REST APIs allow different applications to communicate with each other.",
        "author": "Sakib",
        "published": True
    }
]

@app.get("/",response_class=HTMLResponse,include_in_schema=False)
@app.get("/posts",response_class=HTMLResponse,include_in_schema=False)
def home():
    return "<h1>FastAPI</h1>"

@app.get("/api/posts")
def get_posts():
    return posts
