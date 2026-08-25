#TODO
import uvicorn
from fastapi import FastAPI
from view.api import Api
# NAME A MAIN API
app = FastAPI()
# INCLUDE_ROUTER(Api)
app.include_router(Api)
if __name__ == '__main__':
    uvicorn.run(
"main:app",reload=True
)
