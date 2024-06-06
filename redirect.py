from fastapi import FastAPI, HTTPException
from starlette.responses import RedirectResponse

app = FastAPI()

URLS = {}

@app.post("/{alias}")
async def create_alias_link(alias: str):
    URLS[alias] = "https://" + alias + ".com"
    return "Ok"

@app.get("/{alias}")
async def get_alias_link_redirect(alias: str):
    if alias in URLS.keys():
        return RedirectResponse(URLS[alias])
    raise HTTPException