import pandas as pd
import numpy as np

filmsData = pd.read_csv('C:/Users/admin/source/repos/KoP_JKH/KoP8/films.csv')

directorsFrame = pd.DataFrame(filmsData,columns = ['director','release_date','release_year'])
directorsFrame.dropna(axis=1)
directorsFrame = directorsFrame[(directorsFrame.release_date.str.match("12"))|(directorsFrame.release_date.str.match("1"))|(directorsFrame.release_date.str.match("2"))]
directorsFrame = directorsFrame.drop_duplicates(subset=['director', 'release_year'])

print(directorsFrame.director.value_counts().head(1))