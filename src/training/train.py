import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)
from sklearn.model_selection import train_test_split

from src.features.feature_extraction import load_dataset

dataset_path = "datasets/ravdess"

print("Loading dataset...")

X, y = load_dataset(dataset_path)

print("Dataset loaded.")
print(X.shape)

# encode labels
label_encoder = LabelEncoder()

y_encoded = label_encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

print("Training model...")

model.fit(X_train, y_train)

print("Training complete.")

y_pred = model.predict(X_test)

# convert back to emotion names
y_test_labels = label_encoder.inverse_transform(y_test)
y_pred_labels = label_encoder.inverse_transform(y_pred)

accuracy = accuracy_score(y_test_labels, y_pred_labels)

print(f"\nAccuracy: {accuracy:.4f}")

print("\nClassification Report:")
print(classification_report(y_test_labels, y_pred_labels))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test_labels, y_pred_labels))

joblib.dump(model, "models/emotion_classifier.pkl")
joblib.dump(label_encoder, "models/label_encoder.pkl")

print("\nModel and label encoder saved.")

