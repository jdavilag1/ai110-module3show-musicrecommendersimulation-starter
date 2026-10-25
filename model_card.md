# Model Card: VibeFinder

## 1. Model Name

**VibeFinder** is a small music recommendation simulation.

## 2. Goal / Task

VibeFinder ranks songs for a listener. It uses the listener's favorite genre, mood, and energy level to suggest the top songs.

## 3. Data Used

The catalog has 18 songs. Each song has a genre, mood, energy, tempo, valence, danceability, and acousticness. The catalog is small, and most genres have only one song. It does not include every style of music or every part of a person's taste.

## 4. Algorithm Summary

The recommender gives **1 point** for a genre match and **1 point** for a mood match. Energy can earn up to **2 points**: the closer the song's energy is to the listener's target, the more points it gets. An optional acoustic preference can add **0.5 point**. The songs with the highest total scores are listed first.

## 5. Observed Behavior / Biases

Gym Hero can appear for someone who wants happy pop because it matches pop and has high energy, even though its mood is intense. Energy is worth more than genre or mood in the current experiment, so energetic songs can rank well without matching the listener's other preferences. The catalog is small and has few songs for many genres, so some listeners have fewer good choices. The system also checks exact genre and mood labels, so it can miss songs that are similar but labeled differently.

## 6. Evaluation Process

I tested four profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and Conflicting Metal (metal genre, chill mood, low energy). I also tested a weight change: genre went from 2 points to 1, and energy went from a maximum of 1 point to 2. I compared the top five songs and checked their scores and reasons.

High-Energy Pop and Chill Lofi gave different results. Sunrise City and Gym Hero ranked high for pop, while Midnight Coding and Library Rain ranked high for lofi. This makes sense because their genres, moods, and energy levels fit the different profiles.

High-Energy Pop and Deep Intense Rock both included Gym Hero. It matched pop and high energy for the first profile, and intense mood and high energy for the second. Sunrise City ranked higher for pop, while Storm Runner ranked higher for rock, because each matched more of its profile.

High-Energy Pop and Conflicting Metal preferred different energy levels. Energetic songs appeared in the pop list, while calmer songs led the conflicting profile. This fits the low energy and chill mood requested by that profile.

Chill Lofi and Deep Intense Rock also had different leaders: lofi songs led for the chill profile, while Storm Runner led for rock. Their genre, mood, and energy preferences point to different songs.

Chill Lofi and Conflicting Metal both favored some chill songs. The lofi profile placed lofi songs first because it matched their genre, while the conflicting profile put Spacewalk Thoughts first because of its calm mood and low energy.

Deep Intense Rock and Conflicting Metal had different leaders. Storm Runner matched the rock and intense preferences; Spacewalk Thoughts better matched the conflicting profile's chill mood and low energy.

The weight change made Spacewalk Thoughts beat Heavy Weather for the Conflicting Metal profile. That seems more fitting for its chill mood and low energy, but it only shows that the results changed for this example. It does not prove the system is more accurate for everyone.

## 7. Intended Use and Non-Intended Use

This project is for learning how a simple recommender scores and ranks songs. It is not meant to make serious or personalized recommendations for real music listeners. It does not learn from listening history, understand songs, or know whether someone will actually enjoy a track.

## 8. Ideas for Improvement

- Add more songs and include more examples from each genre.
- Use related genre and mood labels instead of requiring exact matches.
- Add a variety rule so one kind of song does not take over the whole list.

## 9. Personal Reflection

My biggest learning moment was seeing how changing a few point values changed the rankings. The AI assistant helped me write and test the code, but I needed to run it and check the scores so the README and model card matched the real output. I was surprised that a simple score can feel like a recommendation when it gives a clear reason for each result. If I kept working on this, I would add more songs and try to make the recommendations more varied.
