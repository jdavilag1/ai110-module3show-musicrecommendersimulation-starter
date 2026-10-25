import csv
from typing import List, Dict, Tuple
from dataclasses import dataclass


GENRE_MATCH_POINTS = 1.0
MOOD_MATCH_POINTS = 1.0
MAX_ENERGY_SIMILARITY_POINTS = 2.0
ACOUSTIC_MATCH_POINTS = 0.5


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the highest-scoring songs for a user."""
        if k < 0:
            raise ValueError("k must be non-negative")

        ranked_songs = sorted(
            self.songs,
            key=lambda song: core_song(
                {
                    "genre": user.favorite_genre,
                    "mood": user.favorite_mood,
                    "energy": user.target_energy,
                    "likes_acoustic": user.likes_acoustic,
                },
                {
                    "genre": song.genre,
                    "mood": song.mood,
                    "energy": song.energy,
                    "acousticness": song.acousticness,
                },
            )[0],
            reverse=True,
        )
        return ranked_songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain why a song matches the user's preferences."""
        _, reasons = core_song(
            {
                "genre": user.favorite_genre,
                "mood": user.favorite_mood,
                "energy": user.target_energy,
                "likes_acoustic": user.likes_acoustic,
            },
            {
                "genre": song.genre,
                "mood": song.mood,
                "energy": song.energy,
                "acousticness": song.acousticness,
            },
        )
        return "; ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert numeric fields."""
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        required_fields = {
            "id",
            "title",
            "artist",
            "genre",
            "mood",
            "energy",
            "tempo_bpm",
            "valence",
            "danceability",
            "acousticness",
        }
        missing_fields = required_fields.difference(reader.fieldnames or [])
        if missing_fields:
            raise ValueError(
                f"Song CSV is missing required columns: {', '.join(sorted(missing_fields))}"
            )

        songs = []
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )
        return songs

def core_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song and return its score with matching reasons."""
    score = 0.0
    reasons = []

    genre = str(song["genre"]).strip()
    mood = str(song["mood"]).strip()
    preferred_genre = str(user_prefs["genre"]).strip()
    preferred_mood = str(user_prefs["mood"]).strip()

    if genre.casefold() == preferred_genre.casefold():
        score += GENRE_MATCH_POINTS
        reasons.append(f"genre match (+{GENRE_MATCH_POINTS:.1f})")
    if mood.casefold() == preferred_mood.casefold():
        score += MOOD_MATCH_POINTS
        reasons.append(f"mood match (+{MOOD_MATCH_POINTS:.1f})")

    energy_similarity = max(
        0.0, 1.0 - abs(float(song["energy"]) - float(user_prefs["energy"]))
    )
    energy_points = MAX_ENERGY_SIMILARITY_POINTS * energy_similarity
    score += energy_points
    reasons.append(f"energy similarity (+{energy_points:.2f})")

    if user_prefs.get("likes_acoustic") is not None:
        acousticness = float(song["acousticness"])
        acoustic_match = (acousticness >= 0.5) == bool(user_prefs["likes_acoustic"])
        if acoustic_match:
            score += ACOUSTIC_MATCH_POINTS
            reasons.append(f"acousticness match (+{ACOUSTIC_MATCH_POINTS:.1f})")

    return score, reasons


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Backward-compatible name for the core song scoring function."""
    return core_song(user_prefs, song)


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Rank songs by score and return the top k with explanations."""
    if k < 0:
        raise ValueError("k must be non-negative")

    scored_songs = sorted(
        (
            (song, *score_song(user_prefs, song))
            for song in songs
        ),
        key=lambda item: item[1],
        reverse=True,
    )
    return [
        (song, score, "; ".join(reasons))
        for song, score, reasons in scored_songs[:k]
    ]
