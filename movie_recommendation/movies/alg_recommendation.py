import numpy as np
from sklearn.metrics.pairwise import pairwise_distances
from .models import Movie, WatchedMovie, User

def recom():
    n_users = User.objects.count()
    n_items = Movie.objects.count()

    train_data_matrix = np.zeros((n_users, n_items))

    for i in range(1,n_users):
        user = User.objects.get(id=i)
        history = WatchedMovie.objects.filter(user=user)

        for film in history:
            train_data_matrix[i][film.movie.id] = film.rating

    user_similarity = pairwise_distances(train_data_matrix, metric='cosine')
    item_similarity = pairwise_distances(train_data_matrix.T, metric='cosine')

    def predict(ratings, similarity, type='user'):
        if type == 'user':
            mean_user_rating = ratings.mean(axis=1)
            ratings_diff = (ratings - mean_user_rating[:, np.newaxis])
            pred = mean_user_rating[:, np.newaxis] + similarity.dot(ratings_diff) / np.array([np.abs(similarity).sum(axis=1)]).T
        elif type == 'item':
            pred = ratings.dot(similarity) / np.array([np.abs(similarity).sum(axis=1)])
        return pred

    item_prediction = predict(train_data_matrix, item_similarity, type='item')
    user_prediction = predict(train_data_matrix, user_similarity, type='user')

    for i in item_prediction:
        print(i)
        print("___________________")
    for i in user_prediction:
        print(i)


    # user_prediction_filtered = np.where(user_prediction > 5)
    #
    # # Выводим индексы рейтингов, которые больше 5
    # print("Индексы рейтингов, которые больше 5 (user_prediction):")
    # print(user_prediction_filtered)
    #
    # # Применяем фильтрацию для item_prediction
    # item_prediction_filtered = np.where(item_prediction > 5)
    #
    # # Выводим индексы рейтингов, которые больше 5 (item_prediction):
    # print("Индексы рейтингов, которые больше 5 (item_prediction):")
    # print(item_prediction_filtered)

