from fastapi import FastAPI, Request, Response
from fastapi.routing import APIRoute, APIRouter 
import uvicorn
import time
from fastapi.responses import HTMLResponse

# Import route services
from services import to_do

app = FastAPI(
    title= "FastAPI Tutorial",
    version = "0.0.1",
)

# Config middleware
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

# Index page
@app.get("/", response_class = HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Home</title>
        </head>
        <body>
            <h1>Fast API</h1>
            <p>Swagger: /docs</p>
        </body>
    </html>
    """

# app include router of service
app.include_router(to_do.router)

if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port = 8000)