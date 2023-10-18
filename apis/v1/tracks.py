from ninja import Router
from typing import List, Union
from schemas.tracks import *
from audio.models import *
from django.db.models import Q
from decouple import config

BASE_URL = config('BACKEND_BASE_URL') if config('ENVIRONMENT')=='production' else config('DEVELOPMENT_BACKEND_BASE__URL')

router = Router(tags=["Tracks Router"])

@router.get('/getAllTracks', response=Union[List[TrackRetrievalSchema], str])
def get_all_tracks(request):
    tracks = Track.objects.all()
    return tracks


@router.get('/getAllTracksMini', response=Union[List[TrackRetrievalSchemaMini], str])
def getAllTracksMini(request):
    tracks = Track.objects.all()
    tracks2 = [TrackRetrievalSchemaMini(
            id=track.id,
            title=track.title,
            coverImage=f"{BASE_URL}{track.coverImage.url}" if track.coverImage else None,
            artist=track.artist.username
        ) 
    for track in tracks]
    return tracks2

@router.get('/track/{id}', response=Union[TrackRetrievalSchema, str])
def get_track_by_id(request, id):
    track = Track.objects.filter(id=id)
    if track.exists():
        return track[0]
    else:
        return f"Track with ID {id} does not exist"
    

@router.get('/track/{id}/lyrics', response=Union[TrackRetrievalSchema, str])
def get_track_lyrics(request, id):
    track = Track.objects.filter(id=id)
    if track.exists():
        return track[0].lyrics
    else:
        return f"Track with ID {id} does not exist"
    
    
@router.get('/searchTrack/{query}', response=List[TrackRetrievalSchema])
def search_tracks(request, query):
    tracks = Track.objects.filter(Q(title__icontains=query) | Q(artist__stageName__icontains=query))
    return tracks