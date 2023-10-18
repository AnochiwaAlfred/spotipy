from ninja import Schema
import uuid
from schemas.artist import *
from schemas.clients import ClientRetrievalSchema
from schemas.genre import *
from datetime import date



class TrackRegistrationSchema(Schema):
    title:str=None
    lyrics:str=None
    artist:str=None
    genre_id:str=None
    # audioFile:str=None
    # coverImage:str=None


class TrackRetrievalSchema(Schema):
    id:uuid.UUID
    title:str=None
    # lyrics:str=None
    playCount:int=None
    releaseDate:date=None
    audioFile:str=None
    coverImage:str=None
    artist:ArtistRetrievalSchema=None
    # likes:ClientRetrievalSchema=None
    genre:GenreRetrievalSchema=None
    
class TrackRetrievalSchemaMini(Schema):
    id:uuid.UUID
    title:str=None
    coverImage:str=None
    artist:str=None