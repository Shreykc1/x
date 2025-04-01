import pandas as pd
import numpy as np
from sklearn.metrics import pairwise_distances

def collaborative_filtering(ratings, similarity_metric='cosine'):
    user_similarity = 1 - pairwise_distances(ratings, metric=similarity_metric)
    predicted_ratings = ratings.dot(user_similarity) / np.abs(user_similarity).sum(axis=1)
    return predicted_ratings

def predict_missing_ratings(ratings, predicted_ratings):
    missing_mask = np.isnan(ratings)
    filled_ratings = ratings.copy()
    filled_ratings[missing_mask] = predicted_ratings[missing_mask]
    return filled_ratings

if __name__ == '__main__':
    ratings_data = {'User1': [5, 3, np.nan, 1], 'User2': [4, np.nan, 4, np.nan], 'User3': [1, 2, np.nan, 5], 'User4': [np.nan, 4, 5, 4]}
    ratings_df = pd.DataFrame(ratings_data)
    ratings = ratings_df.values
    predicted_ratings = collaborative_filtering(np.nan_to_num(ratings))
    filled_ratings = predict_missing_ratings(ratings, predicted_ratings)
    filled_df = pd.DataFrame(filled_ratings, columns=ratings_df.columns)
    print(filled_df)
