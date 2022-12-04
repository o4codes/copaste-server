from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Copaste Server",
    description="Serves REST API and websockets for copaste service"
)


@app.get("/")
def root():
    return JSONResponse(
        content={
            "message": "Welcome to Copaste service",
            "details": {
                "swagger_docs_url":"/docs",
                "redoc_url": "/redoc"
            }
        }
    )

@app.get("/ping")
def ping():
    return JSONResponse(
        content={
            "message": "SUCCESS"
        }
    )