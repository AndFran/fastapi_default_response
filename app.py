import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import Any

VERSION = "1.0"


class VersionResponse(JSONResponse):
    def render(self, content: Any) -> bytes:
        return super().render({
            "version": VERSION,
            "content": content
        })


app = FastAPI(default_response_class=VersionResponse)


@app.get("/")
async def get_result():
    return {
        "title": "Implementing Domain-Driven Design",
        "author": "Vaughn Vernon",
        "year": 2013
    }


if __name__ == "__main__":
    uvicorn.run("app:app")
