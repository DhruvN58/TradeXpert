from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from users import router as user_router  # Import user routes if using APIRouter
from trades import router as trade_router  # Import trade routes if using APIRouter
import websocket

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React app URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(trade_router)
@app.get("/")
def home():
    return {"message": "API is working!"}
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(trade_router, prefix="/trades", tags=["Trades"])
app.include_router(websocket.router, prefix="/ws", tags=["WebSockets"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
# from fastapi import FastAPI
# from users import router as user_router  # Import user routes if using APIRoute
# from trades import router as trade_router  # Import trade routes if using APIRouter
# import websocket

# app = FastAPI()
# app.include_router(user_router)
# app.include_router(trade_router)
# @app.get("/")
# def home():
#     return {"message": "API is working!"}
# app.include_router(user_router, prefix="/users", tags=["Users"])
# app.include_router(trade_router, prefix="/trades", tags=["Trades"])
# app.include_router(websocket.router, prefix="/ws", tags=["WebSockets"])

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
