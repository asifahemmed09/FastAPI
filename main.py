from fastapi import FastAPI

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

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/api/posts")
def get_posts():
    return posts
