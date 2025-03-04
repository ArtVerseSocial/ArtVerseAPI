from fastapi import APIRouter

ArtRouter = APIRouter() # Création d'une classe de router pour créer un groupe de routes

@ArtRouter.get("/get")
async def getArt():
    return {"message": "getArt"}

@ArtRouter.post("/post")
async def postArt():
    return {"message": "postArt"}

@ArtRouter.put("/update")
async def updateArt():
    return {"message": "updateArt"}

@ArtRouter.delete("/delete")
async def deleteArt():
    return {"message": "deleteArt"}