from movie_model import MovieModel
import requests

def callMovieApi(page=1):
    url = f'''
        https://yts.mx/api/v2/list_movies.json?sort_by=rating&page_number=1&limit=20
    '''

    response = requests.get(url)

    responseDict = response.json()
    movies = responseDict["data"]["movies"]
    return convert_model(movies)


def convert_model(movies):
    list = []

    for movie in movies:
        movie_model = MovieModel(movie["small_cover_image"], movie["title"], movie["rating"], movie["summary"])
        list.append(movie_model)

    return list