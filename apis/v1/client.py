from ninja import Form, Router, UploadedFile
from typing import List, Union
from schemas.likeSongs import LikeSongRetrievalSchema
from schemas.tracks import *
from schemas.album import *
from schemas.clients import *
from schemas.followers import *
from schemas.playlists import *
from audio.models import *
from users.models import *


router = Router(tags=["Clients Router"])

@router.get('/get', response=List[ClientRetrievalSchema])
def get_all_clients(request):
    clients = Client.objects.all()
    return clients

@router.get('/client/get/{id}', response=ClientRetrievalSchema)
def get_client_by_id(request, id):
    client = Client.objects.filter(id=id)
    if client.exists():
        return client[0]
    
    
@router.post('/client/create', response=ClientRetrievalSchema)
def create_client(request, data:ClientRegistrationSchema=Form(...)):
    client = Client.objects.create(**data.dict())
    return client

@router.post('/updateClientImage/{id}', response=Union[ClientRetrievalSchema, str])
def update_client_image(request, id, image:UploadedFile=File(...)):
    instance = Client.objects.filter(id=id)
    if instance.exists():
        client = instance[0]
        client.image = image
        client.save()
        return client
    
# @router.get('/universalSearch/{query}')
    
@router.post('/likeOrUnlikeSong/{client_id}/{track_id}')
def client_like_or_unlike_song(request, client_id, track_id):
    likeSongCheck = LikeSong.objects.filter(client_id=client_id, track_id=track_id)
    if likeSongCheck.exists():
        likeSong=likeSongCheck[0]
        likeSong.delete()
        return f"Track {likeSong.track} removed from favorite"    
    else:
        likeSong = LikeSong.objects.create(client_id=client_id, track_id=track_id)
        return f"Track {likeSong.track} added to favorite"    
        
    
@router.get('/likes/{client_id}', response=List[TrackRetrievalSchema])
def retrieve_client_liked_songs(request, client_id):
    likedSongs = LikeSong.objects.filter(client_id=client_id)
    tracks = [likedSong.track for likedSong in likedSongs]
    return tracks

@router.post('/playlist/create/{client_id}', response=PlaylistRetrievalSchema)
def create_playlist(request, client_id, data:PlaylistRegistrationSchema):
    playlist = Playlist.objects.create(**data.dict())
    return playlist

@router.get('/playlist/get/{playlist_id}', response=Union[PlaylistRetrievalSchema, str])
def get_playlist(request, playlist_id):
    playlist = Playlist.objects.filter(id=playlist_id)
    if playlist.exists():
        return playlist[0]
    return f"Playlist {playlist_id} does not exist"

@router.post('/playlist/delete/{playlist_id}')
def delete_playlist(request, playlist_id):
    playlist = Playlist.objects.filter(id=playlist_id)
    playlist[0].delete()
    return f"Playlist {playlist[0].title} deleted"

@router.put('/playlist/addTrack/{playlist_id}/{track_id}', response=PlaylistRetrievalSchema)
def add_track_to_playlist(request, playlist_id, track_id):
    playlist = Playlist.objects.get(id=playlist_id)
    track = Track.objects.get(id=track_id)
    playlist.tracks.add(track)
    playlist.save()
    return playlist

@router.put('/playlist/removeTrack/{playlist_id}/{track_id}', response=PlaylistRetrievalSchema)
def remove_track_from_playlist(request, playlist_id, track_id):
    playlist = Playlist.objects.get(id=playlist_id)
    track = Track.objects.get(id=track_id)
    playlist.tracks.remove(track)
    playlist.save()
    return playlist


@router.post('/following/FollowOrUnfollowArtist/{client_id}/{artist_id}')
def client_follow_or_unfollow_artist(request, client_id, artist_id):
    followingCheck = Follower.objects.filter(follower_id=client_id, followed_id=artist_id)
    if followingCheck.exists():
        following=followingCheck[0]
        following.delete()
        return f"{following.follower} unfollowed {following.followed}"    
    else:
        following = Follower.objects.create(follower_id=client_id, followed_id=artist_id)
        return f"{following.follower} followed {following.followed}"    
        
    
@router.get('/following/{client_id}', response=List[ArtistRetrievalSchema])
def retrieve_client_followed_artists(request, client_id):
    followings = Follower.objects.filter(follower_id=client_id)
    artists = [following.followed for following in followings]
    return artists


