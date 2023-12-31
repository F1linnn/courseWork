import numpy as np
from sklearn.metrics.pairwise import pairwise_distances
from .models import Movie, WatchedMovie, User

def recom(request):
    n_users = User.objects.count()
    n_items = Movie.objects.count()
    ids = list(range(Movie.objects.count()))
    train_data_matrix = np.zeros((n_users, n_items))

    for i in range(1,n_users+1):
        user = User.objects.get(id=i)
        print(user.username)
        history = WatchedMovie.objects.filter(user=user)

        for film in history:
            train_data_matrix[i-1][film.movie.id-1] = film.rating


    user_similarity = pairwise_distances(train_data_matrix, metric='cosine')
    item_similarity = pairwise_distances(train_data_matrix.T, metric='cosine')

    print(user_similarity)
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

    # for i in range(len(item_prediction)):
    #     print(f"User: {i+1}")
    #     print(item_prediction[i])
    #     # for j in range(len(item_prediction[i])):
    #     #     if item_prediction[i][j] > 0.16:
    #     #         print(f"Film-id: {j+1}, %: {item_prediction[i][j]}")
    #     print("___________________")
    # print("_______NEXT STEP__________")


    result = dict(zip(ids,user_prediction[request.user.id-1]))
    watched = WatchedMovie.objects.filter(user=request.user)
    for film in watched:
        result.pop(film.movie.id-1)
    print(len(result))

    sorted_result = sorted(result.items(), key=lambda x:x[1], reverse=True)
    top5 = sorted_result[:5]
    top5 = [k[0]+1 for k in top5]
    print(top5)
    return top5

    # for i in range(len(user_prediction)):
    #     print(f"User: {i+1}")
    #     for j in range(len(user_prediction[i])):
    #         if user_prediction[i][j] > 0.76:
    #             print(f"Film-id: {j+1}, %: {user_prediction[i][j]}")


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

