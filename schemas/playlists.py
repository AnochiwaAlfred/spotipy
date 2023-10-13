from ninja import Schema
import uuid
from schemas.clients import *
from schemas.tracks import *
from datetime import date


class PlaylistRegistrationSchema(Schema):
    title:str=None
    description:str=None
    
class PlaylistRetrievalSchema(Schema):
    id:uuid.UUID=None
    title:str=None
    description:str=None
    client:ClientRetrievalSchema=None
    tracks:List[TrackRetrievalSchema]=None
    
# class addTracksSchema(Schema):
#     tracks:List[str]=None