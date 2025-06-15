from fastapi import APIRouter
from backend.apis.v1 import route_signup
from backend.apis.v1 import route_boutique
from backend.apis.v1 import route_login

api_router = APIRouter()

api_router.include_router(route_signup.router, prefix = "/signup",tags= ["signup"])
api_router.include_router(route_login.router, prefix = "/login",tags= ["login"])
api_router.include_router(route_boutique.router, prefix = "/boutique",tags= ["boutique"])