import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


audio_path = "datasets/ravdess/Actor_01/03-01-01-01-01-01-01.wav"

# load audio
audio, sample_rate = librosa.load(audio_path, sr=22050)

# create Mel spectrogram
mel_spec = librosa.feature.melspectrogram(
    y=audio,
    sr=sample_rate,
    n_mels=128
)

# convert to decibels
mel_spec_db = librosa.power_to_db(
    mel_spec,
    ref= np.max
)

# plot
plt.figure(figsize=(10, 4))

librosa.display.specshow(
    mel_spec_db,
    sr=sample_rate,
    x_axis="time",
    y_axis="mel"
)

plt.colorbar(format="%+2.0f dB")

plt.title("Mel Spectrogram")

plt.tight_layout()

output_path = "spectrograms/neutral_example.png"

plt.savefig(output_path)

plt.show()

plt.close()