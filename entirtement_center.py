import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                                        "A story of a boy and his toys",
                                        "http://cdn.collider.com/wp-content/uploads/toy-story-poster1.jpg",
                                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)

the_hobbit = media.Movie (" The Hobbit Trilogy",
                                            " A story of a hobbit in his adventure",
                                            "https://reggiestake.files.wordpress.com/2012/12/the-hobbit-movie-poster-2.jpg",
                                            "https://www.youtube.com/watch?v=gs_IJcn0Kck")
#print(The_hobbit.storyline)                           
#The_hobbit.show_trailer()

nemo = media.Movie (" Finding Dory",
                    "The friendly but forgetful blue tang fish begins a search for her long-lost parents, and everyone learns a few things about the real meaning of family along the way.",
                    "http://ia.media-imdb.com/images/M/MV5BNzg4MjM2NDQ4MV5BMl5BanBnXkFtZTgwMzk3MTgyODE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=NQu-153MnGQ")

godzila = media.Movie (" Godzilla",
                       "The world is beset by the appearance of monstrous creatures, but one of them may be the only one who can save humanity.",
                       "http://ia.media-imdb.com/images/M/MV5BN2E4ZDgxN2YtZjExMS00MWE5LTg3NjQtNTkxMzJhOTA3MDQ4XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                       "https://www.youtube.com/watch?v=vIu85WQTPRc")

last_summari = media.Movie (" The Last Samurai",
                            "An American military advisor embraces the Samurai culture he was hired to destroy after he is captured in battle.",
                            "http://ia.media-imdb.com/images/M/MV5BMzkyNzQ1Mzc0NV5BMl5BanBnXkFtZTcwODg3MzUzMw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                            "https://www.youtube.com/watch?v=T50_qHEOahQ")
batman = media.Movie(" The Dark Knight",
                     "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.",
                     "http://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=EXeTwQWrcwY")

movies = [ toy_story, the_hobbit, nemo, godzila, last_summari, batman]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)

