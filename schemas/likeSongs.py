from ninja import Schema
import uuid
from schemas.clients import *
from schemas.tracks import *
from datetime import date


class LikeSongRetrievalSchema(Schema):
    id:uuid.UUID
    client_id:str=None
    track_id:str=None
    
class LikeSongRetrievalSchemaMini(Schema):
    id:uuid.UUID
    client:ClientRetrievalSchema=None
    track:TrackRetrievalSchema=None