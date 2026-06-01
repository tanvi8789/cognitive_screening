import torch

from torch.utils.data import DataLoader
from torch.utils.data import random_split

from src.deep_learning.audio_dataset import AudioDataset


def get_audio_dataloaders():

    dataset = AudioDataset(
        "datasets/ravdess"
    )

    train_size = int(
        0.8 * len(dataset)
    )

    test_size = (
        len(dataset)
        - train_size
    )

    train_dataset, test_dataset = random_split(
        dataset,
        [train_size, test_size],
        generator=torch.Generator().manual_seed(42)
    )

    train_loader = DataLoader(
        train_dataset,
        batch_size=32,
        shuffle=True
    )

    test_loader = DataLoader(
        test_dataset,
        batch_size=32,
        shuffle=False
    )

    return train_loader, test_loader