"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    """Load the catalog and print the top recommendations."""
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations (genre=pop, mood=happy, energy=0.8):")
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"{rank}. {song['title']} - Score: {score:.2f}")
        print(f"   Reasons: {explanation}")


if __name__ == "__main__":
    main()
