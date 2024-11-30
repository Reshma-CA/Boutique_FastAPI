from apps.v1 import route_boutique
from apps.v1 import route_signup
from apps.v1 import route_login
from apps.v1 import route_logout
from apps.v1 import route_home
from fastapi import APIRouter

app_router = APIRouter()

app_router.include_router(route_boutique.router, prefix="", tags=[""], include_in_schema=False)
app_router.include_router(route_signup.router, prefix="/auth", tags=[""], include_in_schema=False)
app_router.include_router(route_login.router, prefix="/auth", tags=[""], include_in_schema=False)
app_router.include_router(route_logout.router, prefix="/auth", tags=[""], include_in_schema=False)

app_router.include_router(route_home.router, prefix="/home", include_in_schema=False)


