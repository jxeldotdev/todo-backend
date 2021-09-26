import logging

from app.routers import health
from app.routers import todo
from app.settings import cfg
from app.settings import RequiredSettingMissingException
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI(title="Todo Rest API")

try:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=cfg.allowed_origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"],
    )
except RequiredSettingMissingException as e:
    logger.error(
        "Failed to configure CORS Middleware, required env vars not present",
    )
    logger.error(e)

app.include_router(todo.router, prefix="/todo")
app.include_router(health.router, prefix="/health")
