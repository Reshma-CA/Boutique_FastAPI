from apps.v1 import route_boutique
from apps.v1 import route_signup
from fastapi import APIRouter

app_router = APIRouter()

app_router.include_router(route_boutique.router, prefix="", tags=[""], include_in_schema=False)
app_router.include_router(route_signup.router, prefix="/auth", tags=[""], include_in_schema=False)