import csv
from io import TextIOWrapper
from zipfile import ZipFile

TABLES = {"Movie_Person": [[11, 12, 13], set()],
          "Author": [[12], set()],
          "Actor": [[13], set()],
          "Director": [[11], set()],
          "Film": [[1, 3, 5, 6, 14], set()],
          "Awards": [[14, 2, 4], set()],
          "Genre": [[7], set()],
          "IMDB": [[14, 9, 8], set()],
          "Content_Rating": [[10], set()],
          "Wrote_The": [[14, 12], set()],
          "Act_In": [[14, 13], set()],
          "Direct_The": [[14, 11], set()],
          "Type_Of": [[14, 7], set()],
          "Rate": [[14, 10], set()]
          }

COLUMNS = [
        '',
        'Film',
        'Oscar Year',
        'Film Studio/Producer(s)',
        'Award',
        'Year of Release',
        'Movie Time',
        'Movie Genre',
        'IMDB Rating',
        'IMDB Votes',
        'Content Rating',
        'Directors',
        'Authors',
        'Actors',
        'Film ID',
    ]
RELATIONSHIPS = {"Wrote_The", "Act_In", "Direct_The", "Type_Of", "Rate"}

# process_file goes over all rows in original csv file, and sends each row to process_row()

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

    write_to_csv()


# return a list of all the inner values in the given list_value.
# you should use this to handle value in the original table which
# contains an inner list of values.
def split_list_value(list_value):
    return list_value.split("&&")

# process_row should splits row into the different csv table files
def process_row(row):
    if row[0] == '':
        return
    for table in TABLES:
        idxes = TABLES[table][0]
        if table == "Author" or table == "Actor" or table == "Director" or table == "Genre":
            splits_val = split_list_value(row[idxes[0]])
            for elem in splits_val:
                if not elem: break
                TABLES[table][1].add((elem,))

        elif table in RELATIONSHIPS:
            splits_val = split_list_value(row[idxes[1]])
            for genre in splits_val:
                if not genre: break
                TABLES[table][1].add((row[idxes[0]], genre))

        elif table == "Movie_Person":
            idxes = TABLES[table][0]
            for j in idxes:
                for name in split_list_value(row[j]):
                    if not name: break
                    TABLES[table][1].add((name,))

        else:
            idxes = TABLES[table][0]
            attributes = []
            for i in idxes:
                if row[i] == '': break
                attributes.append(row[i])
            if len(attributes): TABLES[table][1].add(tuple(attributes))




def write_to_csv():
    titles = COLUMNS
    for table in TABLES:
        out_file = open(f'{table}.csv', 'w')
        out_writer = csv.writer(out_file, delimiter=",",
                                quoting=csv.QUOTE_NONE)
        if table == 'Movie_Person':
            movie_person_title = 'Movie_Person'
            out_writer.writerow([movie_person_title])
        else:
            out_writer.writerow([titles[title] for title in TABLES[table][0]])
        out_writer.writerows(list(TABLES[table][1]))

        out_file.close()

# return the list of all tables

def get_names():
    return [
        "Movie_Person",
        "Author",
        "Actor",
        "Director",
        "Film",
        "Awards",
        "Genre",
        "IMDB",
        "Content_Rating",
        "Wrote_The",
        "Act_In",
        "Direct_The",
        "Type_Of",
        "Rate"
            ]


if __name__ == "__main__":
    process_file()
