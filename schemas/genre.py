from ninja import Schema
import uuid

class GenreRegistrationSchema(Schema):
    name:str
    description:str

class GenreRetrievalSchema(Schema):
    id:uuid.UUID=None
    name:str=None
    description:str=None