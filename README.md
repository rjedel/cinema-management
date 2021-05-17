# Cinema Management

WebAPI that allows you to control what movies are screened in the cinema chain. This project has implemented **REST API** backend, **Django REST framework** was used.

### Tests:

Tests have been implemented in the **pytest** framework.

### Endpoints:

- /movies/
    - GET - list of movies
    - POST - creates a new movie

- movies/{id}/
    - GET - movie details
    - PUT - changes information about a movie with the given id
    - DELETE - removes the movie with the given id

- /cinemas/ - GET and POST
  
- /cinemas/{id}/ - GET, PUT and DELETE
  
- /screenings/ - GET and POST
  
- /screenings/{id} - GET, PUT and DELETE
  
- /screenings/?cinema__city=search_city_name - filtering by the city in which the cinema is located
  
- /screenings/?movie__title=search_movie_title - filtering by the title
  
- /screenings/?movie__title=search_movie_title&cinema__city=search_city_name - both filters combined

