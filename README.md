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
The project focuses on understanding how recommendation systems work internally,
including feature engineering, similarity computation, and evaluation of results.
</p>

<hr>

<h2>Problem Statement</h2>
<p>
Finding movies similar to a user’s interest can be challenging without understanding
content similarity. This project aims to recommend relevant movies based purely on
movie metadata, without using user ratings or collaborative filtering.
</p>

<hr>

<h2>Approach</h2>

<h3>1. Data Preprocessing</h3>
<ul>
    <li>Cleaned movie metadata</li>
    <li>Converted text to lowercase and removed unnecessary spaces</li>
    <li>Combined genres, keywords, cast, crew, and overview into a single text feature</li>
</ul>

<h3>2. Feature Engineering</h3>
<ul>
    <li>Used <b>TF-IDF Vectorizer</b> to convert text data into numerical vectors</li>
    <li>TF-IDF reduces the impact of common words and highlights meaningful terms</li>
</ul>

<h3>3. Similarity Computation</h3>
<ul>
    <li>Calculated similarity between movies using <b>cosine similarity</b></li>
    <li>Built a movie-to-movie similarity matrix</li>
</ul>

<h3>4. Recommendation Logic</h3>
<p>
Given a movie title, the system:
</p>
<ol>
    <li>Finds the movie index</li>
    <li>Fetches similarity scores</li>
    <li>Sorts movies by similarity</li>
    <li>Returns the top-N similar movies</li>
</ol>

<hr>

<h2>Project Structure</h2>

<pre>
CineCrave/
│
├── data/
│   └── movies_clean.csv
│
├── notebooks/
│   └── experiments.ipynb
│
├── src/
│   ├── data_preprocessing.py
│   ├── vectorization.py
│   ├── similarity.py
│   └── recommender.py
│
├── main.py
├── requirements.txt
└── README.html
</pre>

<hr>

<h2>Technologies Used</h2>
<ul>
    <li>Python</li>
    <li>Pandas, NumPy</li>
    <li>Scikit-learn (TF-IDF, Cosine Similarity)</li>
</ul>

<hr>

<h2>How to Run</h2>

<pre>
git clone https://github.com/KavyDave18/CineCrave
cd CineCrave
pip install -r requirements.txt
python main.py
</pre>

<hr>

<h2>Example Usage</h2>

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
    <li>Movies with similar genres and themes are grouped correctly</li>
    <li>TF-IDF performs better than simple count-based methods</li>
    <li>System is fast and easy to extend</li>
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
    <li>Use semantic embeddings for better contextual similarity</li>
    <li>Add fuzzy matching for movie titles</li>
    <li>Build a web interface or REST API</li>
</ul>

<hr>

<h2>Key Learning</h2>
<p>
The biggest takeaway from this project is that building a recommendation system
is not just about implementation, but about understanding model behavior,
limitations, and making informed design decisions.
</p>

<hr>

<h2>Conclusion</h2>
<p>
CineCrave represents a solid baseline content-based recommendation system with
clear scope for future improvements. It reflects both technical implementation
and evaluation-driven thinking.
</p>

</body>
</html>
