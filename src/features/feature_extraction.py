# src/features/feature_extraction.py

import os
import numpy as np
import librosa

# Emotion mapping
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

def extract_emotion(filename):
    parts = filename.split("-")
    emotion_code = parts[2]

    return emotions.get(emotion_code)

def extract_features(file_path):

    # load audio
    audio, sample_rate = librosa.load(file_path, sr=None)

    features = []

    # =========================
    # MFCC FEATURES
    # =========================
    mfccs = librosa.feature.mfcc(
        y=audio,
        sr=sample_rate,
        n_mfcc=40
    )

    mfccs_mean = np.mean(mfccs.T, axis=0)

    features.extend(mfccs_mean)

    # =========================
    # CHROMA FEATURES
    # =========================
    chroma = librosa.feature.chroma_stft(
        y=audio,
        sr=sample_rate
    )

    chroma_mean = np.mean(chroma.T, axis=0)

    features.extend(chroma_mean)

    # =========================
    # RMS ENERGY
    # =========================
    rms = librosa.feature.rms(y=audio)

    rms_mean = np.mean(rms.T, axis=0)

    features.extend(rms_mean)

    # =========================
    # ZERO CROSSING RATE
    # =========================
    zcr = librosa.feature.zero_crossing_rate(audio)

    zcr_mean = np.mean(zcr.T, axis=0)

    features.extend(zcr_mean)

    # =========================
    # SPECTRAL CENTROID
    # =========================
    spectral_centroid = librosa.feature.spectral_centroid(
        y=audio,
        sr=sample_rate
    )

    spectral_centroid_mean = np.mean(
        spectral_centroid.T,
        axis=0
    )

    features.extend(spectral_centroid_mean)

    features = np.array(features)

    return features


def load_dataset(dataset_path):

    X = []
    y = []

    for root, dirs, files in os.walk(dataset_path):

        for file in files:

            if file.endswith(".wav"):

                file_path = os.path.join(root, file)

                # extract emotion
                emotion = extract_emotion(file)

                # extract features
                features = extract_features(file_path)

                X.append(features)
                y.append(emotion)

    return np.array(X), np.array(y)


if __name__ == "__main__":

    dataset_path = "datasets/ravdess"

    X, y = load_dataset(dataset_path)

    print("Feature Shape:", X.shape)
    print("Labels Shape:", y.shape)

    print("First Feature Vector:")
    print(X[0])

    print("First Label:")
    print(y[0])
