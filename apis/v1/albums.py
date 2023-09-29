from ninja import Router
from typing import List, Union
from schemas.tracks import *
from schemas.album import *
from audio.models import *
from django.db.models import Q

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

@router.get('/searchAlbums/{query}', response=List[AlbumRetrievalSchema])
def searchAlbums(request, query):
    albums = Album.objects.filter(Q(title__icontains=query) | Q(artist__stageName__icontains=query))
    return albums