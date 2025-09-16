SELECT DISTINCT name FROM directors,movies,people,ratings WHERE movies.id = directors.movie_id AND  people.id = directors.person_id AND movies.id = ratings.movie_id AND rating >= 9.0;
