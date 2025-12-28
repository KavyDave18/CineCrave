from src.faiss_index import search_faiss
from src.ranking import hybrid_rank
from src.config import TOP_K


def recommend(movie_name, title_to_index, index_to_title, vectors, faiss_index,popularity_map):

    idx = title_to_index[movie_name]
    query_vector = vectors[idx]

    print("QUERY MOVIE:", movie_name)
    print("QUERY INDEX:", idx)

    indices, scores = search_faiss(
        faiss_index,
        query_vector,
        TOP_K + 1
    )


    results = []
    for i, score in zip(indices, scores):
        if i != idx:
            results.append((index_to_title[i]))

    candidates = []

    for i, score in zip(indices, scores):
        if i != idx:
            candidates.append((index_to_title[i], float(score)))

    print("\n--- RAW FAISS OUTPUT ---")
    for t, s in candidates:
        print(t, round(s, 3))


    ranked = hybrid_rank(candidates , popularity_map ,0.85 , 0.1 ,0.05)

    print("\n--- AFTER HYBRID RANKING ---")
    for t, s in ranked:
        print(t, round(s, 3))

    
    return ranked[:TOP_K]
