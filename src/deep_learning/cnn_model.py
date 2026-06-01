import torch
import torch.nn as nn
import torch.nn.functional as F


class EmotionCNN(nn.Module):

    def __init__(self):

        super(EmotionCNN, self).__init__()

        self.conv1 = nn.Conv2d(
            in_channels=1,
            out_channels=16,
            kernel_size=3,
            padding=1
        )

        self.conv2 = nn.Conv2d(
            in_channels=16,
            out_channels=32,
            kernel_size=3,
            padding=1
        )

        self.pool = nn.MaxPool2d(
            kernel_size=2,
            stride=2
        )

        self.dropout = nn.Dropout(0.5)

        self.fc1 = nn.Linear(
            32 * 32 * 32,
            128
        )

        self.fc2 = nn.Linear(
            128,
            8
        )

    def forward(self, x):

        x = self.pool(
            F.relu(self.conv1(x))
        )

        x = self.pool(
            F.relu(self.conv2(x))
        )

        x = x.view(x.size(0), -1)

        x = self.dropout(x)

        x = F.relu(self.fc1(x))

        x = self.fc2(x)

        return x