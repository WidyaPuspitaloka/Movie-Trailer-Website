import media
import fresh_tomatoes

# These instances are to call constructor class
midnight_in_paris = media.Movie(
        "Midnight in Paris",
        "While on a trip to Paris with his fiancée's family, \
        a nostalgic screenwriter finds himself mysteriously \
        going back to the 1920s everyday at midnight.",
        "https://goo.gl/mxxQn5",
        "https://www.youtube.com/watch?v=FAfR8omt-CY",
        "Woody Allen",
        "10 June 2011 (USA)")

the_godfather = media.Movie(
        "The Godfather",
        "The aging patriarch of an organized crime dynasty \
        transfers control of his clandestine empire to his reluctant son.",
        "https://goo.gl/6iBDkS",
        "https://www.youtube.com/watch?v=sY1S34973zA",
        "Francis Ford Coppola",
        "24 March 1972 (USA)")

the_lord_of_the_rings = media.Movie(
        "The Lord of the Rings: The Return of the King",
        "Gandalf and Aragorn lead the World of Men against \
        Sauron's army to draw his gaze from Frodo and Sam \
        as they approach Mount Doom with the One Ring.",
        "https://goo.gl/2VWtEh",
        "https://www.youtube.com/watch?v=r5X-hFf6Bwo",
        "Peter Jackson",
        "17 December 2003 (USA)")

the_dark_knight = media.Movie(
        "The Dark Knight",
        "When the menace known as the Joker wreaks havoc \
        and chaos on the people of Gotham, \
        the caped crusader must come to terms with one of the greatest \
        psychological tests of his ability to fight injustice.",
        "https://goo.gl/39cuNR",
        "https://www.youtube.com/watch?v=EXeTwQWrcwY",
        "Christopher Nolan",
        "18 July 2008 (USA)")


alice_in_wonderland = media.Movie(
        "Alice in Wonderland",
        "Alice returns to the magical world \
        from her childhood adventure, \
        where she reunites with her old friends \
        and learns of her true destiny.",
        "https://goo.gl/GPfUzR",
        "https://www.youtube.com/watch?v=9POCgSRVvf0",
        "Tim Burton",
        "5 March 2010 (USA)")

good_will_hunting = media.Movie(
        "Good Will Hunting",
        "Will Hunting, a janitor at M.I.T., has a gift for mathematics, \
        but needs help from a psychologist to find direction in his life.",
        "https://goo.gl/oZdu8s",
        "https://www.youtube.com/watch?v=PaZVjZEFkRs",
        "Gus Van Sant",
        "9 January 1998 (USA)")


# List of all movies created
movies = [
      midnight_in_paris, the_godfather,
      the_lord_of_the_rings, the_dark_knight,
      alice_in_wonderland, good_will_hunting,
      ]

# Using open movies page function in fresh tomatoes file.
fresh_tomatoes.open_movies_page(movies)
