######################################################
# Project 1: Movie Trailer Website
# Date Created: 08/11/2017
# Date Modified: 08/15/2017
# Submitted by: Widya Puspitaloka
# Description: This file creates the class Movie
#              to allow for instances of the class
#              to be used in the entertainment.py file.
######################################################

import webbrowser


class Movie():

    """ This class provides a way to store movie related information """

    def __init__(
            self, movie_title, movie_synopsis, poster_image, trailer_youtube,
            movie_director, release_date):
        """ The init function is to initialize a space or memory
            to remember details like title, storyline, image and trailer
            from the movie I create. Init will be called
            from the instance being created."""
        self.title = movie_title
        self.synopsis = movie_synopsis
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.director = movie_director
        self.date = release_date

    def show_trailer(self):
        """ This instance method function is to
            open web browser with the correct URL.
            The URL link is stored in
            the instance variable trailer_youtube_url"""
        webbrowser.open(self.trailer_youtube_url)
