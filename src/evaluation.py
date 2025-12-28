def precision_at_k(recommended, relevant):
    hits = len(set(recommended) & set(relevant))
    return hits / len(recommended)
