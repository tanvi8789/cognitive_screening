import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.metrics import (

    accuracy_score,

    classification_report,

    confusion_matrix,

    roc_auc_score
)

df = pd.read_csv(
    "datasets/parkinsons/parkinsons.data"
)

print(df.head())

print("\nShape:")
print(df.shape)

print("\nClass Distribution:")
print(df["status"].value_counts())

X = df.drop(
    columns=["name", "status"]
)

y = df["status"]

print(X.shape)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.2,

    random_state=42,

    stratify=y
)

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(

    n_estimators=200,

    random_state=42,

    class_weight="balanced"
)

model.fit(
    X_train,
    y_train
)


predictions = model.predict(
    X_test
)

print("\nAccuracy:")
print(
    accuracy_score(
        y_test,
        predictions
    )
)

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        predictions
    )
)

print("\nConfusion Matrix:")
print(
    confusion_matrix(
        y_test,
        predictions
    )
)

scores = cross_val_score(

    model,

    X,

    y,

    cv=5,

    scoring="f1"
)

print(scores)

print(scores.mean())

feature_importance = pd.DataFrame({

    "Feature": X.columns,

    "Importance":
        model.feature_importances_

})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

print(feature_importance.head(10))

probabilities = model.predict_proba(X_test)[:, 1]

roc_auc = roc_auc_score(
    y_test,
    probabilities
)

print(
    f"ROC-AUC: {roc_auc:.4f}" 
) 

import shap

print("Creating SHAP explainer...")

explainer = shap.Explainer(
    model,
    X_train
)

print("Generating SHAP values...")

shap_values = explainer(
    X_test
)

print("Shape:")
print(shap_values.values.shape)

# Select Parkinson's class
shap.plots.beeswarm(
    shap_values[:, :, 1],
    max_display=15
)