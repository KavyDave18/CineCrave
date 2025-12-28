import numpy as np
import pandas as pd
import argparse
from src.faiss_index import load_index
from src.recommender import recommend
from src.personalization import recommend_for_user
from src.config import FAISS_INDEX_PATH, MOVIE_VECTORS_PATH

def main():
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
    rec_parser.add_argument("--k", type=int, default=5)

    # user command
    user_parser = subparsers.add_parser(
        "user",
        help="User-based recommendation"
    )
    user_parser.add_argument("--history", type=str, required=True)

    args = parser.parse_args()

    movies = pd.read_csv("movies_cleaned.csv")

    title_to_index = {
        title: i for i, title in enumerate(movies["original_title"])
    }
    index_to_title = movies["original_title"].tolist()

    popularity_map = dict(
    zip(movies["original_title"], movies["popularity"]))

    vectors = np.load(MOVIE_VECTORS_PATH, allow_pickle=True)
    faiss_index = load_index(FAISS_INDEX_PATH)

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
            faiss_index
        ))

if __name__ == "__main__":
    main()
