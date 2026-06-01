def interpret_profile(profile):

    observations = []

    temporal = profile["temporal"]
    fluency = profile["fluency"]
    semantic = profile["semantic"]
    language = profile["language"]

    # Silence

    if temporal["silence_percentage"] > 25:

        observations.append(
            "Elevated silence percentage observed."
        )

    elif temporal["silence_percentage"] > 10:

        observations.append(
            "Moderate silence percentage observed."
        )

    # Pauses

    if temporal["pause_count"] > 15:

        observations.append(
            "Frequent pauses detected."
        )

    # WPM

    wpm = fluency["words_per_minute"]

    if wpm > 170:

        observations.append(
            "Speech rate is relatively fast."
        )

    elif wpm > 120:

        observations.append(
            "Speech rate is within expected range."
        )

    else:

        observations.append(
            "Reduced speech rate detected."
        )

    # Topic Consistency

    score = semantic[
        "topic_consistency_score"
    ]

    if score >= 70:

        observations.append(
            "Strong topic consistency."
        )

    elif score >= 55:

        observations.append(
            "Moderate topic consistency."
        )

    else:

        observations.append(
            "Reduced topic consistency."
        )

    # Vocabulary

    diversity = language[
        "lexical_diversity"
    ]

    if diversity > 0.75:

        observations.append(
            "High vocabulary diversity."
        )

    elif diversity > 0.55:

        observations.append(
            "Moderate vocabulary diversity."
        )

    else:

        observations.append(
            "Limited vocabulary diversity."
        )

    return observations