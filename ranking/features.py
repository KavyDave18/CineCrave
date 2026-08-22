import numpy as np

def min_max_normalize(scores):
    scores = np.array(scores, dtype=float)
    if scores.max() == scores.min():
        return np.zeros_like(scores)
    return (scores - scores.min()) / (scores.max() - scores.min())


def build_features(candidates, popularity_map, config):
    titles = [c[0] for c in candidates]
    sim_scores = [float(c[1]) for c in candidates]

    pop_scores = [
        float(popularity_map.get(title, 0.0))
        for title in titles
    ]

    nov_scores = [
        1.0 / (np.log1p(pop) + 1.0)
        for pop in pop_scores
    ]

    return {
        "titles": titles,
        "sim_norm": min_max_normalize(sim_scores),
        "pop_norm": min_max_normalize(pop_scores),
        "nov_norm": min_max_normalize(nov_scores),
    }