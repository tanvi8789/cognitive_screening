import os
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt


# emotion mapping
emotions = {
    "01": "neutral",
    "02": "calm",
    "03": "happy",
    "04": "sad",
    "05": "angry",
    "06": "fearful",
    "07": "disgust",
    "08": "surprised"
}


# paths
dataset_path = "datasets/ravdess"
output_path = "spectrograms"


# create output folders
for emotion in emotions.values():
    os.makedirs(
        os.path.join(output_path, emotion),
        exist_ok=True
    )


# loop through dataset
for root, dirs, files in os.walk(dataset_path):

    for file in files:

        if file.endswith(".wav"):

            file_path = os.path.join(root, file)

            # extract emotion label
            emotion_code = file.split("-")[2]

            emotion = emotions[emotion_code]

            print(f"Processing: {file}")

            # load audio
            audio, sample_rate = librosa.load(
                file_path,
                sr=22050
            )

            # create Mel spectrogram
            mel_spec = librosa.feature.melspectrogram(
                y=audio,
                sr=sample_rate,
                n_mels=128
            )

            # convert to dB
            mel_spec_db = librosa.power_to_db(
                mel_spec,
                ref=np.max
            )

            # create figure
            plt.figure(figsize=(3, 3))

            librosa.display.specshow(
                mel_spec_db,
                sr=sample_rate
            )

            # remove axes
            plt.axis("off")

            # remove padding
            plt.tight_layout(pad=0)

            # save path
            save_path = os.path.join(
                output_path,
                emotion,
                file.replace(".wav", ".png")
            )

            # save image
            plt.savefig(
                save_path,
                bbox_inches="tight",
                pad_inches=0
            )

            plt.close()

print("\nDataset generation complete.")