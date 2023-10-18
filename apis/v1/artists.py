from ninja import Router, UploadedFile, Form, File
from typing import List, Union
from schemas.tracks import *
from schemas.album import *
from users.models import *
from schemas.artist import *
from decouple import config
from audio.models import *

router = Router(tags=["Artists Router"])
BASE_URL = config('BACKEND_BASE_URL') if config('ENVIRONMENT')=='production' else config('DEVELOPMENT_BACKEND_BASE__URL')


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
            coverImage=f"{BASE_URL}{artist.coverImage.url}" if artist.coverImage else None,
            image=f"{BASE_URL}{artist.image.url}" if artist.image else None,
        )
        for artist in artists
    ]
    return artistsMod

@router.get('/artist/get/{id}', response=Union[ArtistRetrievalSchema, str])
def get_artist_by_id(request, id):
    instance = Artist.objects.filter(id=id)
    if instance.exists():
        artist=instance[0]
        return ArtistRetrievalSchema(
            id=artist.id,
            email=artist.email,
            username=artist.username,
            firstName=artist.firstName,
            lastName=artist.lastName,
            stageName=artist.stageName,
            phone=artist.phone,
            bio=artist.bio,
            dateOfBirth=artist.dateOfBirth,
            coverImage=f"{BASE_URL}{artist.coverImage.url}" if artist.coverImage else None,
            image=f"{BASE_URL}{artist.image.url}" if artist.image else None,
        )
    else:
        return f"Artist with ID {id} does not exists"


@router.get('/search/{query}', response=List[ArtistRetrievalSchema])
def search_artists(request, query):
    artists = Artist.objects.filter(stageName__icontains=query)
    return artists

@router.post('/artist/create', response=ArtistRetrievalSchema)
def create_artist(request, data:ArtistRegistrationSchema=Form(...)):
    artist = Artist.objects.create(**data.dict())
    return artist

@router.post('/artist/update/{id}', response=Union[ArtistRetrievalSchema, str])
def update_artist(request, id, data:ArtistUpdateSchema=Form(...)):
    instance = Artist.objects.filter(id=id)
    if instance.exists():
        # artist = instance[0]
        data_p = data.dict()
        filterdata = {attr:value for attr,value in data_p.items() if (value != None) and (value != '')}
        if len(filterdata) > 0:
            artist = instance.filter(id=id).update(**filterdata)
            return instance[0]
        else:
            return "Data Empty"
    else:
        return f"Error: Artist with ID {id} does not exist"
   
   
     
@router.post('/updateArtistImages/{id}', response=Union[ArtistRetrievalSchema, str])
def update_artist_image(request, id, image:UploadedFile=File(...)):
    instance = Artist.objects.filter(id=id)
    if instance.exists():
        artist = instance[0]
        artist.image = image 
        artist.save()
        return artist

@router.post('/updateArtistImages/{id}', response=Union[ArtistRetrievalSchema, str])
def update_artist_cover_image(request, id, coverImage:UploadedFile=File(...)):
    instance = Artist.objects.filter(id=id)
    if instance.exists():
        artist = instance[0]
        artist.coverImage = coverImage
        artist.save()
        return artist



@router.post('artist/album/create/{artist_id}', response=AlbumRetrievalSchema)
def create_album(request, artist_id, data:AlbumRegistrationSchema=Form(...)):
    album = Album.objects.create(artist_id=artist_id, **data.dict())
    return album



@router.post('/artist/album/updateAlbumArt/{artist_id}/{album_id}', response=Union[AlbumRetrievalSchema, str])
def update_album_art(request, artist_id, album_id, coverArt:UploadedFile=File(...)):
    albumInstance = Album.objects.filter(id=album_id, artist_id=artist_id)
    if albumInstance.exists():
        album = albumInstance[0]
        album.coverArt = coverArt
        album.save()
        return album
    
@router.put('/artist/album/addTrack/{artist_id}/{album_id}/{track_id}', response=Union[AlbumRetrievalSchema, str])
def add_track_to_album(request, artist_id, album_id, track_id):
    albumInstance = Album.objects.filter(id=album_id, artist_id=artist_id)
    trackInstance = Track.objects.filter(id=track_id)
    
    if albumInstance.exists():
        album = albumInstance[0]
        if trackInstance.exists():
            track = trackInstance[0]
            album.tracks.add(track)
    return album
 
@router.get('/artist/followers/list/{artist_id}', response=Union[List[ClientRetrievalSchema], str])
def list_artists_followers(request, artist_id):
    followings = Follower.objects.filter(followed_id=artist_id)
    followers = [following.follower for following in followings]
    return followers

@router.get('/artist/followers/count/{artist_id}')
def count_artists_followers(request, artist_id):
    followings = Follower.objects.filter(followed_id=artist_id)
    followersCount = followings.count()
    return followersCount
