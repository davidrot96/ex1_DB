-- create table oscars(
--   id varchar,
--   film_name varchar,
--   oscar_year varchar,
--   studio varchar,
--   award varchar,
--   release_year varchar,
--   duration varchar,
--   genres varchar,
--   imdb_rating varchar,
--   imdb_votes varchar,
--   content_rating varchar,
--   directors varchar,
--   authors varchar,
--   actors varchar,
--   filmId varchar
-- );
create table movie_person(
    name varchar(100),
    primary key (name)
);

create table author(
    name varchar(100),
    primary key (name),
    foreign key (name) references movie_person(name)
);


create table actor(
    name varchar(100),
    primary key (name),
    foreign key (name) references movie_person(name)
);

create table director(
    name varchar(100),
    primary key (name),
    foreign key (name) references movie_person(name)
);

create table film(
    id varchar(100),
    name varchar(100),
    year_of_release varchar(100),
    movie_time varchar(100),
    producer varchar(100),
    primary key (id, name)
);

create table awards(
    id varchar(100),
    name varchar(100),
    oscar_year varchar(100),
    awards varchar(100),
    primary key (id, name),
    foreign key (id, name) references film(id, name)
);

create table genre(
    id varchar(100),
    name varchar(100),
    genre varchar(100),
    primary key (id, name),
    foreign key (id, name) references film(id, name)
);

create table imbd(
    id varchar(100),
    name varchar(100),
    votes varchar(100),
    rate varchar(100),
    primary key (id, name),
    foreign key (id, name) references film(id, name)
);

create table content_rating(
    id varchar(100),
    name varchar(100),
    rate varchar(100),
    primary key (id, name),
    foreign key (id, name) references film(id, name)
);

create table wrote_the(
    author_name varchar(100),
    film_name varchar(100),
    film_id varchar(100),
    primary key (author_name, film_name, film_id),
    foreign key (author_name) references author(name),
    foreign key (film_name, film_id) references film(name, id)
);

create table act_in(
    actor_name varchar(100),
    film_name varchar(100),
    film_id varchar(100),
    primary key (actor_name, film_name, film_id),
    foreign key (actor_name) references actor(name),
    foreign key (film_name, film_id) references film(name, id)
);

create table direct_the(
    director_name varchar(100),
    film_name varchar(100),
    film_id varchar(100),
    primary key (director_name, film_name, film_id),
    foreign key (director_name) references director(name),
    foreign key (film_name, film_id) references film(name, id)
);