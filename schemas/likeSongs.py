from ninja import Schema
import uuid
from schemas.clients import *
from schemas.tracks import *
from datetime import date


class LikeSongRetrievalSchema(Schema):
    id:uuid.UUID=None
    client:ClientRetrievalSchema=None
    track:TrackRetrievalSchema=None
    
