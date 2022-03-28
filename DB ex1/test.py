import csv
from io import TextIOWrapper
from zipfile import ZipFile

TABLES = {"Movie Person": [[11, 12, 13], set()],
          "Author": [[12], set()],
          "Actor": [[13], set()],
          "Director": [[11], set()],
          "Film": [[1, 3, 5, 6, 14], set()],
          "Awards": [[1, 14, 2, 4], set()],
          "Genre": [[7], set()],
          "IMDB": [[1, 14, 9, 8], set()],
          "Content_Rating": [[1, 14, 10], set()],
          "Wrote The": [[1, 12, 14], set()],
          "Act In": [[1, 13, 14], set()],
          "Direct The": [[1, 11, 14], set()]
          }

# opens file for oscars table.
# CHANGE!
# outfile = open("oscars.csv", 'w', )
# awards = open("awards.csv", 'w', )
# genre = open("genre.csv", 'w', )
# imbd = open("imbd.csv", 'w', )
# content_rating = open("content_rating.csv", 'w', )
# wrote_the = open("wrote_the.csv", 'w', )
# act_in = open("act_in.csv", 'w', )
# direct_the = open("direct_the.csv", 'w', )
# film = open("film.csv", 'w', )
# actor = open("actor.csv", 'w', )
# director = open("director.csv", 'w', )
# author = open("author.csv", 'w', )
# movie_person = open("movie_person.csv", 'w', )
#
# # outwriter = csv.writer(outfile, delimiter=",", quoting=csv.QUOTE_NONE)
#
# outwriter_awards = csv.writer(awards, delimiter=",", quoting=csv.QUOTE_NONE)
# outwriter_genre = csv.writer(genre, delimiter=",", quoting=csv.QUOTE_NONE)
# outwriter_imbd = csv.writer(imbd, delimiter=",", quoting=csv.QUOTE_NONE)
# outwriter_content_rating = csv.writer(content_rating, delimiter=",", quoting=csv.QUOTE_NONE)
# outwriter_wrote_the = csv.writer(wrote_the, delimiter=",", quoting=csv.QUOTE_NONE)
# outwriter_act_in = csv.writer(act_in, delimiter=",", quoting=csv.QUOTE_NONE)
# outwriter_direct_the = csv.writer(direct_the, delimiter=",", quoting=csv.QUOTE_NONE)
# outwriter_film = csv.writer(film, delimiter=",", quoting=csv.QUOTE_NONE)
# outwriter_actor = csv.writer(actor, delimiter=",", quoting=csv.QUOTE_NONE)
# outwriter_director = csv.writer(director, delimiter=",", quoting=csv.QUOTE_NONE)
# outwriter_author = csv.writer(author, delimiter=",", quoting=csv.QUOTE_NONE)
# outwriter_movie_person = csv.writer(movie_person, delimiter=",", quoting=csv.QUOTE_NONE)

# process_file goes over all rows in original csv file, and sends each row to process_row()
# DO NOT CHANGE!!!
def process_file():
    with ZipFile('archive.zip') as zf:
        with zf.open('oscars_df.csv', 'r') as infile:
            reader = csv.reader(TextIOWrapper(infile, 'utf-8'))
            for row in reader:
                # remove some of the columns
                chosen_indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14, 15, 16, 29]
                row = [row[index] for index in chosen_indices]

                # change "," into && in list values
                lists_values_indices = [7, 11, 12, 13]
                for list_value_index in lists_values_indices:
                    row[list_value_index] = row[list_value_index].replace(',', '&&')

                # pre-process : remove all quotation marks from input and turns NA into null value ''.
                row = [v.replace(',', '') for v in row]
                row = [v.replace("'", '') for v in row]
                row = [v.replace('"', '') for v in row]
                row = [v if v != 'NA' else "" for v in row]

                # In the first years of oscars in the database they used "/" for example 1927/28, so we will change these.
                row[2] = row[2].split("/")[0]

                # In 1962 two movies were written as winners, then we change one of them to nominee.
                if row[4] == "Winner" and row[2] == "1962" and row[14] == "8d5317bd-df12-4f24-b34d-e5047ef4665e":
                    row[4] = "Nominee"

                # In 2020 Nomadland won and marked as nominee by mistake.
                if row[2] == "2020" and row[1] == "Nomadland":
                    row[4] = "Winner"

                process_row(row)


    # flush and close the file. close all of your files.
    # for table in TABLES:
    #     table.close()
    # awards.close()
    # genre.close()
    # imbd.close()
    # content_rating.close()
    # wrote_the.close()
    # act_in.close()
    # direct_the.close()
    # film.close()
    # actor.close()
    # director.close()
    # author.close()
    # movie_person.close()

# return a list of all the inner values in the given list_value.
# you should use this to handle value in the original table which
# contains an inner list of values.
# DO NOT CHANGE!!!
def split_list_value(list_value):
    return list_value.split("&&")

# process_row should splits row into the different csv table files
# CHANGE!!!
# ['' - 0, 'Film' - 1, 'Oscar Year' - 2, 'Film Studio/Producer(s)' - 3, 'Award' - 4, 'Year of Release' - 5, 'Movie Time' - 6,
# 'Movie Genre' - 7, 'IMDB Rating' - 8, 'IMDB Votes' - 9, 'Content Rating' - 10, 'Directors' - 11, 'Authors' - 12, 'Actors' - 13, 'Film ID' - 14]
def process_row(row):
    row = [split_list_value(col) for col in row]
    # print(row)
    if row[0] == '':
        pass

    for table in TABLES:
        if table == "Author" or "Actor" or "Director" or "Genre":
            for elem in row[TABLES[table][0][0]]:
                # print(elem)
                TABLES[table][1].add(elem)


        # for i in TABLES[table][0]:




    # print(row)
    # outwriter_awards.writerow([row[1], row[14], row[2], row[4]])
    # outwriter_genre.writerow([row[1], row[14], row[7]])
    # outwriter_imbd.writerow([row[1], row[14], row[9], row[8]])
    # outwriter_content_rating.writerow([row[1], row[14], row[10]])
    # outwriter_wrote_the.writerow([row[12], row[1], row[14]])
    # outwriter_act_in.writerow([row[13], row[1], row[14]])
    # outwriter_direct_the.writerow([row[11], row[1], row[14]])
    # outwriter_film.writerow([row[1], row[14], row[5], row[6], row[3]])
    # print([row[13]])
    # outwriter_actor.writerow([row[13]])
    # outwriter_director.writerow([row[11]])
    # outwriter_author.writerow([row[12]])
    # outwriter_movie_person.writerow()


    # outwriter.writerow()
# return the list of all tables
# CHANGE!!!
def get_names():
    return ["awards",
            "genre",
            "imbd",
            "content_rating",
            "wrote_the",
            "act_in",
            "direct_the",
            "film",
            "actor",
            "director",
            "author",
            "movie_person"]

if __name__ == "__main__":
    # a = [1,0]
    # b = [2,9]
    # c = [3,8]
    # z = (*x )
    # # z.add(*x)
    # print(*x)

    process_file()
    print(TABLES["Genre"])
