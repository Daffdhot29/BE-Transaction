from router.router_transaction import router_transaction
from router.router_user import router_user
from fastapi import FastAPI 

app = FastAPI()

app.include_router(router_transaction)
app.include_router(router_user)