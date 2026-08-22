import numpy as np


def maximal_marginal_relevance(
    ranked_candidates,
    vectors,
    title_to_index,
    top_k,
    lambda_param
):
    if not ranked_candidates:
        return []

    valid_candidates = [
        (title, score)
        for title, score in ranked_candidates
        if title in title_to_index
    ]

    if not valid_candidates:
        return ranked_candidates[:top_k]

    selected = [valid_candidates[0]]
    remaining = valid_candidates[1:]

    selected_indices = [
        title_to_index[valid_candidates[0][0]]
    ]

    while len(selected) < top_k and remaining:

        selected_vectors = vectors[selected_indices]

        best_score = -float("inf")
        best_position = -1

        for i, (title, relevance) in enumerate(remaining):

            candidate_index = title_to_index[title]
            candidate_vector = vectors[candidate_index]

            similarities = np.dot(
                selected_vectors,
                candidate_vector
            )

            redundancy = float(np.max(similarities))

            mmr_score = (
                lambda_param * relevance
                - (1 - lambda_param) * redundancy
            )

            if mmr_score > best_score:
                best_score = mmr_score
                best_position = i

        selected_item = remaining.pop(best_position)

        selected.append(selected_item)

        selected_indices.append(
            title_to_index[selected_item[0]]
        )

    return selected


def post_process(
    ranked_items,
    cfg,
    vectors=None,
    title_to_index=None
):
    decision_cfg = cfg.get("decision_layer", {})

    use_mmr = decision_cfg.get("use_mmr", False)

    final_k = cfg["candidate_generation"].get(
        "final_k", 10
    )

    lambda_param = decision_cfg.get(
        "diversity_lambda", 0.7
    )

    if (
        use_mmr
        and vectors is not None
        and title_to_index is not None
    ):
        return maximal_marginal_relevance(
            ranked_items,
            vectors,
            title_to_index,
            final_k,
            lambda_param
        )

    return ranked_items[:final_k]