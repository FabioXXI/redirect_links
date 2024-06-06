from fastapi import FastAPI
from starlette.responses import RedirectResponse

app = FastAPI()

URLS = {
    "google": "https://google.com"
}

@app.get("/")
async def redirect():
    return RedirectResponse(URLS["google"])