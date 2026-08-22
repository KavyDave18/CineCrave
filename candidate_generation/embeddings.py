from sentence_transformers import SentenceTransformer
import numpy as np

def generate_embeddings(texts,cfg):
    model_name = cfg["model"]["embedding_model"]
    model = SentenceTransformer(model_name)
    embeddings = model.encode(
        texts,
        show_progress_bar=True
    )
    return np.array(embeddings, dtype="float32")
