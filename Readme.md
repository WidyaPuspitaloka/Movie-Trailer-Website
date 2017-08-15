# Movie Trailer Website - FSND Project 1

This is the source code for the Movie Trailer website project, the first project of Full Stack Nanodegree Programme in Udacity. This project is made by Widya A. Puspitaloka.

The website will show a list of some movies along with a few line of synopsis and the trailer.

### Installation
Python is needed to run and build the website.
This website was developed in Python 2.7.13 and used `fresh-tomatoes.py` which is provided by Udacity to display the website created.

### Building the Website
* Python class (Movie) is created in `media.py` file to store some of my favorite movies which include movie title, poster URL, synopsis, release date, and a link to the movie trailer.
* A constructor is written in `media.py` to be able to create multiple instances of that Pyhton class; all the instances are grouped together in a list.
* A list of the movie objects is created in `entertainment_center.py` by calling the constructor `media.Movie()` to instantiate movie objects.
* By defining the movie class and constructor, the own custom date structure is created for the movies, and now these objects can be stored in a list data structure.
* A Python module called `fresh_tomatoes.py` provided by Udacity will help generate the website that displays those movies. This module has a function called `open_movies_page()` that takes in one argument.
* The list of movies created before is what the `open_movies_page()` function needs as input in order to build the HTML file, so the website can be displayed.

### Usage
* Download Python (if you have not already)
* Download all the files (`media.py`, `entertainment_center.py`, and `fresh_tomatoes.py`)
* Open all the files in your text editor and run the code in `entertainment_center.py` file to display the website on the browser
or
* Use terminal to go to the local file path where you download the files.
* Once you are in the correct path, open the files and run code in `entertainment_center.py` file to display the website on the browser

### Notes
The hover color is changed from the original `fresh_tomatoes.py` file

### License
This project is released under the [MIT License](https://opensource.org/licenses/MIT)