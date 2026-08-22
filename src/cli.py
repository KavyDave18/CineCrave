import numpy as np
import pandas as pd
import argparse
from candidate_generation.faiss_index import load_index
from src.recommender import recommend
from src.personalization import recommend_for_user
from config_loader import load_config

def main():
    cfg = load_config()
    parser = argparse.ArgumentParser(
        description="Movie Recommendation System CLI"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    # recommend command
    rec_parser = subparsers.add_parser(
        "recommend",
        help="Recommend similar movies"
    )
    rec_parser.add_argument("--movie", type=str, required=True)

    # user command
    user_parser = subparsers.add_parser(
        "user",
        help="User-based recommendation"
    )
    user_parser.add_argument("--history", type=str, required=True)

    args = parser.parse_args()

    movies = pd.read_csv(cfg["paths"]["data_dir"]+ "movies_cleaned.csv")

    title_to_index = {
        title: i for i, title in enumerate(movies["original_title"])
    }
    index_to_title = movies["original_title"].tolist()

    if "popularity" in movies.columns:
        popularity = movies["popularity"].tolist()
    else:
        popularity = [0] * len(movies)

    popularity_map = dict(
        zip(movies["original_title"], popularity)
    )

    vectors = np.load(cfg["paths"]["movie_vectors"], allow_pickle=True)
    faiss_index = load_index(cfg["paths"]["faiss_index"])

    if args.command == "recommend":
        if args.movie not in title_to_index:
            raise ValueError("Movie not Found")
        print(recommend(
            args.movie,
            title_to_index,
            index_to_title,
            vectors,
            faiss_index,
            popularity_map
        ))
    
    elif args.command == "user":
        history = [title.strip() for title in args.history.split(",")]
        print(recommend_for_user(
            history,
            title_to_index,
            index_to_title,
            vectors,
            faiss_index,
            cfg
        ))

if __name__ == "__main__":
    main()
