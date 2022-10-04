import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from router import product

app = FastAPI(
    title="Shopping Cart API",
    description="This API was developed for teaching Fast API",
    version="0.1.0",
    docs_url='/api/docs',
    redoc_url='/api/redoc',
    openapi_url='/api/openapi.json'
)

app.include_router(product.router)


@app.get("/")
def root():
    return {"title": 'HELLO'}


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)

origins = [
    'http://127.0.0.1:3000',
    'http://localhost:3000',
    'http://127.0.0.1:5173',
    'http://localhost:5173',
    'https://fastapi4railway2022-production.up.railway.app'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*']
)