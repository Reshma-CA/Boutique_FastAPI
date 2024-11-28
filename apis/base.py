from fastapi import APIRouter
from apis.v1 import route_signup
from apis.v1 import route_boutique

api_router = APIRouter()

api_router.include_router(route_signup.router, prefix = "/users",tags= ["users"])
api_router.include_router(route_boutique.router, prefix = "/boutique",tags= ["boutique"])