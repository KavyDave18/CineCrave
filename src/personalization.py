import numpy as np
from candidate_generation.faiss_index import search_faiss
import uuid

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

def recommend_for_user(history , title_to_index , index_to_title , vectors , faiss_index, cfg):
    
    request_id = str(uuid.uuid4())
    user_id = "history_based"

    print(f"[USER REQUEST] id={request_id} user_id={user_id}")

    user_vector = build_user_embeddings(history , title_to_index , vectors)

    indices , scores = search_faiss(faiss_index , user_vector ,  cfg)##k+len(history)

    results = []

    for i in indices:
        title = index_to_title[i]
        if title not in history:
            results.append(title)

    top_k = cfg["candidate_generation"]["faiss_k"]

    print(f"[USER RESULT] id={request_id} count = {len(results)}")
    return results[:top_k]


