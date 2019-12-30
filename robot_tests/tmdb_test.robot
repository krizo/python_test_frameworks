*** Settings ***
Library  tmdb_keywords.py
Library  utils_keywords.py
Library  Collections

*** Variables ***
${tv_show_id}       1396
# how to break the line when so many lists' elements?
@{tv_show_fields}   id  origin_country  poster_path     name    overview    popularity  backdrop_path   first_air_date  vote_count  vote_average
${movie_name}       Forrest Gump
@{movie_fields}     popularity  vote_count  video   poster_path     id  adult   backdrop_path   original_language   original_title  genre_ids   title   vote_average    overview    release_date

*** Keywords ***
verify tv shows response fields
    [Arguments]      ${response}
    list should contain sub list     ${response}     ${tv_show_fields}

verify movies search response
    [Arguments]      ${response}
    is dict         ${response}
    is list         ${response['results']}
    is dict         ${response['results'][0]}
    list should contain sub list     ${response['results'][0]}  ${movie_fields}



*** Test Cases ***
TMDB check response of getting specific movie's info
    ${response}   get tv show info     ${tv_show_id}
    verify tv shows response fields    ${response.keys()}

TMDB check response of popular tv shows
    ${response}     get popular shows
    is dict         ${response}
    is list         ${response['results']}
    is dict         ${response['results'][0]}
    verify tv shows response fields    ${response['results'][0]}


TMBD check response of movies search
    ${response}     search movie    ${movie_name}
    verify movies search response   ${response}



