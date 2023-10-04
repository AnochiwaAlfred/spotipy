from ninja import Schema, File
from typing import List
from datetime import date




class ArtistRegistrationSchema(Schema):
    email:str
    password:str
    username:str
    firstName:str
    lastName:str
    stageName:str
    phone:str
    bio:str
    dateOfBirth:date

class ArtistRetrievalSchema(Schema):
    id:int=None
    email:str=None
    username:str=None
    firstName:str=None
    lastName:str=None
    stageName:str=None
    phone:str=None
    bio:str=None
    image:str=None
    coverImage:str=None
    dateOfBirth:date=None