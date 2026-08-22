from candidate_generation.faiss_index import search_faiss
from ranking.features import build_features
from ranking.rank import hybrid_rank
from config_loader import load_config
from decision_layer.constraints import apply_constraints
from decision_layer.post_process import post_process
import uuid

cfg = load_config()

def recommend(movie_name, title_to_index, index_to_title, vectors, faiss_index,popularity_map):
    request_id = str(uuid.uuid4())
    try:

        print(f"[REQUEST START] id={request_id} movie= {movie_name}")

        ## Candidate Generation
        if movie_name not in title_to_index:
            raise ValueError("Movie not Found")
        
        idx = title_to_index[movie_name]
        query_vector = vectors[idx]

        indices, scores = search_faiss(faiss_index, query_vector, cfg)

        candidate_titles = []
        for i,score in zip(indices,scores):
            if i != idx:
                candidate_titles.append((index_to_title[i],float(score)))
        
        print(f'[CANDIDATES]  id={request_id} count = {len(candidate_titles)}')

        if not candidate_titles:
            raise ValueError("No candidates found")

        ## Ranking

        features = build_features(candidate_titles, popularity_map,cfg)
        ranked_titles = hybrid_rank(features,cfg)

        print(
            f"[RANKED] id={request_id} top5="
            f"{[t for t, _ in ranked_titles[:5]]}"
        )

        if not ranked_titles:
            raise ValueError("No ranked titles found")

        ## Decision Layer

        constrained = apply_constraints(ranked_titles, cfg)
        final_output = post_process(
            constrained,
            cfg,
            vectors=vectors,
            title_to_index=title_to_index
        )

        ## Final Layer

        top_k = cfg["candidate_generation"]["final_k"]
        result = final_output[:top_k]
    
        print(f"[REQUEST END] id={request_id} returned={len(result)}")
        return result

    except Exception as e:
        print(f"[REQUEST ERROR] id={request_id} error={str(e)}")
        return []
