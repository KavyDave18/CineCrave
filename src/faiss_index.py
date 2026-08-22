import faiss
import numpy as np

def build_faiss_index(vectors):
    faiss.normalize_L2(vectors)
    dim = vectors.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(vectors)
    return index

def save_index(index, path):
    faiss.write_index(index, path)

def load_index(path):
    return faiss.read_index(path)

def search_faiss(index, query_vector, k):
    q = np.array(query_vector, dtype="float32").reshape(1, -1)
    faiss.normalize_L2(q)
    scores, indices = index.search(q, k)
    return indices[0], scores[0]
