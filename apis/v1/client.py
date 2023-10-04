from ninja import Router
from typing import List, Union
from schemas.tracks import *
from schemas.album import *
from users.models import *
from schemas.clients import *

router = Router(tags=["Clients Router"])

@router.get('/getAllClients', response=List[ClientRetrievalSchema])
def getAllClients(request):
    clients = Client.objects.all()
    return clients

@router.get('/getClientById/{id}', response=ClientRetrievalSchema)
def getClientById(request, id):
    client = Client.objects.filter(id=id)
    if client.exists():
        return client[0]

