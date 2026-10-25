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

    profiles = {
        "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.95},
        "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.40},
        "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.90},
        "Edge Case - Conflicting Metal": {
            "genre": "metal",
            "mood": "chill",
            "energy": 0.10,
        },
    }

    for profile_name, user_prefs in profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print(
            f"\n{profile_name} "
            f"(genre={user_prefs['genre']}, mood={user_prefs['mood']}, "
            f"energy={user_prefs['energy']:.2f}):"
        )
        for rank, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"{rank}. {song['title']} - Score: {score:.2f}")
            print(f"   Reasons: {explanation}")


if __name__ == "__main__":
    main()
