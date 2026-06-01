import librosa

from src.utils.audio_converter import convert_to_wav


def load_audio(file_path):

    wav_path = convert_to_wav(file_path)

    audio, sr = librosa.load(
        wav_path,
        sr=None
    )

    return audio, sr, wav_path