import pytest
import pytz
from faker import Faker

from .utils import fake_cinema_data
from core.settings import TIME_ZONE
from movielist.models import Movie
from showtimes.models import Cinema, Screening

faker = Faker("pl_PL")
TZ = pytz.timezone(TIME_ZONE)


@pytest.mark.django_db
def test_add_cinema(client, set_up):
    cinemas_before = Cinema.objects.count()
    new_cinema = fake_cinema_data()
    response = client.post("/cinemas/", new_cinema, format='json')
    assert response.status_code == 201
    assert Cinema.objects.count() == cinemas_before + 1
    for key, value in new_cinema.items():
        assert key in response.data
        assert response.data[key] == value


@pytest.mark.django_db
def test_get_cinema_list(client, set_up):
    response = client.get("/cinemas/", {}, format='json')

    assert response.status_code == 200
    assert Cinema.objects.count() == len(response.data)


@pytest.mark.django_db
def test_get_cinema_detail(client, set_up):
    cinema = Cinema.objects.first()
    response = client.get(f"/cinemas/{cinema.id}/", {}, format='json')

    assert response.status_code == 200
    for field in ("name", "city", "movies"):
        assert field in response.data


@pytest.mark.django_db
def test_delete_cinema(client, set_up):
    cinema = Cinema.objects.first()
    response = client.delete(f"/cinemas/{cinema.id}/", {}, format='json')
    assert response.status_code == 204
    cinema_ids = [cinema.id for cinema in Cinema.objects.all()]
    assert cinema.id not in cinema_ids


@pytest.mark.django_db
def test_update_cinema(client, set_up):
    cinema = Cinema.objects.first()
    response = client.get(f"/cinemas/{cinema.id}/", {}, format='json')
    cinema_data = response.data
    new_name = 'test_cinema_name'
    new_city = 'test_cinema_city'
    cinema_data["name"] = new_name
    cinema_data["city"] = new_city
    response = client.patch(f"/cinemas/{cinema.id}/", cinema_data, format='json')
    assert response.status_code == 200
    cinema_obj = Cinema.objects.get(pk=cinema.id)
    assert cinema_obj.name == new_name
    assert cinema_obj.city == new_city


@pytest.mark.django_db
def test_add_screening(client, set_up):
    screening_before = Screening.objects.count()
    cinema = Cinema.objects.first()
    movie = Movie.objects.first()
    new_screening = {
        'movie': movie.title,
        'cinema': cinema.name,
        'date': faker.date_time_this_month(tzinfo=TZ).isoformat(),
    }
    response = client.post("/screenings/", new_screening, format='json')
    assert response.status_code == 201
    assert Screening.objects.count() == screening_before + 1
    new_screening["date"] = new_screening["date"].replace('+00:00', 'Z')
    for key, value in new_screening.items():
        assert key in response.data
        assert response.data[key] == value


@pytest.mark.django_db
def test_get_screening_list(client, set_up):
    response = client.get("/screenings/", {}, format='json')

    assert response.status_code == 200
    assert Screening.objects.count() == len(response.data)


@pytest.mark.django_db
def test_get_screening_detail(client, set_up):
    screening = Screening.objects.first()
    response = client.get(f"/screenings/{screening.id}/", {}, format='json')

    assert response.status_code == 200
    for field in ("movie", "cinema", "date"):
        assert field in response.data


@pytest.mark.django_db
def test_delete_screening(client, set_up):
    screening = Screening.objects.first()
    response = client.delete(f"/screenings/{screening.id}/", {}, format='json')
    assert response.status_code == 204
    screening_ids = [screening.id for screening in Screening.objects.all()]
    assert screening.id not in screening_ids


@pytest.mark.django_db
def test_update_screening(client, set_up):
    screening = Screening.objects.first()
    response = client.get(f"/screenings/{screening.id}/", {}, format='json')
    screening_data = response.data
    new_movie = Movie.objects.last()
    screening_data["movie"] = new_movie.title
    new_cinema = Cinema.objects.last()
    screening_data["cinema"] = new_cinema.name
    response = client.patch(f"/screenings/{screening.id}/", screening_data, format='json')
    assert response.status_code == 200
    screening_obj = Screening.objects.get(id=screening.id)
    assert screening_obj.movie == new_movie
    assert screening_obj.cinema == new_cinema
