<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <!-- <title>Movie Recommendation System – FAANG-Style ML Engineering</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
            line-height: 1.6;
            margin: 40px;
            color: #222;
        }
        h1, h2, h3 {
            color: #0a3d62;
        }
        h1 {
            border-bottom: 2px solid #0a3d62;
            padding-bottom: 10px;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 0.95em;
        }
        pre {
            background-color: #f4f4f4;
            padding: 12px;
            border-radius: 6px;
            overflow-x: auto;
        }
        ul {
            margin-left: 20px;
        }
        .highlight {
            background-color: #eef6ff;
            padding: 12px;
            border-left: 4px solid #0a3d62;
            margin: 20px 0;
        }
        .section {
            margin-bottom: 40px;
        }
    </style> -->
</head>
<body>

<h1>🎬 Movie Recommendation System (FAANG-Style ML Engineering)</h1>

<div class="section">
    <h2>Overview</h2>
    <p>
        This project implements a <strong>content-based movie recommendation system</strong> that
        evolves from a <strong>TF-IDF baseline</strong> to a <strong>scalable, semantic,
        embedding-based recommender</strong> using <strong>Sentence-BERT</strong> and
        <strong>FAISS (Approximate Nearest Neighbors)</strong>.
    </p>
    <p>
        The emphasis is on <strong>engineering correctness, scalability, and design trade-offs</strong>,
        not UI or surface-level features.
    </p>
</div>

<div class="section">
    <h2>Why This Project Matters</h2>
    <ul>
        <li>Clear baseline → upgraded system evolution</li>
        <li>Semantic understanding using dense embeddings</li>
        <li>Scalable retrieval using FAISS (ANN)</li>
        <li>Offline vs online computation separation</li>
        <li>Clean, modular <code>.py</code> codebase</li>
        <li>CLI interface (no notebook dependency)</li>
        <li>Documented failure cases and trade-offs</li>
    </ul>
</div>

<div class="section">
    <h2>Problem Statement</h2>
    <p>
        Given a movie title, recommend the <strong>top-N most similar movies</strong> based on
        <strong>semantic similarity of content</strong> (genres, overview, keywords, cast, crew),
        rather than exact keyword overlap.
    </p>
</div>

<div class="section">
    <h2>System Evolution</h2>

    <h3>1️⃣ Baseline — TF-IDF + Cosine Similarity</h3>
    <ul>
        <li>Combined textual features into a single <code>tags</code> field</li>
        <li>Vectorized using TF-IDF</li>
        <li>Used cosine similarity for recommendations</li>
    </ul>
    <p><strong>Limitations:</strong></p>
    <ul>
        <li>Keyword-dependent (no semantic understanding)</li>
        <li>Fails on paraphrases and synonyms</li>
        <li>Sparse vectors → high memory usage</li>
        <li>Poor scalability</li>
    </ul>

    <h3>2️⃣ Upgraded System — Semantic Embeddings</h3>
    <ul>
        <li>Used Sentence-BERT (MiniLM)</li>
        <li>Each movie mapped to a 384-dimensional dense vector</li>
        <li>Embeddings generated once offline and cached</li>
        <li>Cosine similarity used for semantic matching</li>
    </ul>

    <h3>3️⃣ Scalable Retrieval — FAISS (ANN)</h3>
    <ul>
        <li>Brute-force cosine similarity replaced with FAISS</li>
        <li>Normalized embeddings + inner product search</li>
        <li>FAISS as primary retrieval, brute-force as fallback</li>
    </ul>
</div>

<div class="section">
    <h2>Architecture Overview</h2>
    <pre>
Movie Text (tags)
        ↓
Sentence-BERT (MiniLM)
        ↓
Dense Embeddings (384-D)
        ↓
FAISS ANN Index
        ↓
Top-K Similar Movies
    </pre>
    <p>
        <strong>Offline:</strong> text processing, embedding generation, index building<br>
        <strong>Online:</strong> query embedding, ANN search, result mapping
    </p>
</div>

<div class="section">
    <h2>Project Structure</h2>
    <pre>
src/
 ├── embeddings.py
 ├── faiss_index.py
 ├── recommender.py
 ├── config.py
 ├── cli.py
 ├── evaluation.py
 └── utils.py
    </pre>
</div>

<div class="section">
    <h2>CLI Usage</h2>
    <pre>
python cli.py recommend --movie "Avatar" --top_k 5
    </pre>
    <p>
        Features include case-insensitive input handling and graceful error responses.
    </p>
</div>

<div class="section">
    <h2>Evaluation Strategy</h2>
    <p>
        This is an <strong>unsupervised system</strong>; traditional accuracy metrics are misleading.
        Evaluation focuses on:
    </p>
    <ul>
        <li>Manual relevance checks</li>
        <li>TF-IDF vs embedding output comparison</li>
        <li>Semantic coherence of recommendations</li>
        <li>Failure case analysis</li>
    </ul>
</div>

<div class="section">
    <h2>Known Failure Cases</h2>
    <ul>
        <li>Very short or vague descriptions</li>
        <li>Rare or domain-specific terms</li>
        <li>Similarity does not equal personalization</li>
    </ul>
</div>

<div class="section">
    <h2>Key Engineering Decisions</h2>
    <ul>
        <li><strong>Embeddings over TF-IDF:</strong> semantic understanding and scalability</li>
        <li><strong>Cosine similarity:</strong> direction-based similarity for embeddings</li>
        <li><strong>FAISS:</strong> scalable ANN search for large datasets</li>
        <li><strong>No UI:</strong> focus on system correctness</li>
        <li><strong>Caching:</strong> offline computation, fast online inference</li>
    </ul>
</div>

<div class="section">
    <h2>Future Work</h2>
    <ul>
        <li>User-level personalization</li>
        <li>Hybrid ranking (similarity + popularity + novelty)</li>
        <li>Incremental updates for new movies</li>
        <li>Vector database integration</li>
        <li>API layer for deployment</li>
    </ul>
</div>

<div class="section">
    <h2>Tech Stack</h2>
    <ul>
        <li>Python</li>
        <li>Sentence-Transformers (MiniLM)</li>
        <li>FAISS (ANN)</li>
        <li>NumPy, scikit-learn</li>
        <li>Pickle for artifact storage</li>
    </ul>
</div>

<div class="highlight">
    <strong>Resume One-Liner:</strong><br>
    Built a scalable, embedding-based movie recommender system using Sentence-BERT and FAISS,
    demonstrating semantic similarity search, ANN optimization, and clean ML pipeline design.
</div>

</body>
</html>
