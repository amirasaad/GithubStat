from typing import List
from src.schema import Langauge
"""
src.app Contains main APIs
"""
from fastapi import FastAPI

from .github import Github
from .schema import Langauge

app = FastAPI()


@app.get("/languages/", response_model=List[Langauge])
async def languages():
    """
    List the languages used by the 100 trending public repos on GitHub
    """
    return await Github.get_languages()

