from ninja import Schema, Form
import uuid
from schemas.artist import *
from schemas.genre import *
from datetime import date
from typing import List

from schemas.tracks import *




class AlbumRegistrationSchema(Schema):
    title:str
    genre_id:str=None
    releaseDate:date

class AlbumRetrievalSchema(Schema):
    id:uuid.UUID=None
    title:str=None
    releaseDate:date=None
    coverArt:str=None
    genre:GenreRetrievalSchema=None
    artist:ArtistRetrievalSchema=None
    tracks:List[TrackRetrievalSchema]=None
    
    
    