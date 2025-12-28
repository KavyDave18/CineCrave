<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body>

<h1>CineCrave</h1>

<p>
A content-based movie recommendation system focused on scalable retrieval, ranking,
and qualitative evaluation.
</p>

<hr>

<h2>Overview</h2>

<p>
CineCrave explores how recommender systems are designed when explicit user feedback
and labeled relevance data are unavailable.
The project emphasizes <strong>system architecture, correctness, and evaluation</strong>,
rather than model experimentation.
</p>

<h2>Key Components</h2>

<ul>
  <li>Semantic movie embeddings using Sentence-BERT (all-MiniLM-L6-v2)</li>
  <li>Nearest-neighbor retrieval with FAISS</li>
  <li>User-level personalization via embedding aggregation</li>
  <li>Hybrid ranking (similarity, popularity, novelty)</li>
  <li>Command-line interface for reproducible usage</li>
</ul>

<h2>Architecture</h2>

<pre>
movie metadata
→ embeddings
→ FAISS retrieval
→ hybrid ranking
→ recommendations
</pre>

<p>
The system follows a standard two-stage <strong>retrieve → rank</strong> design.
</p>

<h2>Project Structure</h2>

<pre>
src/        core recommendation logic
data/       processed artifacts
evaluation_report.md
</pre>

<h2>Demo</h2>

<p>Item-based recommendation:</p>
<pre>
python -m src.cli recommend --movie "Titanic"
</pre>

<p>Sample output:</p>
<pre>
Poseidon
All Is Lost
The Reef
Fool's Gold
</pre>

<p>User-based recommendation:</p>
<pre>
python -m src.cli user --history "Interstellar,Inception"
</pre>

<h2>Evaluation</h2>

<p>
This project intentionally avoids accuracy-based metrics due to the absence of labeled
relevance data.
</p>

<p>Evaluation is based on:</p>

<ul>
  <li>Qualitative relevance inspection</li>
  <li>Personalization behavior comparison</li>
  <li>Ranking impact analysis</li>
  <li>Failure-case identification</li>
</ul>

<p>
Detailed evaluation notes are documented in <code>evaluation_report.md</code>.
</p>

<h2>Limitations</h2>

<ul>
  <li>Cold-start users fall back to item-based recommendations</li>
  <li>Sparse metadata affects embedding quality</li>
  <li>Popularity bias requires careful tuning</li>
</ul>

<h2>Future Steps</h2>

<ul>
  <li>Incorporate learning-to-rank models using interaction data</li>
  <li>Add genre-aware and constraint-based re-ranking</li>
  <li>Integrate a vector database for large-scale deployment</li>
  <li>Introduce online evaluation through A/B testing</li>
</ul>

<h2>Notes</h2>

<p>
This project prioritizes clarity and correctness over complexity and is intended as a
system-design–focused implementation of a recommender pipeline.
</p>

</body>
</html>
