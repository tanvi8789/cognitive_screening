def analyze_speech_rate(
    transcript,
    temporal_features
):

    words = transcript.split()

    word_count = len(words)

    speaking_time = (
        temporal_features[
            "speaking_time"
        ]
    )

    audio_duration = (
        temporal_features[
            "audio_duration"
        ]
    )

    if speaking_time <= 0:

        wpm = 0

    else:

        wpm = (
            word_count
            / speaking_time
        ) * 60

    speaking_ratio = (

        speaking_time
        / audio_duration

    ) * 100

    return {

        "word_count":
            word_count,

        "words_per_minute":
            round(wpm, 2),

        "speaking_ratio":
            round(
                speaking_ratio,
                2
            )
    }