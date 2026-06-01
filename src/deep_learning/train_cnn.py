import os

import torch
import torch.nn as nn
import torch.optim as optim

from src.deep_learning.audio_loader import get_audio_dataloaders
from src.deep_learning.cnn_model import EmotionCNN


# device
device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

print(f"Using device: {device}")


# data
train_loader, test_loader = get_audio_dataloaders()


# model
model = EmotionCNN().to(device)


# loss
criterion = nn.CrossEntropyLoss()


# optimizer
optimizer = optim.Adam(
    model.parameters(),
    lr=0.001
)


# create models folder
os.makedirs("models", exist_ok=True)


best_accuracy = 0


epochs = 25


for epoch in range(epochs):

    # =========================
    # TRAINING
    # =========================

    model.train()

    running_loss = 0

    train_correct = 0
    train_total = 0

    for images, labels in train_loader:

        images = images.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()

        outputs = model(images)

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        running_loss += loss.item()

        _, predicted = torch.max(outputs, 1)

        train_total += labels.size(0)

        train_correct += (
            predicted == labels
        ).sum().item()

    train_accuracy = (
        100 * train_correct / train_total
    )

    # =========================
    # TESTING
    # =========================

    model.eval()

    test_correct = 0
    test_total = 0

    with torch.no_grad():

        for images, labels in test_loader:

            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)

            _, predicted = torch.max(outputs, 1)

            test_total += labels.size(0)

            test_correct += (
                predicted == labels
            ).sum().item()

    test_accuracy = (
        100 * test_correct / test_total
    )

    # =========================
    # SAVE BEST MODEL
    # =========================

    if test_accuracy > best_accuracy:

        best_accuracy = test_accuracy

        torch.save(
            model.state_dict(),
            "models/emotion_cnn_best.pth"
        )

        print(
            f"New best model saved "
            f"({best_accuracy:.2f}%)"
        )

    # =========================
    # LOGGING
    # =========================

    print(
        f"Epoch [{epoch+1}/{epochs}] | "
        f"Loss: {running_loss:.4f} | "
        f"Train Acc: {train_accuracy:.2f}% | "
        f"Test Acc: {test_accuracy:.2f}%"
    )


print("\nTraining complete.")
print(
    f"Best Test Accuracy: "
    f"{best_accuracy:.2f}%"
)