from ninja import Form, Router, UploadedFile
from typing import List, Union
from schemas.tracks import *
from schemas.playlists import *
from audio.models import *
from users.models import *
from django.db.models import Q

router = Router(tags=["Playlists Router"])

@router.get('/getAllPlaylists', response=Union[List[PlaylistRetrievalSchema], str])
def get_all_playlists(request):
    playlists = Playlist.objects.all()
    return playlists

@router.get('/playlist/{id}', response=Union[PlaylistRetrievalSchema, str])
def get_playlist_by_id(request, id):
    playlist = Playlist.objects.filter(id=id)
    if playlist.exists():
        return playlist[0]
    else:
        return f"Playlist with ID {id} does not exists"

@router.delete('/playlist/delete/{playlist_id}/{client_id}')
def delete_playlist(request, client_id, playlist_id):
    playlistInstance = Playlist.objects.filter(id=playlist_id, client_id=client_id)
    
    if playlistInstance.exists():
        playlist = playlistInstance[0]
        playlist.delete()
        return f"Playlist {playlist.title} deleted successfully"
    else:
        return f"Playlist with ID {id} does not exists"

@router.get('/search/{query}', response=List[PlaylistRetrievalSchema])
def searchPlaylists(request, query):
    playlists = Playlist.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    return playlists

@router.post('/playlist/create/{client_id}', response=PlaylistRetrievalSchema)
def create_Playlist(request, client_id, data:PlaylistRegistrationSchema=Form(...)):
    playlist = Playlist.objects.create(client_id=client_id, **data.dict())
    return playlist


@router.put('/playlist/tracks/add/{client_id}/{playlist_id}/{track_id}', response=Union[PlaylistRetrievalSchema, str])
def add_track_to_playlist(request, client_id, playlist_id, track_id):
    playlistInstance = Playlist.objects.filter(id=playlist_id, client_id=client_id)
    trackInstance = Track.objects.filter(id=track_id)
    if playlistInstance.exists():
        playlist = playlistInstance[0]
        if trackInstance.exists():
            track = trackInstance[0]
            playlist.tracks.add(track)
            return playlist
        else:
            return f"Track with ID {track_id} does not exist"
    else:
        return f"Playlist with ID {playlist_id} does not exist"

@router.put('/playlist/track/remove/{client_id}/{playlist_id}/{track_id}', response=PlaylistRetrievalSchema)
def remove_track_from_playlist(request, client_id, playlist_id, track_id):
    playlistInstance = Playlist.objects.filter(id=playlist_id, client_id=client_id)
    trackInstance = Track.objects.filter(id=track_id)
    if playlistInstance.exists():
        playlist = playlistInstance[0]
        if trackInstance.exists():
            track = trackInstance[0]
            playlist.tracks.remove(track)
            return playlist
        else:
            return f"Track with ID {track_id} does not exist"
    else:
        return f"Playlist with ID {playlist_id} does not exist"
    
