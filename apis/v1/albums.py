from ninja import Router
from typing import List, Union
from schemas.tracks import *
from schemas.album import *
from audio.models import *

router = Router(tags=["Albums Router"])

@router.get('/getAllAlbums', response=Union[List[AlbumRetrievalSchema], str])
def getAllAlbums(request):
    albums = Album.objects.all()
    return albums

@router.get('/getAlbumById/{id}', response=Union[AlbumRetrievalSchema, str])
def getAlbumById(request, id):
    album = Album.objects.filter(id=id)
    if album.exists():
        return album[0]
    else:
        return f"Album with ID {id} does not exists"
