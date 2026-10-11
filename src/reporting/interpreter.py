import json
from src.config import load_config

def interpret_profile(profile):
    """Generate human‑readable observations based on the profile.
    Thresholds are loaded from ``config.yaml`` so they can be tuned without
    touching code.
    """
    config = load_config()
    silence_cfg = config.get("silence_thresholds", {"low": 10, "moderate": 25})
    low_thr = silence_cfg.get("low", 10)
    mod_thr = silence_cfg.get("moderate", 25)

    observations = []
    temporal = profile["temporal"]
    fluency = profile["fluency"]
    semantic = profile["semantic"]
    language = profile["language"]

    # Silence
    silence = temporal["silence_percentage"]
    if silence > mod_thr:
        observations.append("Elevated silence percentage observed.")
    elif silence > low_thr:
        observations.append("Moderate silence percentage observed.")
    else:
        observations.append("Low silence percentage observed.")

    # Pauses
    if temporal["pause_count"] > 15:
        observations.append("Frequent pauses detected.")

    # Words per minute
    wpm = fluency["words_per_minute"]
    if wpm > 170:
        observations.append("Speech rate is relatively fast.")
    elif wpm > 120:
        observations.append("Speech rate is within expected range.")
    else:
        observations.append("Reduced speech rate detected.")

    # Topic consistency
    score = semantic["topic_consistency_score"]
    if score >= 70:
        observations.append("Strong topic consistency.")
    elif score >= 55:
        observations.append("Moderate topic consistency.")
    else:
        observations.append("Reduced topic consistency.")

    # Vocabulary diversity
    diversity = language["lexical_diversity"]
    if diversity > 0.75:
        observations.append("High vocabulary diversity.")
    elif diversity > 0.55:
        observations.append("Moderate vocabulary diversity.")
    else:
        observations.append("Limited vocabulary diversity.")

    return observations