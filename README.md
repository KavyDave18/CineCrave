<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CineCrave – Movie Recommendation System</title>
</head>
<body>

<h1>🎬 CineCrave – Movie Recommendation System</h1>

<h2>Overview</h2>
<p>
CineCrave is a <b>content-based movie recommendation system</b> built using Python.
It recommends movies based on similarity in content such as genres, keywords,
cast, crew, and overview text.
</p>

<p>
The project is implemented using <b>Jupyter notebooks</b> to clearly demonstrate
each stage of the recommendation pipeline, including feature engineering,
similarity computation, and evaluation.
</p>

<hr>

<h2>Problem Statement</h2>
<p>
Users often find it difficult to discover movies similar to the ones they like.
This project aims to recommend relevant movies using movie metadata alone,
without relying on user ratings or collaborative filtering.
</p>

<hr>

<h2>Approach</h2>

<h3>1. Data Preprocessing</h3>
<ul>
    <li>Cleaned and filtered movie metadata</li>
    <li>Converted text to lowercase and removed unnecessary spaces</li>
    <li>Combined genres, keywords, cast, crew, and overview into a single text feature</li>
</ul>

<h3>2. Feature Engineering</h3>
<ul>
    <li>Used <b>TF-IDF Vectorizer</b> to convert text data into numerical vectors</li>
    <li>TF-IDF helps reduce the influence of common terms and highlight meaningful words</li>
</ul>

<h3>3. Similarity Computation</h3>
<ul>
    <li>Computed movie similarity using <b>cosine similarity</b></li>
    <li>Generated a movie-to-movie similarity matrix</li>
</ul>

<h3>4. Recommendation Logic</h3>
<p>
Given a movie title, the system:
</p>
<ol>
    <li>Identifies the corresponding movie index</li>
    <li>Retrieves similarity scores</li>
    <li>Sorts movies based on similarity</li>
    <li>Returns the top-N most similar movies</li>
</ol>

<hr>

<h2>Technologies Used</h2>
<ul>
    <li>Python</li>
    <li>Pandas, NumPy</li>
    <li>Scikit-learn (TF-IDF Vectorizer, Cosine Similarity)</li>
</ul>

<hr>

<h2>Example</h2>

<pre>
recommend("Avatar", top_n=5)
</pre>

<p>Sample Output:</p>

<pre>
['Pirates of the Caribbean: At World's End',
 'John Carter',
 'Spectre',
 'The Dark Knight Rises',
 'Spider-Man 3']
</pre>

<hr>

<h2>Evaluation & Observations</h2>

<h3>What Works Well</h3>
<ul>
    <li>Movies with similar genres and themes are recommended correctly</li>
    <li>TF-IDF performs better than basic count-based methods</li>
    <li>The system is simple, fast, and easy to extend</li>
</ul>

<h3>Limitations</h3>
<ul>
    <li>No true semantic understanding of text</li>
    <li>Synonyms are treated as different words</li>
    <li>Context and narrative meaning are not captured</li>
</ul>

<hr>

<h2>Future Improvements</h2>
<ul>
    <li>Use semantic embeddings for deeper contextual similarity</li>
    <li>Add fuzzy matching for movie titles</li>
    <li>Build a web interface or REST API</li>
</ul>

<hr>

<h2>Key Learning</h2>
<p>
This project reinforced that building a recommendation system is not only about
writing code, but also about evaluating results, understanding limitations, and
making informed design decisions.
</p>

<hr>

<h2>Conclusion</h2>
<p>
CineCrave represents a solid baseline content-based recommendation system built
for learning and experimentation, with a clear path for future improvements.
</p>

</body>
</html>
