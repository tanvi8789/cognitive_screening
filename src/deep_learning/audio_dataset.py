import os
import torch
import librosa
import numpy as np

from torch.utils.data import Dataset


EMOTIONS = {
    "01": 0,  # neutral
    "02": 1,  # calm
    "03": 2,  # happy
    "04": 3,  # sad
    "05": 4,  # angry
    "06": 5,  # fearful
    "07": 6,  # disgust
    "08": 7   # surprised
}


class AudioDataset(Dataset):

    def __init__(self, dataset_path):

        self.samples = []

        for root, dirs, files in os.walk(dataset_path):

            for file in files:

                if file.endswith(".wav"):

                    emotion_code = file.split("-")[2]

                    label = EMOTIONS[emotion_code]

                    self.samples.append(
                        (
                            os.path.join(root, file),
                            label
                        )
                    )

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):

        file_path, label = self.samples[idx]

        audio, sr = librosa.load(
            file_path,
            sr=22050
        )

        mel_spec = librosa.feature.melspectrogram(
            y=audio,
            sr=sr,
            n_mels=128
        )

        mel_spec = librosa.power_to_db(
            mel_spec,
            ref=np.max
        )

        # fixed size
        mel_spec = librosa.util.fix_length(
            mel_spec,
            size=128,
            axis=1
        )

        mel_spec = torch.tensor(
            mel_spec,
            dtype=torch.float32
        )

        # add channel dimension
        mel_spec = mel_spec.unsqueeze(0)

        return mel_spec, label