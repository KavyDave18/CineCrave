from sentence_transformers import SentenceTransformer
import numpy as np
from src.config import EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)

def generate_embeddings(texts):
    embeddings = model.encode(
        texts,
        show_progress_bar=True
    )
    return np.array(embeddings, dtype="float32")
