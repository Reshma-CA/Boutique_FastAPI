# backend/apps/base.py
from backend.apps.v1 import route_boutique, route_signup, route_login, route_logout, route_home
from fastapi import APIRouter

app_router = APIRouter()

app_router.include_router(route_boutique.router, prefix="", tags=[""], include_in_schema=True
)
app_router.include_router(route_signup.router, prefix="/auth", tags=[""], include_in_schema=True
)
app_router.include_router(route_login.router, prefix="/auth", tags=[""], include_in_schema=True
)
app_router.include_router(route_logout.router, prefix="/auth", tags=[""], include_in_schema=True
)
app_router.include_router(route_home.router, prefix="/home", include_in_schema=True
)
