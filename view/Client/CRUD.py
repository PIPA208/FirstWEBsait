#TODO
from dataclasses import dataclass,field
from view.Client.shemas import Client , ClientCreate
@dataclass
class data:
    last_id : int
    clients : dict[int : Client] = field( default_factory= dict )

    @property
    def next_id (self) -> int:
        self.last_id += 1
        return self.last_id

    def Client_List(self) -> list:
        return list(self.clients.values())

    def Client_Create(self, new_client : ClientCreate) -> clients:
        Client[self.next_id] = new_client.model_dump()
        self.clients[self.last_id] = Client
        return Client, self.clients

    def Client_Delete(self,id):
        return self.clients.pop(id)

    def Client_Id(self,id):
        return self.clients.get(id,False)