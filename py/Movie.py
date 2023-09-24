import pandas as pd

class Movie:
    movie_title = ""
    movie_genres = []
    movie_plot = ""
    release = ""
    images = ""

    df = pd.read_csv("data/movies.csv", low_memory=False)

    def __init__(self, movie_title):
        self.movie_title = movie_title
        self.movie_genres = self.getGenres()
        self.movie_plot = self.getPlot()
        self.release = self.getRelease()
        #self.images = self.getImage()
        
    def getGenres(self):
        genres = self.df.loc[self.df['title'] == self.movie_title]['genres']
        if not genres.empty:
            return genres.iloc[0]  # Access the first element of the Series
        else:
            return ""

    def getPlot(self):
        plot = self.df.loc[self.df['title'] == self.movie_title]['overview']
        if not plot.empty:
            return plot.iloc[0]  # Access the first element of the Series
        else:
            return ""

    def getRelease(self):
        release = self.df.loc[self.df['title'] == self.movie_title]['release_date']
        if not release.empty:
            return release.iloc[0]  # Access the first element of the Series
        else:
            return ""

    def __str__(self):
        return f"{self.movie_title} {self.movie_plot} {self.release}"