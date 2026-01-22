from router.router_transaction import router_transaction
from router.router_user import router_user
from fastapi import FastAPI 

app = FastAPI()

# Transaction Router
app.include_router(router_transaction)

# User Router
app.include_router(router_user)