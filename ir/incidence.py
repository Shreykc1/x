import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np
import pandas as pd

nltk.download('punkt_tab')
nltk.download('stopwords')

def preprocess(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())  # Tokenization and lowercasing
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
    return filtered_words

def build_incidence_matrix(documents):
    processed_docs = [preprocess(doc) for doc in documents]
    vocabulary = sorted(set(word for doc in processed_docs for word in doc))

    incidence_matrix = np.zeros((len(vocabulary), len(documents)), dtype=int)

    for j, doc in enumerate(processed_docs):
        for i, word in enumerate(vocabulary):
            if word in doc:
                incidence_matrix[i, j] = 1

    return pd.DataFrame(incidence_matrix, index=vocabulary, columns=[f'Doc{j+1}' for j in range(len(documents))])

# Example Documents
documents = [
    "The quick brown fox jumps over the lazy dog.",
    "A fast fox and a sleepy dog were in the yard.",
    "Dogs are very loyal animals and love their owners."
]

incidence_matrix_df = build_incidence_matrix(documents)
print(incidence_matrix_df)
