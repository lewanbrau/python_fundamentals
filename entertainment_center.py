import media
import fresh_tomatoes


# define the different movie titles, descriptions,
# movie posters and youtube trailers
toy_story = media.Movie(
    "Toy Story",
    "A toy goes out for an adventure", 
    "http://vignette4.wikia.nocookie.net/disney/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20140816182710",  # noqa
    "https://www.youtube.com/watch?v=KYz2wyBy3kc"
    )

avatar = media.Movie(
    "Avatar",
    "Bunch of aliens have hair sex", 
    "http://pre02.deviantart.net/51e1/th/pre/f/2010/192/b/e/avatar_special_edition_poster_by_j_k_k_s.jpg",  # noqa
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
    )

harry_potter = media.Movie(
    "Harry Potter",
    "A little kid becomes a wizzard and defeates his enimies by chance", 
    "http://www.harrypottermovieposters.com/wp-content/uploads/2013/08/harry-potter-and-the-deathly-hallows-part-2-movie-poster-style-k1.jpg",  # noqa
    "https://www.youtube.com/watch?v=_EC2tmFVNNE"
    )

chappie = media.Movie(
    "Chappie",
    "A robot becomes self aware and then a South African gangster", 
    "http://www.fatmovieguy.com/wp-content/uploads/2014/11/Chappie-Movie-Poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=QHWbzrCJ4nE"
    )

kung_pow = media.Movie(
    "Kung Pow",
    "An old movie was dubbed over and characters added to make it a comedy", 
    "http://ia.media-imdb.com/images/M/MV5BMTYyODQwODY1N15BMl5BanBnXkFtZTcwNzE3ODI1MQ@@._V1_SX640_SY720_.jpg",  # noqa
    "https://www.youtube.com/watch?v=GXrAYdSeWY8"
    )

inglourious_basterds = media.Movie(
    "Inglourious Basterds",
    "Brad Pitt does world war 2", 
    "http://img02.deviantart.net/9c0d/i/2013/262/b/3/inglourious_basterds___movie_poster_by_zungam80-d6mwea5.jpg",  # noqa
    "https://www.youtube.com/watch?v=QHWbzrCJ4nE"
    )

# create a list of all movie names
movies = [
    toy_story,
    avatar,
    harry_potter,
    chappie,
    kung_pow,
    inglourious_basterds
    ]

# pass the movies list to the open_movies_page funciton
fresh_tomatoes.open_movies_page(movies)
