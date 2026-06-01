import os
import sys
import json

import librosa

from src.cognitive_features.transcribe import (
    transcribe_audio
)

from src.cognitive_features.temporal_analysis import (
    analyze_pauses
)

from src.cognitive_features.speech_rate import (
    analyze_speech_rate
)

from src.cognitive_features.transcript_analysis import (
    analyze_transcript
)

from src.cognitive_features.semantic_analysis import (
    analyze_semantics
)


def generate_profile(audio_path):

    print("Loading audio...")

    audio, sr = librosa.load(
        audio_path,
        sr=None
    )

    print("Generating transcript...")

    transcript = transcribe_audio(
        audio_path
    )

    print("Analyzing temporal features...")

    temporal = analyze_pauses(
        audio,
        sr
    )

    print("Analyzing fluency...")

    fluency = analyze_speech_rate(
        transcript,
        temporal
    )

    print("Analyzing language...")

    language = analyze_transcript(
        transcript
    )

    print("Analyzing semantics...")

    semantic = analyze_semantics(
        transcript
    )

    profile = {

        "transcript":
            transcript,

        "temporal":
            temporal,

        "fluency":
            fluency,

        "language":
            language,

        "semantic":
            semantic
    }

    return profile


def save_profile(profile):

    os.makedirs(
        "output",
        exist_ok=True
    )

    with open(
        "output/profile.json",
        "w"
    ) as f:

        json.dump(
            profile,
            f,
            indent=4
        )


def print_profile(profile):

    print(
        "\n===== COGNITIVE COMMUNICATION PROFILE =====\n"
    )

    print(
        "TRANSCRIPT\n"
        "----------"
    )

    print(
        profile["transcript"]
    )

    print(
        "\nTEMPORAL\n"
        "--------"
    )

    for k, v in profile["temporal"].items():

        print(
            f"{k}: {v}"
        )

    print(
        "\nFLUENCY\n"
        "-------"
    )

    for k, v in profile["fluency"].items():

        print(
            f"{k}: {v}"
        )

    print(
        "\nLANGUAGE\n"
        "--------"
    )

    for k, v in profile["language"].items():

        print(
            f"{k}: {v}"
        )

    print(
        "\nSEMANTIC\n"
        "--------"
    )

    for k, v in profile["semantic"].items():

        print(
            f"{k}: {v}"
        )


if __name__ == "__main__":

    if len(sys.argv) != 2:

        print(
            "Usage:\n"
            "python -m src.cognitive_features.profile_generator audio.wav"
        )

        sys.exit(1)

    audio_path = sys.argv[1]

    profile = generate_profile(
        audio_path
    )

    print_profile(
        profile
    )

    save_profile(
        profile
    )

    print(
        "\nProfile saved:"
    )

    print(
        "output/profile.json"
    )