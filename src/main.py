import uvicorn
from fastapi import FastAPI
from controllers import (
    product_controller,
    service_controller,
    user_controller,
    sale_controller,
    staff_controller,
    client_controller,
)

app = FastAPI(
    root_path="/",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)

app.include_router(user_controller.router)
app.include_router(client_controller.router)
app.include_router(staff_controller.router)
app.include_router(product_controller.router)
app.include_router(service_controller.router)
app.include_router(sale_controller.router)

if __name__ == "__main__":
    uvicorn.run(app, loop="auto")
