from ninja import Schema
import uuid
from schemas.clients import *
from schemas.tracks import *
from datetime import date


class FollowerRegistrationSchema(Schema):
    follower_id:str=None
    followed_id:str=None
    
class FollowerRetrievalSchema(Schema):
    id:uuid.UUID
    follower:ClientRetrievalSchema=None
    followed:ArtistRetrievalSchema=None