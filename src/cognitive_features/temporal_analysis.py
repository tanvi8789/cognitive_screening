import numpy as np
import librosa


def analyze_pauses(
    audio,
    sr,
    top_db=30,
    min_pause_duration=0.20
):

    duration = len(audio) / sr

    intervals = librosa.effects.split(
        audio,
        top_db=top_db
    )

    pauses = []

    for i in range(len(intervals) - 1):

        pause_samples = (
            intervals[i + 1][0]
            - intervals[i][1]
        )

        pause_seconds = pause_samples / sr

        if pause_seconds >= min_pause_duration:

            pauses.append(pause_seconds)

    total_pause_time = sum(pauses)

    speaking_time = (
        duration - total_pause_time
    )

    return {

        "audio_duration":
            round(duration, 2),

        "speaking_time":
            round(speaking_time, 2),

        "pause_count":
            len(pauses),

        "average_pause_duration":
            round(
                np.mean(pauses),
                3
            ) if pauses else 0,

        "longest_pause":
            round(
                max(pauses),
                3
            ) if pauses else 0,

        "total_pause_time":
            round(
                total_pause_time,
                3
            ),

        "silence_percentage":
            round(
                (
                    total_pause_time
                    / duration
                ) * 100,
                2
            )
            if duration > 0 else 0
    }