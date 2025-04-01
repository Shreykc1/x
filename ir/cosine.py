import numpy as np
import pandas as pd

def cosine_similarity(tf_array):
    tf_df = pd.DataFrame(tf_array, dtype="float")

    log_weights = tf_df.copy()
    log_weights[log_weights > 0] = 1 + np.log10(log_weights[log_weights > 0])

    normalized = log_weights / np.sqrt((log_weights**2).sum(axis=0))

    similarity_matrix = normalized.T @ normalized

    return similarity_matrix

# Example usage
tf_array = [
    [115, 58, 20],
    [10, 7, 11],
    [2, 0, 6],
    [0, 0, 38],
]

similarities = cosine_similarity(tf_array)
print(similarities)
