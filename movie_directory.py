import media
import urllib
import fresh_tomatoes
##the instances of the movie class

a_clockwork_orange = media.movie("A Clockwork Orange",
                           "In the future, a sadistic gang leader is imprisoned and volunteers for a"
                                 "conduct-aversion experiment, but it doesn't go as planned.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY3MjM1Mzc4N15BMl5BanBnXkFtZTgwODM0NzAxMDE@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=vN-1Mup0UI0"
                           )

american_psycho = media.movie("American Psycho",
                           "A wealthy New York investment banking executive, Patrick Bateman, hides his alternate psychopathic"
                              "ego from his co-workers and friends as he delves deeper into his violent, hedonistic fantasies.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIyMTYwMTI0N15BMl5BanBnXkFtZTgwNTU2NTYxMTE@._V1_.jpg",
                           "https://www.youtube.com/watch?v=AaUk9w90zZI"
                           )

batman_begins= media.movie("Batman Begins",
                           "After training with his mentor, Batman begins his fight to free crime-ridden Gotham City from"
                               "the corruption that Scarecrow and the League of Shadows have cast upon it.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BYzc4ODgyZmYtMGFkZC00NGQyLWJiMDItMmFmNjJiZjcxYzVmXkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,676,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=QhPqez3CwiM"
                           )

fight_club = media.movie("Fight Club",
                           "An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soapmaker,"
                                "forming an underground fight club that evolves into something much, much more.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMzFjMWNhYzQtYTIxNC00ZWQ1LThiOTItNWQyZmMxNDYyMjA5XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=SUXWAEX2jlg"
                           )
forrest_gump = media.movie("Forrest Gump",
                           "The presidencies of Kennedy and Johnson, Vietnam, Watergate, and other history unfold"
                               "through the perspective of an Alabama man with an IQ of 75.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BNWIwODRlZTUtY2U3ZS00Yzg1LWJhNzYtMmZiYmEyNmU1NjMzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
                           "https://www.youtube.com/watch?v=DRc7JrORPas"
                           )
good_will_hunting = media.movie("Good Will Hunting",
                           "Will Hunting, a janitor at M.I.T., has a gift for mathematics, but needs help from a psychologist to find direction in his life.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BOTI0MzcxMTYtZDVkMy00NjY1LTgyMTYtZmUxN2M3NmQ2NWJhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,655,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=hIdsjNGCGz4"
                            )

midnight_in_paris = media.movie("Midnight in Paris",
                                "While on a trip to Paris with his fiancée's family, a nostalgic screenwriter finds"
                                    "himself mysteriously going back to the 1920s everyday at midnight.",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BMTM4NjY1MDQwMl5BMl5BanBnXkFtZTcwNTI3Njg3NA@@._V1_SY1000_CR0,0,677,1000_AL_.jpg",
                                "https://www.youtube.com/watch?v=BYRWfS2s2v4"
                                )
psycho = media.movie("Psycho",
                           "A Phoenix secretary embezzles $40,000 from her employer's client, goes on the run,"
                                "and checks into a remote motel run by a young man under the domination of his mother.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BOWQ0MjRmZmUtY2Q2Yi00ODcxLWE4NGMtMTNjMDY1YmUzMjVkXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_.jpg",
                           "https://www.youtube.com/watch?v=NUve430f63s"
                           )


star_wars_a_new_hope = media.movie("Star Wars: A New Hope",
                           "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a Wookiee and two droids"
                                   "to save the galaxy from the Empire's world-destroying battle-station while also attempting to rescue Princess Leia from the evil Darth Vader.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BNzVlY2MwMjktM2E4OS00Y2Y3LWE3ZjctYzhkZGM3YzA1ZWM2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_CR0,0,643,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=MpkrMqmmy5k"
                           )

the_dark_knight= media.movie("The Dark Knight",
                           "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham,"
                                "the Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=_PZpmTj1Q8Q"
                           )

the_graduate = media.movie("The Graduate",
                           "A disillusioned college graduate finds himself torn between his older lover and her daughter. ",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ0ODc4MDk4Nl5BMl5BanBnXkFtZTcwMTEzNzgzNA@@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=6U5BKOgFLac"
                           )

the_hunger_games = media.movie("The Hunger Games",
                               "Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games:a televised competition"
                                   "in which two teenagers from each of the twelve Districts of Panem are chosen at random to fight to the death.",
                               "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4NDg3NzYxMF5BMl5BanBnXkFtZTcwNTgyNzkyNw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                               "https://www.youtube.com/watch?v=mfmrPu43DF8"
                               )

the_princess_bride = media.movie("The Princess Bride",
                               "A fairy tale adventure about a beautiful young woman nad her one true love.",
                               "https://upload.wikimedia.org/wikipedia/en/d/db/Princess_bride.jpg",
                               "https://www.youtube.com/watch?v=VYgcrny2hRs"
                               )



the_shawshank_redemption = media.movie("The Shawshank Redemption",
                           "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg",
                           "https://www.youtube.com/watch?v=6hB3S9bIaco"
                           )


wonder_woman = media.movie("Wonder Woman",
                           "When a pilot crashes and tells of conflict in the outside world, Diana, an Amazonian warrior in training,"
                                "leaves home to fight a war, discovering her full powers and true destiny.",
                           "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",
                           "https://www.youtube.com/watch?v=VSB4wGIdDwo"
                           )
                           

##the films are sorted on the webpage by the order that they occur in movie_dirrectory.py
films = sorted([star_wars_a_new_hope,good_will_hunting,the_shawshank_redemption,the_hunger_games,midnight_in_paris,wonder_woman,the_princess_bride,fight_club,batman_begins,the_dark_knight,forrest_gump,a_clockwork_orange,american_psycho,psycho,the_graduate,])


fresh_tomatoes.open_movies_page(films)
##print(the_dark_knight.storyline)

