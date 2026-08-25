#TODO
from fastapi import APIRouter
from view.Client.api import view
# NAME A VIEW API
Api = APIRouter()
Api.include_router(view)