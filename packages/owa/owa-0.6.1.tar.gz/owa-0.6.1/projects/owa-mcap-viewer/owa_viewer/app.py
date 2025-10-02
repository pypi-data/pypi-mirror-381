import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from rich.logging import RichHandler

from .api import router as api_router
from .config import settings
from .services import services
from .utils import format_size_human_readable

logging.basicConfig(
    level=settings.LOG_LEVEL,
    handlers=[RichHandler(rich_tracebacks=True, show_time=False, show_level=True)],
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle application startup and shutdown"""
    logger.info("Starting OWA Viewer application")
    services.clear_cache()
    await services.start_periodic_cleanup()
    yield
    logger.info("Shutting down OWA Viewer application")
    await services.stop_periodic_cleanup()


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)
app.include_router(api_router)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def read_root(request: Request):
    """Render the index page"""
    featured_datasets = settings.FEATURED_DATASETS.copy()
    if settings.PUBLIC_HOSTING_MODE and "local" in featured_datasets:
        featured_datasets.remove("local")
    return templates.TemplateResponse("index.html", {"request": request, "featured_datasets": featured_datasets})


@app.get("/viewer")
async def read_viewer(repo_id: str, request: Request):
    """Render the viewer page for a specific dataset"""
    files = services.file_service.list_files(repo_id)
    total_size = sum(f.size for f in files) if files else 0
    size_str = format_size_human_readable(total_size)
    return templates.TemplateResponse(
        "viewer.html",
        {"request": request, "dataset_info": {"repo_id": repo_id, "files": len(files), "size": size_str}},
    )


if __name__ == "__main__":
    import uvicorn

    logger.info(f"Starting server on {settings.HOST}:{settings.PORT}")
    uvicorn.run("owa_viewer.app:app", host=settings.HOST, port=settings.PORT, reload=True)
