import os
import sys
from random import randint, sample

import pytest
from movielist.models import Person, Movie
from movielist.tests.utils import faker, create_fake_movie
from rest_framework.test import APIClient
from showtimes.models import Cinema, Screening

sys.path.append(os.path.dirname(__file__))


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.fixture
def set_up():
    for _ in range(5):
        Person.objects.create(name=faker.name())
        for _ in range(1, 11):
            create_fake_movie()
        cinema = Cinema.objects.create(name=faker.company(), city=faker.city())
        for id_ in sample(range(1, 11), randint(1, 10)):
            movie_obj = Movie.objects.get(pk=id_)
            Screening.objects.create(cinema=cinema, movie=movie_obj, date=faker.date_time_this_month())
