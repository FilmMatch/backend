from fastapi import APIRouter

from User import routes as UserRoutes


router = APIRouter()
router.include_router(UserRoutes.router)
