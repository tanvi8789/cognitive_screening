import sys
import joblib
import numpy as np

from src.features.feature_extraction import extract_features


# load trained model
model = joblib.load("models/emotion_classifier.pkl")

# load label encoder
label_encoder = joblib.load("models/label_encoder.pkl")


def predict_emotion(audio_path):

    # extract features
    features = extract_features(audio_path)

    # reshape for sklearn
    features = features.reshape(1, -1)

    # predict class
    prediction = model.predict(features)

    # prediction probabilities
    probabilities = model.predict_proba(features)

    # highest confidence
    confidence = np.max(probabilities) * 100

    # convert numeric label back to emotion
    emotion = label_encoder.inverse_transform(prediction)[0]

    return emotion, confidence


if __name__ == "__main__":

    # check command line argument
    if len(sys.argv) < 2:
        print("Usage: python -m src.inference.predict path/to/audio.wav")
        sys.exit()

    audio_path = sys.argv[1]

    try:

        emotion, confidence = predict_emotion(audio_path)

        print(f"\nPredicted Emotion: {emotion}")
        print(f"Confidence: {confidence:.2f}%")

    except FileNotFoundError:
        print("Error: Audio file not found.")

    except Exception as e:
        print(f"Error: {e}")