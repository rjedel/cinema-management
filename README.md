# Cinema Management

This is a Web APIs application for the management of the cinema. The **Django REST framework** was used to build it.

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

