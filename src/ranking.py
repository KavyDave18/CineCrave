import numpy as np

def min_max_normalize(scores):
    scores = np.array(scores)
    if scores.max() == scores.min():
        return np.ones_like(scores)
    return (scores - scores.min())/(scores.max()-scores.min())

def hybrid_rank(candidates , popularity_map , w_sim = 0.85 , w_pop = 0.1 , w_nov = 0.05):
    titles = [c[0] for c in candidates]
    sim_scores = [float(c[1]) for c in candidates]

    pop_scores = [popularity_map.get(title, 0) for title in titles]
    nov_scores = [1 / (pop + 1) for pop in pop_scores]

    sim_norm = min_max_normalize(sim_scores)
    pop_norm = min_max_normalize(pop_scores)
    nov_norm = min_max_normalize(nov_scores)

    final_scores = (
        w_sim * sim_norm +
        w_pop * pop_norm +
        w_nov * nov_norm
    )

    ranked = list(zip(titles, final_scores))
    ranked.sort(key=lambda x: x[1], reverse=True)
    return ranked


