import numpy as np
from src.faiss_index import search_faiss

def build_user_embeddings(history , title_to_index , vectors):
    indices= [
        title_to_index[movie]
        for movie in history
        if movie in title_to_index
    ]

    if not indices:
        raise ValueError("User history has no valid movies")

    user_vector = vectors[indices].mean(axis=0)

    return user_vector

def recommend_for_user(history , title_to_index , index_to_title , vectors , faiss_index, k=5):
    
    user_vector = build_user_embeddings(history , title_to_index , vectors)

    indices , socres = search_faiss(faiss_index , user_vector , k + len(history))

    results = []

    for i in indices:
        title = index_to_title[i]
        if title not in history:
            results.append(title)

    return results[:k]


