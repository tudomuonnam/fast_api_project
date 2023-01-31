from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from config import settings
from database import engine
from models import Base
from routers import users,items
from routers import login


Base.metadata.create_all(bind=engine)

tags_metadata = [
    {
        "name": "user",
        "description": "this is user router"
    },
    {
        "name": "items",
        "description": "This is product router"
    }
]

app = FastAPI(
    title= settings.PROJECT_TITLE,
   # description= "API call to finance hub",
    version=settings.PROJECT_VERSION,
    contact={
        "name": "doluong2007",
        "email": "doluong2007@gmail.com"
    },
        license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }

)
@app.get("/")
def get_root():
    return ({"message": "Hello World"})

app.include_router(users.router)
app.include_router(items.router)
app.include_router(login.router)