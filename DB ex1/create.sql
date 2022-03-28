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
    primary key (id)
);

create table awards(
    id varchar(100),
    oscar_year varchar(100),
    awards varchar(100),
    primary key (id),
    foreign key (id) references film(id)
);

create table genre(
    genre varchar(100),
    primary key (genre),
);

create table imdb(
    id varchar(100),
    votes varchar(100),
    rate varchar(100),
    primary key (id),
    foreign key (id) references film(id)
);

create table content_rating(
    rate varchar(100),
    primary key (rate)
);

create table wrote_the(
    name varchar(100),
    id varchar(100),
    primary key (name, id),
    foreign key (name) references author(name),
    foreign key (id) references film(id)
);

create table act_in(
    name varchar(100),
    id varchar(100),
    primary key (name, id),
    foreign key (name) references actor(name),
    foreign key (id) references film(id)
);

create table direct_the(
    name varchar(100),
    id varchar(100),
    primary key (name, id),
    foreign key (name) references director(name),
    foreign key (id) references film(id)
);

create table type_of(
    id varchar(100),
    genre varchar(100),
    primary key (director_name, film_name, film_id),
    foreign key (id) references film(id),
    foreign key (genre) references genre(genre)
);

create table rate(
    id varchar(100),
    rate varchar(100),
    primary key (id, rate),
    foreign key (id) references film(id),
    foreign key (rate) references content_rating(rate)