#TODO
from pydantic import BaseModel
# SHEMAS
class ClientBase(BaseModel):
    name : str
    age : int
class ClientCreate(ClientBase):
    '''
    this class created a new client
    '''
class Client(ClientBase):
    id : int
