import pandas as pd
#from IPython.display import Image, display

class Recommend:
    df = pd.read_csv("data/movies.csv", low_memory=False)

    def __init__(self, movie_title):
        self.movie_title = movie_title

    def getRecs(self, row):
        temp = self.df.iloc[row]['recommendations']
        temp = temp.split('-')
        return temp
    
    def titleToPoster(self, movie_title):
        base_domain = 'https://image.tmdb.org/t/p/w500'
        image_links = base_domain + self.df.loc[self.df['title'] == movie_title, 'poster_path'].iloc[0]
        image_widget = Image(url=image_links, width=200, height=300)
        display(image_widget)

    def getRecTitles1 (self, title):
        matching_rows = self.df['title'] == title
        row_numbers = matching_rows.index[matching_rows].tolist()
        row = row_numbers[0]
        arr = self.getRecs(row)
        return arr
    
    def getRecTitles2 (self, title):
        arr = self.getRecTitles1(title)
        for i in range(len(arr)):
            matching_rows = self.df['id'] == int(arr[i])
            row = matching_rows.index[matching_rows].tolist()
            for x in row:
                arr[i] = x
        tarr = [x for x in arr if isinstance(x, int)]
        titles = []
        for i in range(len(tarr)):
            titles.append(self.df.iloc[tarr[i]]['title'])
        return titles

    
if __name__ == '__main__':
    rec = Recommend("")
    print(rec.getRecTitles2("Creed III"))
    print(rec.getRecTitles2("Ted"))
    print(rec.getRecTitles2("It"))