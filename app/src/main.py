"""src.app Contains main APIs."""
from typing import List

from fastapi import FastAPI

from .github import Github
from .schema import Language
from .settings import settings

app = FastAPI(title=settings().app_name)


@app.get("/languages/", response_model=List[Language])
async def languages():
    """
    List the languages used by the 100 trending public repos on GitHub
    """
    return Github(settings().GITHUB_BASE_URL).get_languages()
