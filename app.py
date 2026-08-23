import streamlit as st
import pandas as pd
import numpy as np
from config_loader import load_config
from candidate_generation.faiss_index import load_index
from src.recommender import recommend
from src.personalization import recommend_for_user

# Page Configuration
st.set_page_config(
    page_title="CineCrave — Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium Dark UI
st.markdown("""
<style>
    .main-header {
        font-size: 2.4rem;
        font-weight: 800;
        background: linear-gradient(135deg, #6366f1 0%, #06b6d4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    .sub-header {
        color: #94a3b8;
        font-size: 1.05rem;
        margin-bottom: 25px;
    }
    .movie-card {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 18px 20px;
        margin-bottom: 14px;
        transition: transform 0.2s;
    }
    .movie-card:hover {
        border-color: #6366f1;
        transform: translateY(-2px);
    }
    .score-badge {
        background: rgba(99, 102, 241, 0.18);
        color: #a5b4fc;
        padding: 4px 10px;
        border-radius: 6px;
        font-weight: 700;
        font-size: 0.85rem;
        border: 1px solid rgba(99, 102, 241, 0.3);
    }
    .genre-tag {
        background: rgba(6, 182, 212, 0.12);
        color: #67e8f9;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 0.75rem;
        margin-right: 6px;
    }
</style>
""", unsafe_allow_html=True)

# Load Data & Index with Cache
@st.cache_resource
def load_system():
    cfg = load_config()
    movies = pd.read_csv(cfg["paths"]["data_dir"] + "movies_cleaned.csv")
    title_to_index = {t: i for i, t in enumerate(movies["original_title"])}
    index_to_title = movies["original_title"].tolist()
    pop_map = dict(zip(movies["original_title"], movies["popularity"]))
    vectors = np.load(cfg["paths"]["movie_vectors"], allow_pickle=True)
    faiss_index = load_index(cfg["paths"]["faiss_index"])
    return cfg, movies, title_to_index, index_to_title, pop_map, vectors, faiss_index

cfg, movies, title_to_index, index_to_title, pop_map, vectors, faiss_index = load_system()

# Header
st.markdown('<div class="main-header">🎬 CineCrave</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Production-Grade Two-Stage Retrieve & Rank Movie Recommender System</div>', unsafe_allow_html=True)

# Sidebar Controls
st.sidebar.header("⚙️ Hyperparameters")

mode = st.sidebar.radio("Recommendation Mode", ["🎯 Item-Based", "👤 User History Profile"])

st.sidebar.subheader("Ranking & Diversity Weights")
w_sim = st.sidebar.slider("Similarity Weight (w_sim)", 0.0, 1.0, float(cfg["ranking"]["weights"]["similarity"]), 0.05)
w_pop = st.sidebar.slider("Popularity Weight (w_pop)", 0.0, 0.5, float(cfg["ranking"]["weights"]["popularity"]), 0.05)
w_nov = st.sidebar.slider("Novelty Weight (w_nov)", 0.0, 0.5, float(cfg["ranking"]["weights"]["novelty"]), 0.05)

st.sidebar.subheader("Decision Layer (MMR)")
use_mmr = st.sidebar.toggle("Enable MMR Diversity", value=cfg["decision_layer"].get("use_mmr", True))
diversity_lambda = st.sidebar.slider("Diversity Lambda (λ)", 0.1, 1.0, float(cfg["decision_layer"].get("diversity_lambda", 0.7)), 0.05,
                                    help="1.0 = Pure relevance, 0.0 = Maximal diversity")

top_k = st.sidebar.slider("Results Count", 5, 20, int(cfg["candidate_generation"].get("final_k", 10)))

# Apply Dynamic Config Updates
runtime_cfg = dict(cfg)
runtime_cfg["ranking"] = {"weights": {"similarity": w_sim, "popularity": w_pop, "novelty": w_nov}}
runtime_cfg["decision_layer"] = {"use_mmr": use_mmr, "diversity_lambda": diversity_lambda}
runtime_cfg["candidate_generation"]["final_k"] = top_k

# Main Content Area
if mode == "🎯 Item-Based":
    all_titles = movies["original_title"].tolist()
    
    col1, col2 = st.columns([3, 1])
    with col1:
        default_idx = all_titles.index("The Dark Knight") if "The Dark Knight" in all_titles else 0
        selected_movie = st.selectbox("Search or Select a Movie:", all_titles, index=default_idx)
    with col2:
        st.write("")
        st.write("")
        generate_btn = st.button("🚀 Recommend Similar", type="primary", use_container_width=True)

    if selected_movie:
        # Show Selected Movie Metadata
        movie_row = movies[movies["original_title"] == selected_movie].iloc[0]
        with st.expander("ℹ️ Query Movie Details", expanded=False):
            st.markdown(f"**Genres:** {movie_row.get('genres', 'N/A')}")
            st.markdown(f"**Director:** {movie_row.get('director', 'N/A')} | **Cast:** {movie_row.get('cast', 'N/A')}")
            st.markdown(f"**Overview:** {movie_row.get('overview', 'N/A')}")
            st.markdown(f"**Popularity:** `{movie_row.get('popularity', 0.0):.2f}`")

        results = recommend(selected_movie, title_to_index, index_to_title, vectors, faiss_index, pop_map, cfg_override=runtime_cfg)
        
        st.subheader(f"Top {len(results)} Recommendations for **{selected_movie}**")
        
        for rank, (title, score) in enumerate(results, 1):
            item_row = movies[movies["original_title"] == title].iloc[0]
            genres = str(item_row.get("genres", "")).split()
            genre_badges = "".join([f'<span class="genre-tag">{g.capitalize()}</span>' for g in genres[:4]])
            
            with st.container():
                st.markdown(f"""
                <div class="movie-card">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <h4 style="margin: 0; color: #f8fafc;">#{rank}. {title}</h4>
                        <span class="score-badge">Match: {score:.3f}</span>
                    </div>
                    <div style="margin-bottom: 8px;">{genre_badges}</div>
                    <p style="font-size: 0.88rem; color: #94a3b8; margin: 0;">
                        <strong>Director:</strong> {item_row.get('director', 'N/A')} &nbsp;|&nbsp; 
                        <strong>Cast:</strong> {str(item_row.get('cast', 'N/A'))[:50]}... &nbsp;|&nbsp;
                        <strong>Popularity:</strong> {item_row.get('popularity', 0.0):.1f}
                    </p>
                </div>
                """, unsafe_allow_html=True)

elif mode == "👤 User History Profile":
    st.subheader("Personalized Recommendations from Watch History")
    all_titles = movies["original_title"].tolist()
    
    default_history = ["Interstellar", "Inception"] if "Interstellar" in all_titles and "Inception" in all_titles else [all_titles[0]]
    user_history = st.multiselect("Select movies you have watched:", all_titles, default=default_history)
    
    if user_history:
        results = recommend_for_user(user_history, title_to_index, index_to_title, vectors, faiss_index, runtime_cfg)
        
        st.subheader(f"Personalized Recommendations ({len(results)} Movies):")
        
        for rank, title in enumerate(results[:top_k], 1):
            item_row = movies[movies["original_title"] == title].iloc[0]
            genres = str(item_row.get("genres", "")).split()
            genre_badges = "".join([f'<span class="genre-tag">{g.capitalize()}</span>' for g in genres[:4]])
            
            with st.container():
                st.markdown(f"""
                <div class="movie-card">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <h4 style="margin: 0; color: #f8fafc;">#{rank}. {title}</h4>
                    </div>
                    <div style="margin-bottom: 8px;">{genre_badges}</div>
                    <p style="font-size: 0.88rem; color: #94a3b8; margin: 0;">
                        <strong>Director:</strong> {item_row.get('director', 'N/A')} &nbsp;|&nbsp; 
                        <strong>Popularity:</strong> {item_row.get('popularity', 0.0):.1f}
                    </p>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info("Please select at least 1 movie in your history.")
