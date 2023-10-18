from ninja import Form, Router, UploadedFile
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

@router.get('/search/{query}', response=List[AlbumRetrievalSchema])
def search_albums(request, query):
    albums = Album.objects.filter(Q(title__icontains=query) | Q(artist__stageName__icontains=query))
    return albums

@router.get('/album/get/{id}', response=Union[AlbumRetrievalSchema, str])
def get_album_by_id(request, id):
    album = Album.objects.filter(id=id)
    if album.exists():
        return album[0]
    else:
        return f"Album with ID {id} does not exists"


@router.post('/album/create/{artist_id}', response=AlbumRetrievalSchema)
def create_album(request, artist_id, data:AlbumRegistrationSchema=Form(...)):
    album = Album.objects.create(artist_id=artist_id, **data.dict())
    return album



@router.post('/album/updateAlbumArt/{id}', response=Union[AlbumRetrievalSchema, str])
def update_album_art(request, id, coverArt:UploadedFile=File(...)):
    instance = Album.objects.filter(id=id)
    if instance.exists():
        album = instance[0]
        album.coverArt = coverArt
        album.save()
        return album
    
@router.put('/album/addTrack/{album_id}', response=Union[AlbumRetrievalSchema, str])
def add_track_to_album(request, album_id, track_id):
    albumInstance = Album.objects.filter(id=album_id)
    trackInstance = Track.objects.filter(id=track_id)
    
    if albumInstance.exists():
        album = albumInstance[0]
        if trackInstance.exists():
            track = trackInstance[0]
            album.tracks.add(track)
    return album