#TODO
from dataclasses import dataclass,field
from view.Client.shemas import Client , ClientCreate
@dataclass
class data:
    last_id : int = 0
    clients : dict[int : Client] = field( default_factory= dict )

    @property
    def next_id (self) -> int:
        self.last_id += 1
        return self.last_id

    def Client_List(self) -> list[clients]:
        return list(self.clients.values())

    def Client_Create(self, new_client : ClientCreate) -> Client:
        client = Client(id = self.next_id, **new_client.model_dump())
        self.clients[self.last_id] = client
        return client

    def Client_Delete(self,id : int) -> clients:
        return self.clients.pop(id,None)

    def Client_Id(self,id : int) -> clients:
        return self.clients.get(id,None)

DataClient = data()