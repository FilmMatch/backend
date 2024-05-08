from fastapi import APIRouter

from User import routes as UserRoutes
from SubUser import routes as SubUserRoutes


router = APIRouter()
router.include_router(UserRoutes.router)
router.include_router(SubUserRoutes.router)
