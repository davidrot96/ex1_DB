create table Movie_Person(
    name varchar(100),
    primary key (name)
);

create table Author(
    name varchar(100),
    primary key (name),
    foreign key (name) references movie_person(name)
);


create table Actor(
    name varchar(100),
    primary key (name),
    foreign key (name) references movie_person(name)
);

create table Director(
    name varchar(100),
    primary key (name),
    foreign key (name) references movie_person(name)
);

create table Film(

    name varchar(100),
    producer varchar(100),
    year_of_release varchar(100),
    movie_time varchar(100),
    id varchar(100),
    primary key (id)
);

create table Awards(
    id varchar(100),
    oscar_year varchar(100),
    awards varchar(100),
    primary key (id),
    foreign key (id) references film(id)
);

create table Genre(
    genre varchar(100),
    primary key (genre)
);

create table IMDB(
    id varchar(100),
    votes varchar(100),
    rate varchar(100),
    primary key (id),
    foreign key (id) references film(id)
);

create table Content_Rating(
    rate varchar(100),
    primary key (rate)
);

create table Wrote_The(
    id varchar(100),
    name varchar(100),
    primary key (name, id),
    foreign key (name) references author(name),
    foreign key (id) references film(id)
);

create table Act_In(
    id varchar(100),
    name varchar(100),
    primary key (name, id),
    foreign key (name) references actor(name),
    foreign key (id) references film(id)
);

create table Direct_The(
    id varchar(100),
    name varchar(100),
    primary key (name, id),
    foreign key (name) references director(name),
    foreign key (id) references film(id)
);

create table Type_Of(
    id varchar(100),
    genre varchar(100),
    primary key (id, genre),
    foreign key (id) references film(id),
    foreign key (genre) references genre(genre)
);

create table Rate(
    id varchar(100),
    rate varchar(100),
    primary key (id, rate),
    foreign key (id) references film (id),
    foreign key (rate) references content_rating (rate)
);