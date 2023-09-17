from ninja import Schema
import uuid
from schemas.artist import *
from schemas.genre import *
from datetime import date



class TrackRegistrationSchema(Schema):
    title:str=None
    lyrics:str=None
    artist:str
    genre_id:str
    # audioFile:str=None
    # coverImage:str=None


class TrackRetrievalSchema(Schema):
    id:uuid.UUID=None
    title:str=None
    lyrics:str=None
    playCount:int=None
    releaseDate:date=None
    audioFile:str=None
    coverImage:str=None
    artist:ArtistRetrievalSchema=None
    genre:GenreRetrievalSchema=None
    
class TrackRetrievalSchemaMini(Schema):
    id:uuid.UUID=None
    title:str=None
    coverImage:str=None
    artist:str=None