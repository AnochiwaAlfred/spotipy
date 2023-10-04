from ninja import Schema, File
from typing import List
from datetime import date




class ClientRegistrationSchema(Schema):
    email:str
    password:str
    username:str
    firstName:str
    lastName:str
    phone:str
    bio:str
    dateOfBirth:date

class ClientRetrievalSchema(Schema):
    id:int=None
    email:str=None
    username:str=None
    firstName:str=None
    lastName:str=None
    phone:str=None
    bio:str=None
    dateOfBirth:date=None
    image:str=None