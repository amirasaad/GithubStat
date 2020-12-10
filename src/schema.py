from typing import List, Union

from pydantic import BaseModel, HttpUrl


class Langauge(BaseModel):
    name: Union[str, None]
    number_of_repos: int
    repos: List[HttpUrl]

    class Config:
        schema_extra = {
            "example": {
                "name": "Python",
                "number_of_repos": 2,
                "repos": [
                    "https://github.com/amirasaad/pastebin",
                    "https://github.com/amirasaad/GDL",
                ],
            }
        }
