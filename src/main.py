import uvicorn
from fastapi import FastAPI
from controllers import (
    product_controller,
    service_controller,
    user_controller,
    sale_controller,
    staff_controller,
    client_controller,
    supply_controller,
    schedule_controller,
    finance_controller,
    review_controller,
    auth_controller,
)
from controllers import log_controller

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
app.include_router(supply_controller.router)
app.include_router(schedule_controller.router)
app.include_router(finance_controller.router)
app.include_router(review_controller.router)
app.include_router(log_controller.router)
app.include_router(auth_controller.router)

if __name__ == "__main__":
    uvicorn.run(app, loop="auto")
