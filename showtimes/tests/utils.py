from random import sample

import pytz
from core.settings import TIME_ZONE
from faker import Faker
from movielist.models import Movie
from showtimes.models import Screening, Cinema

faker = Faker("pl_PL")
TZ = pytz.timezone(TIME_ZONE)


def random_movies():
    """Return 3 random Movies from db."""
    movies = list(Movie.objects.all())
    return sample(movies, 3)


def add_screenings(cinema):
    """Add 3 screenings for given cinema."""
    movies = random_movies()
    for movie in movies:
        Screening.objects.create(cinema=cinema, movie=movie, date=faker.date_time_this_month(tzinfo=TZ))


def fake_cinema_data():
    """Generate fake data for cinema."""
    return {
        "name": faker.company(),
        "city": faker.city(),
    }


def create_fake_cinema():
    """Create fake cinema with some screenings."""
    cinema = Cinema.objects.create(**fake_cinema_data())
    add_screenings(cinema)
