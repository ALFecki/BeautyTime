
import uvicorn
from fastapi import FastAPI


app = FastAPI(
    root_path="/",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)


if __name__ == "__main__":
    uvicorn.run(app, loop="auto")