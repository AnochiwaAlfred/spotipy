
from ninja import Router, Form
from typing import List, Union
from schemas.genre import *
from audio.models import *

router = Router(tags=['Genre Router'])

@router.post('/genre/add', response=GenreRetrievalSchema)
def add_genre(request, data:GenreRegistrationSchema):
    genre = Genre.objects.create(**data.dict())
    return genre


@router.get('/getAllGenre', response=List[GenreRetrievalSchema])
def list_genre(request):
    genres = Genre.objects.all()
    return genres


@router.get('/genre/{genre_id}', response=GenreRetrievalSchema)
def get_genre(request, genre_id):
    genreInstance = Genre.objects.filter(id=genre_id)
    if genreInstance.exists():
        return genreInstance[0]
    return f"Genre with ID {genre_id} does not exist"


@router.delete('/genre/delete/{genre_id}')
def delete_genre(request, genre_id):
    genreInstance = Genre.objects.filter(id=genre_id)
    if genreInstance.exists():
        genre = genreInstance[0]
        genre.delete()
        return f"Genre {genre.name} deleted successfully"
    return f"Genre with ID {genre_id} does not exist"