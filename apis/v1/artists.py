from ninja import Router
from typing import List, Union
from schemas.tracks import *
from schemas.album import *
from users.models import *
from schemas.artist import *

router = Router(tags=["Artists Router"])

@router.get('/getAllArtists', response=Union[List[ArtistRetrievalSchema], str])
def getAllArtists(request):
    artists = Artist.objects.all()
    artistsMod = [
        ArtistRetrievalSchema(
            id=artist.id,
            email=artist.email,
            username=artist.username,
            firstName=artist.firstName,
            lastName=artist.lastName,
            stageName=artist.stageName,
            phone=artist.phone,
            bio=artist.bio,
            dateOfBirth=artist.dateOfBirth,
            coverImage=f"http://127.0.0.1:8000{artist.coverImage.url}" if artist.coverImage else None,
            image=f"http://127.0.0.1:8000{artist.image.url}" if artist.image else None,
        )
        for artist in artists
    ]
    return artistsMod

@router.get('/getArtistById/{id}', response=Union[ArtistRetrievalSchema, str])
def getArtistById(request, id):
    artist = Artist.objects.filter(id=id)
    if artist.exists():
        return artist[0]
    else:
        return f"Artist with ID {id} does not exists"


@router.get('/searchArtists/{query}', response=List[ArtistRetrievalSchema])
def searchArtists(request, query):
    artists = Artist.objects.filter(stageName__icontains=query)
    return artists