def hybrid_rank(features,cfg):
    w = cfg["ranking"]["weights"]

    w_sim = w["similarity"]
    w_pop = w["popularity"]
    w_nov = w["novelty"]
    final_scores = (
        w_sim * features["sim_norm"] +
        w_pop * features["pop_norm"] +
        w_nov * features["nov_norm"]
    )

    ranked = list(zip(features["titles"], final_scores))
    ranked.sort(key=lambda x: x[1], reverse=True)
    return ranked
