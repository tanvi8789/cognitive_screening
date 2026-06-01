import os
import subprocess


def convert_to_wav(input_path):

    # Create output directory
    os.makedirs(
        "processed_audio",
        exist_ok=True
    )

    filename = os.path.splitext(
        os.path.basename(input_path)
    )[0]

    output_path = (
        f"processed_audio/{filename}.wav"
    )

    command = [
        "ffmpeg",
        "-y",
        "-i",
        input_path,
        "-ar",
        "16000",
        "-ac",
        "1",
        output_path
    ]

    subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return output_path

import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:

        print(
            "Usage:\n"
            "python -m src.preprocessing.audio_converter input.mp3"
        )

        sys.exit(1)

    output = convert_to_wav(
        sys.argv[1]
    )

    print(
        f"Converted file saved to:\n{output}"
    )