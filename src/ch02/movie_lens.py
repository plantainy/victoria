__author__ = 'plantain'
__data__ = 'data/ch02/'

import pandas as pd

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table(__data__ + 'movielens/users.dat', sep='::', header=None, names=unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table(__data__ + 'movielens/ratings.dat', sep='::', header=None, names=rnames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table(__data__ + 'movielens/movies.dat', sep='::', header=None, names=mnames)

data = pd.merge(pd.merge(ratings, users), movies)

mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')

ratings_by_title = data.groupby('title').size()
active_titles = ratings_by_title.index[ratings_by_title >= 250]

mean_ratings = mean_ratings.ix[active_titles]

top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)

mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_index(by='diff')

# Standard deviation of rating grouped by title
rating_std_by_title = data.groupby('title')['rating'].std()
# Filter down to active titles
rating_std_by_title = rating_std_by_title.ix[active_titles]
# Order Series by value in descending order
ordered_rating_std_by_title = rating_std_by_title.order(ascending=False)

print 'Import done'
