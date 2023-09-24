import pandas as pd

class Movie:
    movie_title = ""
    movie_genres = []
    movie_plot = ""
    release = ""
    images = ""
    rating =0.0

    df = pd.read_csv("data/movies.csv", low_memory=False)

    def __init__(self, movie_title):
        self.movie_title = movie_title
        self.movie_genres = self.getGenres()
        self.movie_plot = self.getPlot()
        self.images=self.titleToPoster(movie_title)
        print(self.images)
        self.release = self.getRelease()
        #self.rating = self.getRating()

        
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
        
    #def getRating(self):
     #   rating = self.df.loc[self.df['title']] == self.movie_title['vote_average']
      #  if not rating.empty:
       #     return rating.iloc[0]  # Access the first element of the Series
        #else:
         #   return ""

    def titleToPoster(self, movie_title):
        base_domain = 'https://image.tmdb.org/t/p/w500'
        image_links = base_domain + self.df.loc[self.df['title'] == movie_title, 'poster_path'].iloc[0]
        return image_links

    def __str__(self):
        return f"{self.movie_title} {self.movie_plot} {self.release}"