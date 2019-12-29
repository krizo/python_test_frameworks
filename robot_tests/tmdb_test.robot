*** Settings ***
Library  tmdb_keywords.py
Library  utils_keywords.py
Library  Collections

*** Variables ***
${movie_id}    1396
# how to break the line when so many lists' elements?
@{expected_fields}  id  origin_country  poster_path     name    overview    popularity  backdrop_path   first_air_date  vote_count  vote_average


*** Test Cases ***
TMDB check response of getting specific movie's info
    ${response}   get movie info     ${movie_id}
    list should contain sub list     ${response.keys()}  ${expected_fields}

TMDB check response of popular movies
    ${response}     get popular movies
    is dict         ${response}
    is list         ${response['results']}
    is dict         ${response['results'][0]}
    list should contain sub list     ${response['results'][0]}  ${expected_fields}



