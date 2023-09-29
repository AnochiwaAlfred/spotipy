from ninja import Router
from typing import List, Union
from schemas.tracks import *
from audio.models import *
from django.db.models import Q


router = Router(tags=["Tracks Router"])

@router.get('/getAllTracks', response=Union[List[TrackRetrievalSchema], str])
def getAllTracks(request):
    tracks = Track.objects.all()
    return tracks


@router.get('/getAllTracksMini', response=Union[List[TrackRetrievalSchemaMini], str])
def getAllTracksMini(request):
    tracks = Track.objects.all()
    tracks2 = [TrackRetrievalSchemaMini(
            id=track.id,
            title=track.title,
            coverImage=f"http://127.0.0.1:8000{track.coverImage.url}" if track.coverImage else None,
            artist=track.artist.username
        ) 
    for track in tracks]
    return tracks2

@router.get('/getTrackById/{id}', response=Union[TrackRetrievalSchema, str])
def getTrackById(request, id):
    track = Track.objects.filter(id=id)
    if track.exists():
        return track[0]
    else:
        return f"Track with ID {id} does not exist"
    
    
@router.get('/searchTrack/{query}', response=List[TrackRetrievalSchema])
def searchTracks(request, query):
    tracks = Track.objects.filter(Q(title__icontains=query) | Q(artist__stageName__icontains=query))
    return tracks