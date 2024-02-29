from fastapi import FastAPI
from routes.user import userRouter

app = FastAPI()

app.include_router(userRouter, prefix="/user")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=7676)