from fastapi import APIRouter

from Objects.SessionToken import router as SessionTokenRoutes
from Objects.Catalog import router as CatalogRoutes
from Objects.Item import router as ItemRoutes
from Objects.Reserve import router as ReserveRoutes

router = APIRouter()

router.include_router(SessionTokenRoutes.router)
router.include_router(CatalogRoutes.router)
router.include_router(ItemRoutes.router)
router.include_router(ReserveRoutes.router)

