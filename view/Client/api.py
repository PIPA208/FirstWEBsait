#TODO
from fastapi import APIRouter, HTTPException, status
from view.Client.CRUD import DataClient, Client, ClientCreate
from view.Client.shemas import ClientBase

view = APIRouter(prefix = "/client", tags = ["Client"])

@view.get("/list", response_model= list[Client],responses={
    status.HTTP_500_INTERNAL_SERVER_ERROR:
        {"descripton": "Problem in code", "content":{
            "application/json":{
                "shema":{
                    "title":"Problem","detail": "Maybe problem in response_model or return in func"
                }
            }
        }
        }
    }
)
def Client_list() -> list[Client]:
    return DataClient.Client_List()

@view.get("/{id}", response_model = ClientBase,responses={
    status.HTTP_404_NOT_FOUND:
        {"descripton": "Dont have a client", "content":{
            "application/json":{
                "shema":{
                "title": f"Dont have a client id = {id}"
                    }
                }
            }
        }
    }
)
def Clien_id(id : int) -> Client:
    if DataClient.Client_Id(id) is not None:
        return DataClient.Client_Id(id)
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND)

@view.post("/create", response_model= Client,responses={
    status.HTTP_500_INTERNAL_SERVER_ERROR:
        {"descripton": "Problem in code", "content":{
            "application/json":{
                "shema":{
                    "title":"Problem","detail": "Maybe problem in response_model or return in func"
                }
            }
        }
        }
    }
)
def Client_create(client : ClientCreate) -> Client:
    return DataClient.Client_Create(client)

@view.delete("/delete/{id}",responses={
    status.HTTP_404_NOT_FOUND:
        {"descripton": "Dont have a client", "content":{
            "application/json":{
                "shema":{
                "title": f"Dont have a client id = {id}"
                    }
                }
            }
        }
    }
)
def Clien_id(id : int) -> status:
    if DataClient.Client_Delete(id) is not None:
        return HTTPException(status_code= status.HTTP_200_OK)
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND)