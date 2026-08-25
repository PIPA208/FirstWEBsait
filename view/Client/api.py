#TODO
from fastapi import APIRouter, HTTPException, status
from view.Client.CRUD import DataClient, Client, ClientCreate
from view.Client.shemas import ClientBase

view = APIRouter(prefix = "/client", tags = ["Client"])

@view.get("/list")
def Client_list() -> list:
    return DataClient.Client_List()

@view.get("/{id}", response_model = ClientBase)
def Clien_id(id : int):
    if DataClient.Client_Id(id) is not None:
        return DataClient.Client_Id(id)
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND)

@view.post("/create", response_model= Client)
def Client_create(client : ClientCreate):
    return DataClient.Client_Create(client)

@view.delete("/delete/{id}")
def Clien_id(id : int):
    if DataClient.Client_Delete(id) is not None:
        return HTTPException(status_code= status.HTTP_200_OK)
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND)