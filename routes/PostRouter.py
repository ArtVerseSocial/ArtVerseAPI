from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.ConfigDatabase import SessionLocal
from models.PostModel import Post

PostRouter = APIRouter() # Création d'une classe de router pour créer un groupe de routes

@PostRouter.get("/get")
async def getArt(db: Session = Depends(SessionLocal)):
    posts = db.query(Post).all()
    return posts

@PostRouter.post("/create")
async def postArt():
    return {"message": "postArt"}

@PostRouter.put("/update")
async def updateArt():
    return {"message": "updateArt"}

@PostRouter.delete("/delete")
async def deleteArt():
    return {"message": "deleteArt"}