from ninja import Schema, File
from typing import List
from datetime import date




class ClientRegistrationSchema(Schema):
    email:str
    password:str
    username:str
    firstName:str
    lastName:str
    phone:str=None
    dateOfBirth:date=None

class ClientRetrievalSchema(Schema):
    id:int=None
    email:str=None
    username:str=None
    firstName:str=None
    lastName:str=None
    phone:str=None
    dateOfBirth:date=None
    image:str=None